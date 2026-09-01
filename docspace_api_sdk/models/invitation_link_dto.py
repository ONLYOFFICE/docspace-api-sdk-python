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
from uuid import UUID
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.employee_type import EmployeeType
from typing import Optional, Set
from typing_extensions import Self

class InvitationLinkDto(BaseModel):
    """
    The invitation link parameters.
    """ # noqa: E501
    id: Optional[UUID] = Field(default=None, description="The ID of the invitation link.", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    employee_type: EmployeeType = Field(description="The user type.", alias="employeeType")
    expiration: Optional[ApiDateTime] = Field(default=None, description="The API date and time parameters.")
    is_expired: Optional[StrictBool] = Field(default=None, description="Indicates whether the invitation link has expired.", alias="isExpired", json_schema_extra={"examples": [True]})
    max_use_count: Optional[StrictInt] = Field(default=None, description="The maximum number of times the invitation link can be used.", alias="maxUseCount", json_schema_extra={"examples": [1]})
    current_use_count: Optional[StrictInt] = Field(default=None, description="The current number of times the invitation link has been used.", alias="currentUseCount", json_schema_extra={"examples": [1]})
    url: Optional[StrictStr] = Field(default=None, description="The URL of the invitation link.", json_schema_extra={"examples": ["https://example.com"]})
    __properties: ClassVar[List[str]] = ["id", "employeeType", "expiration", "isExpired", "maxUseCount", "currentUseCount", "url"]

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
        """Create an instance of InvitationLinkDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of expiration
        if self.expiration:
            _dict['expiration'] = self.expiration.to_dict()
        # set to None if max_use_count (nullable) is None
        # and model_fields_set contains the field
        if self.max_use_count is None and "max_use_count" in self.model_fields_set:
            _dict['maxUseCount'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvitationLinkDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "employeeType": obj.get("employeeType"),
            "expiration": ApiDateTime.from_dict(obj["expiration"]) if obj.get("expiration") is not None else None,
            "isExpired": obj.get("isExpired"),
            "maxUseCount": obj.get("maxUseCount"),
            "currentUseCount": obj.get("currentUseCount"),
            "url": obj.get("url")
        })
        return _obj


