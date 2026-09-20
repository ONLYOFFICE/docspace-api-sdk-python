#
# (c) Copyright Ascensio System SIA 2026
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
#



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetReferenceDataDto(BaseModel):
    """
    The body of a spreadsheet reference request: the source spreadsheet, and the three ways of naming the document it  refers to, which are tried in the order they are described.
    """ # noqa: E501
    file_key: Optional[StrictStr] = Field(description="The id of the referenced file as the document service recorded it in the formula. It is tried first, and only  when `instanceId` names this portal.", alias="fileKey", json_schema_extra={"examples": ["512"]})
    instance_id: Optional[StrictStr] = Field(description="The portal the reference was made on, as the document service recorded it. Only the id of this portal makes  the file key resolvable; any other value falls through to the path and the link.", alias="instanceId", json_schema_extra={"examples": ["1"]})
    source_file_id: Optional[StrictInt] = Field(default=None, description="The spreadsheet the formula sits in. The path is resolved against it - the referenced file is looked for among  the files lying next to it - and it is the file whose read access is checked.", alias="sourceFileId", json_schema_extra={"examples": [1]})
    path: Optional[StrictStr] = Field(default=None, description="The title of the referenced file exactly as the formula spells it, matched against the files lying next to the  source file. It is tried after the file key, and only when no link is given.", json_schema_extra={"examples": ["Budget 2026.xlsx"]})
    link: Optional[StrictStr] = Field(default=None, description="The web address the formula points at, an editor link of this portal or one of its short links. It is tried  last, and an address belonging to another site is not resolved at all but handed back for the client to follow  as it is.", json_schema_extra={"examples": ["https://portal.example.com/doc/512"]})
    __properties: ClassVar[List[str]] = ["fileKey", "instanceId", "sourceFileId", "path", "link"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetReferenceDataDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if file_key (nullable) is None
        # and model_fields_set contains the field
        if self.file_key is None and "file_key" in self.model_fields_set:
            _dict['fileKey'] = None

        # set to None if instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.instance_id is None and "instance_id" in self.model_fields_set:
            _dict['instanceId'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetReferenceDataDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fileKey": obj.get("fileKey"),
            "instanceId": obj.get("instanceId"),
            "sourceFileId": obj.get("sourceFileId"),
            "path": obj.get("path"),
            "link": obj.get("link")
        })
        return _obj


