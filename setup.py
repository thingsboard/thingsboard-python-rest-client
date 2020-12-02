# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

from setuptools import setup, find_packages  # noqa: H301
from os import path

NAME = "tb-rest-client32"
VERSION = "1.2"
REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

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
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    download_url='https://github.com/thingsboard/python_tb_rest_client/archive/%s.tar.gz' % VERSION,
    python_requires=">=3.5",
)
