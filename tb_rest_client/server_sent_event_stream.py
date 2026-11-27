#  Copyright 2026. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from json import loads
from re import compile

DEFAULT_CHUNK_SIZE = 1024
DEFAULT_EVENT_NAME = 'message'
ENCODING = 'utf-8'
COMMENT_PREFIX = ':'
FIELD_SEPARATOR = ':'
EVENT_FIELD = 'event'
DATA_FIELD = 'data'
DATA_LINES_SEPARATOR = '\n'
LINE_BREAK = compile(rb'\r\n|\r|\n')


class ServerSentEventStream:
    def __init__(self, response, chunk_size=DEFAULT_CHUNK_SIZE):
        self.__response = response
        self.__events = self.__read_events(response, chunk_size)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.__events)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.__events.close()
        self.__release(self.__response)

    @classmethod
    def __read_events(cls, response, chunk_size):
        event_name, data_lines = None, []
        try:
            for line in cls.__read_lines(response, chunk_size):
                if line.startswith(COMMENT_PREFIX):
                    continue

                if line:
                    field, value = cls.__parse_field(line)
                    if field == EVENT_FIELD:
                        event_name = value
                    elif field == DATA_FIELD:
                        data_lines.append(value)
                    continue

                if event_name is not None or data_lines:
                    yield event_name or DEFAULT_EVENT_NAME, cls.__parse_data(data_lines)
                event_name, data_lines = None, []
        finally:
            cls.__release(response)

    @classmethod
    def __read_lines(cls, response, chunk_size):
        rest = b''
        for chunk in response.stream(chunk_size):
            lines, rest = cls.__split_complete_lines(rest + chunk)
            for line in lines:
                yield cls.__decode(line)

        *lines, unfinished_line = LINE_BREAK.split(rest)
        for line in lines:
            yield cls.__decode(line)

    @staticmethod
    def __split_complete_lines(text):
        unfinished_line_break = b'\r' if text.endswith(b'\r') else b''
        *lines, rest = LINE_BREAK.split(text.removesuffix(unfinished_line_break))
        return lines, rest + unfinished_line_break

    @staticmethod
    def __decode(line):
        return line.decode(ENCODING, errors='replace')

    @staticmethod
    def __parse_field(line):
        field, _, value = line.partition(FIELD_SEPARATOR)
        return field, value.removeprefix(' ')

    @staticmethod
    def __parse_data(data_lines):
        data = DATA_LINES_SEPARATOR.join(data_lines)
        try:
            return loads(data)
        except ValueError:
            return data

    @staticmethod
    def __release(response):
        response.close()
        response.release_conn()
