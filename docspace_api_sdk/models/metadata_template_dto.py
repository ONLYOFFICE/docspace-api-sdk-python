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
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.employee_dto import EmployeeDto
from docspace_api_sdk.models.metadata_field_dto import MetadataFieldDto
from typing import Optional, Set
from typing_extensions import Self

class MetadataTemplateDto(BaseModel):
    """
    The metadata template information.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The template ID.", json_schema_extra={"examples": [3]})
    name: Optional[StrictStr] = Field(default=None, description="The template name.", json_schema_extra={"examples": ["Contracts"]})
    visible: Optional[StrictBool] = Field(default=None, description="Specifies if the template is visible in the UI pickers.", json_schema_extra={"examples": [True]})
    create_by: Optional[EmployeeDto] = Field(default=None, description="The user who created the template. A user who has since left the portal comes back as the lost user placeholder.", alias="createBy")
    create_on: Optional[ApiDateTime] = Field(default=None, description="The template creation date.", alias="createOn")
    modified_by: Optional[EmployeeDto] = Field(default=None, description="The user who changed the template itself last: its name or its visibility. The creator until somebody changes  it; a change of a field is recorded on the field, not here.", alias="modifiedBy")
    modified_on: Optional[ApiDateTime] = Field(default=None, description="The date when the template was modified last.", alias="modifiedOn")
    fields: Optional[List[MetadataFieldDto]] = Field(default=None, description="The template metadata fields.", json_schema_extra={"examples": [[{"id": 9, "templateId": 3, "name": "Customer", "type": 0, "order": 0}]]})
    __properties: ClassVar[List[str]] = ["id", "name", "visible", "createBy", "createOn", "modifiedBy", "modifiedOn", "fields"]

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
        """Create an instance of MetadataTemplateDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of create_by
        if self.create_by:
            _dict['createBy'] = self.create_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of create_on
        if self.create_on:
            _dict['createOn'] = self.create_on.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_by
        if self.modified_by:
            _dict['modifiedBy'] = self.modified_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_on
        if self.modified_on:
            _dict['modifiedOn'] = self.modified_on.to_dict()
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
        """Create an instance of MetadataTemplateDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "visible": obj.get("visible"),
            "createBy": EmployeeDto.from_dict(obj["createBy"]) if obj.get("createBy") is not None else None,
            "createOn": ApiDateTime.from_dict(obj["createOn"]) if obj.get("createOn") is not None else None,
            "modifiedBy": EmployeeDto.from_dict(obj["modifiedBy"]) if obj.get("modifiedBy") is not None else None,
            "modifiedOn": ApiDateTime.from_dict(obj["modifiedOn"]) if obj.get("modifiedOn") is not None else None,
            "fields": [MetadataFieldDto.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None
        })
        return _obj


