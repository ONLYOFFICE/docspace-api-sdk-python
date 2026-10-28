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

class AiMetadataMatchDto(BaseModel):
    """
    Where a text search met the metadata of a file, a folder or a room: one string value that holds the searched text,  with the field it belongs to.
    """ # noqa: E501
    template_id: Optional[StrictInt] = Field(default=None, description="The ID of the metadata template the matching field belongs to. Null for a custom field, which belongs to no  template the API shows.", alias="templateId", json_schema_extra={"examples": [3]})
    field_id: Optional[StrictInt] = Field(default=None, description="The ID of the matching template field. Null for a custom field, which is addressed by its name alone.", alias="fieldId", json_schema_extra={"examples": [12]})
    field_name: Optional[StrictStr] = Field(default=None, description="The name of the matching field: the template field or the custom field as it is shown in the entry metadata.", alias="fieldName", json_schema_extra={"examples": ["Client"]})
    value: Optional[StrictStr] = Field(default=None, description="The stored value that holds the searched text, as it was written, not only the matching part of it.", json_schema_extra={"examples": ["ACME Corporation"]})
    __properties: ClassVar[List[str]] = ["templateId", "fieldId", "fieldName", "value"]

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
        """Create an instance of AiMetadataMatchDto from a JSON string"""
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
        # set to None if template_id (nullable) is None
        # and model_fields_set contains the field
        if self.template_id is None and "template_id" in self.model_fields_set:
            _dict['templateId'] = None

        # set to None if field_id (nullable) is None
        # and model_fields_set contains the field
        if self.field_id is None and "field_id" in self.model_fields_set:
            _dict['fieldId'] = None

        # set to None if field_name (nullable) is None
        # and model_fields_set contains the field
        if self.field_name is None and "field_name" in self.model_fields_set:
            _dict['fieldName'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiMetadataMatchDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "templateId": obj.get("templateId"),
            "fieldId": obj.get("fieldId"),
            "fieldName": obj.get("fieldName"),
            "value": obj.get("value")
        })
        return _obj


