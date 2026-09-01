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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from docspace_api_sdk.models.employee_dto import EmployeeDto
from typing import Optional, Set
from typing_extensions import Self

class ApiKeyResponseDto(BaseModel):
    """
    The response data for the API key operations.
    """ # noqa: E501
    id: UUID = Field(description="The API key unique identifier.", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    name: Optional[StrictStr] = Field(description="The API key name.", json_schema_extra={"examples": ["My API Key"]})
    key: Optional[StrictStr] = Field(description="The full API key value (only returned when creating a new key).", json_schema_extra={"examples": ["api_key_1234567890abcdef"]})
    key_postfix: Optional[StrictStr] = Field(default=None, description="The API key postfix (used for identification).", alias="keyPostfix", json_schema_extra={"examples": ["...cdef"]})
    permissions: Optional[List[StrictStr]] = Field(description="The list of permissions granted to the API key.", json_schema_extra={"examples": [["read", "write", "delete"]]})
    last_used: Optional[datetime] = Field(default=None, description="The date and time when the API key was last used.", alias="lastUsed", json_schema_extra={"examples": ["2025-06-15T10:30:00.0000000Z"]})
    create_on: Optional[datetime] = Field(default=None, description="The date and time when the API key was created.", alias="createOn", json_schema_extra={"examples": ["2025-06-15T10:30:00.0000000Z"]})
    create_by: Optional[EmployeeDto] = Field(default=None, description="The identifier of the user who created the API key.", alias="createBy")
    expires_at: Optional[datetime] = Field(default=None, description="The date and time when the API key expires.", alias="expiresAt", json_schema_extra={"examples": ["2025-06-15T10:30:00.0000000Z"]})
    is_active: StrictBool = Field(description="Indicates whether the API key is active or not.", alias="isActive", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["id", "name", "key", "keyPostfix", "permissions", "lastUsed", "createOn", "createBy", "expiresAt", "isActive"]

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
        """Create an instance of ApiKeyResponseDto from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if key_postfix (nullable) is None
        # and model_fields_set contains the field
        if self.key_postfix is None and "key_postfix" in self.model_fields_set:
            _dict['keyPostfix'] = None

        # set to None if permissions (nullable) is None
        # and model_fields_set contains the field
        if self.permissions is None and "permissions" in self.model_fields_set:
            _dict['permissions'] = None

        # set to None if last_used (nullable) is None
        # and model_fields_set contains the field
        if self.last_used is None and "last_used" in self.model_fields_set:
            _dict['lastUsed'] = None

        # set to None if create_on (nullable) is None
        # and model_fields_set contains the field
        if self.create_on is None and "create_on" in self.model_fields_set:
            _dict['createOn'] = None

        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expiresAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiKeyResponseDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "key": obj.get("key"),
            "keyPostfix": obj.get("keyPostfix"),
            "permissions": obj.get("permissions"),
            "lastUsed": obj.get("lastUsed"),
            "createOn": obj.get("createOn"),
            "createBy": EmployeeDto.from_dict(obj["createBy"]) if obj.get("createBy") is not None else None,
            "expiresAt": obj.get("expiresAt"),
            "isActive": obj.get("isActive")
        })
        return _obj


