# Copyright 2022 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from marshmallow import Schema, fields


class PipelineSchema(Schema):
    config_id = fields.String()
    owner_id = fields.String()
    tasks = fields.List(fields.String)
    properties = fields.Dict()


class PipelineResponseSchema(PipelineSchema):
    id = fields.String()
    subscribers = fields.List(fields.Dict)
