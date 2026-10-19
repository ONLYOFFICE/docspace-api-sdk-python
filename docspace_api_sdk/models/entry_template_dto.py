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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.entry_field_dto import EntryFieldDto
from docspace_api_sdk.models.metadata_conflict_resolve_type import MetadataConflictResolveType
from typing import Optional, Set
from typing_extensions import Self

class EntryTemplateDto(BaseModel):
    """
    A metadata template assigned to an entry: the template with every field of it, each field carrying its value on the entry.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The template ID.", json_schema_extra={"examples": [3]})
    name: Optional[StrictStr] = Field(default=None, description="The template name.", json_schema_extra={"examples": ["Project"]})
    visible: Optional[StrictBool] = Field(default=None, description="Specifies if the template is visible in the UI pickers.", json_schema_extra={"examples": [True]})
    cascade: Optional[StrictBool] = Field(default=None, description="Whether the template cascades from this entry to the folders and files below it. Only a folder or a room can  cascade; on a file the value is always false.", json_schema_extra={"examples": [True]})
    conflict_resolve_type: Optional[MetadataConflictResolveType] = Field(default=None, description="How the cascade of this entry treats a value an entry below already holds. Null while the template does not  cascade from this entry.", alias="conflictResolveType")
    fields: Optional[List[EntryFieldDto]] = Field(default=None, description="The template fields with their values on the entry.", json_schema_extra={"examples": [[{"id": 9, "name": "Customer", "type": 0, "order": 0, "value": {"stringValue": "ACME Corp"}}]]})
    __properties: ClassVar[List[str]] = ["id", "name", "visible", "cascade", "conflictResolveType", "fields"]

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
        """Create an instance of EntryTemplateDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EntryTemplateDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "visible": obj.get("visible"),
            "cascade": obj.get("cascade"),
            "conflictResolveType": obj.get("conflictResolveType"),
            "fields": [EntryFieldDto.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None
        })
        return _obj


