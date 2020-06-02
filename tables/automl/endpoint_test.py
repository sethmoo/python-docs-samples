#!/usr/bin/env python

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from google.api_core import exceptions
import pytest

import automl_tables_set_endpoint
from google.cloud import automl_v1beta1 as automl
from google.api_core.client_options import ClientOptions

PROJECT = os.environ["GCLOUD_PROJECT"]


def test_client_creation(capsys):
    client = automl_tables_set_endpoint.create_client_with_endpoint(PROJECT)
    print(client.list_datasets())
    out, _ = capsys.readouterr()
    assert "GRPCIterator" in out
