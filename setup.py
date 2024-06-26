#  Copyright 2024. ThingsBoard
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


from setuptools import setup, find_packages  # noqa: H301
from os import path

NAME = "tb-rest-client"
VERSION = "3.7.0"

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="ThingsBoard REST API client",
    author_email="info@thingsboard.io",
    license="Apache Software License (Apache Software License 2.0)",
    url="https://thingsboard.io/docs/reference/python-rest-client/",
    keywords=["IoT", "ThingsBoard", "ThingsBoard REST API client"],
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    download_url='https://github.com/thingsboard/thingsboard-python-rest-client/archive/refs/tags/%s.tar.gz' % VERSION,
    python_requires=">=3.7",
    install_requires=[
        'certifi >= 2023.7.22',
        'six >= 1.10',
        'python_dateutil >= 2.5.3',
        'setuptools >= 21.0.0',
        'urllib3 >= 2.0.7',
        'requests>=2.31.0',
        'pyjwt==2.6.0',
    ]
)
