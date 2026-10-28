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
from docspace_api_sdk.models.metadata_field_option_dto import MetadataFieldOptionDto
from docspace_api_sdk.models.metadata_field_type import MetadataFieldType
from typing import Optional, Set
from typing_extensions import Self

class MetadataFieldDto(BaseModel):
    """
    The metadata field information.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The field ID.", json_schema_extra={"examples": [9]})
    template_id: Optional[StrictInt] = Field(default=None, description="The ID of the template the field belongs to.", alias="templateId", json_schema_extra={"examples": [3]})
    name: Optional[StrictStr] = Field(default=None, description="The field name.", json_schema_extra={"examples": ["Customer"]})
    type: Optional[MetadataFieldType] = Field(default=None, description="The field type.")
    options: Optional[List[MetadataFieldOptionDto]] = Field(default=None, description="The choice options of the field.", json_schema_extra={"examples": [[{"id": "4f1e2d3c-5b6a-4788-99aa-0c1d2e3f4a55", "value": "Red"}]]})
    order: Optional[StrictInt] = Field(default=None, description="The field display order inside the template.", json_schema_extra={"examples": [0]})
    __properties: ClassVar[List[str]] = ["id", "templateId", "name", "type", "options", "order"]

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
        """Create an instance of MetadataFieldDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item_options in self.options:
                if _item_options:
                    _items.append(_item_options.to_dict())
            _dict['options'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if options (nullable) is None
        # and model_fields_set contains the field
        if self.options is None and "options" in self.model_fields_set:
            _dict['options'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetadataFieldDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "templateId": obj.get("templateId"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "options": [MetadataFieldOptionDto.from_dict(_item) for _item in obj["options"]] if obj.get("options") is not None else None,
            "order": obj.get("order")
        })
        return _obj


