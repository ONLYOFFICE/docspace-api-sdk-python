# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace.models.api_date_time import ApiDateTime
from docspace.models.employee_dto import EmployeeDto
from typing import Optional, Set
from typing_extensions import Self

class ApiKeyResponseDto(BaseModel):
    """
    The response data for the API key operations.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the API key.")
    name: Optional[StrictStr] = Field(default=None, description="The API key name.")
    key: Optional[StrictStr] = Field(default=None, description="The full API key value (only returned when creating a new key).")
    key_postfix: Optional[StrictStr] = Field(default=None, description="The API key postfix (used for identification).", alias="keyPostfix")
    permissions: Optional[List[StrictStr]] = Field(default=None, description="The list of permissions granted to the API key.")
    last_used: Optional[ApiDateTime] = Field(default=None, alias="lastUsed")
    create_on: Optional[ApiDateTime] = Field(default=None, alias="createOn")
    create_by: Optional[EmployeeDto] = Field(default=None, alias="createBy")
    expires_at: Optional[ApiDateTime] = Field(default=None, alias="expiresAt")
    is_active: Optional[StrictBool] = Field(default=None, description="Indicates whether the API key is active or not.", alias="isActive")
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
        # override the default output from pydantic by calling `to_dict()` of last_used
        if self.last_used:
            _dict['lastUsed'] = self.last_used.to_dict()
        # override the default output from pydantic by calling `to_dict()` of create_on
        if self.create_on:
            _dict['createOn'] = self.create_on.to_dict()
        # override the default output from pydantic by calling `to_dict()` of create_by
        if self.create_by:
            _dict['createBy'] = self.create_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expires_at
        if self.expires_at:
            _dict['expiresAt'] = self.expires_at.to_dict()
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
            "lastUsed": ApiDateTime.from_dict(obj["lastUsed"]) if obj.get("lastUsed") is not None else None,
            "createOn": ApiDateTime.from_dict(obj["createOn"]) if obj.get("createOn") is not None else None,
            "createBy": EmployeeDto.from_dict(obj["createBy"]) if obj.get("createBy") is not None else None,
            "expiresAt": ApiDateTime.from_dict(obj["expiresAt"]) if obj.get("expiresAt") is not None else None,
            "isActive": obj.get("isActive")
        })
        return _obj


