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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self

class TfaSettingsDto(BaseModel):
    """
    One two-factor authentication method the portal offers, with the portal-wide state of that method.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(description="Which method this entry describes: `sms` for a code sent by text message, `app` for a code from an  authenticator application. It is the value `PUT api/2.0/settings/tfaapp` takes as its `type`, and no other  value ever appears here.", json_schema_extra={"examples": ["app"]})
    title: Optional[StrictStr] = Field(description="The label for the method in the portal language, meant for a button or a radio option. It is not stable  enough to branch on - match `id` for that.", json_schema_extra={"examples": ["Authenticator app"]})
    enabled: StrictBool = Field(description="Whether this method is the portal's current policy. At most one entry can have it set, and none has it  while the portal challenges nobody. It says nothing about the caller's own account, which may be exempt  through `trustedIps` or forced through `mandatoryUsers`.", json_schema_extra={"examples": [True]})
    available: StrictBool = Field(description="Whether the method could be switched on at all. For `sms` it is `false` until the installation has a  working SMS provider, so a method can be offered here and still be impossible to enable; for `app` it is  always `true`.", json_schema_extra={"examples": [True]})
    trusted_ips: Optional[List[StrictStr]] = Field(default=None, description="The addresses that skip the challenge, each either a single address, a `from-to` pair or a CIDR range. It  is empty when no address is exempt, which means every account is challenged.", alias="trustedIps", json_schema_extra={"examples": [["192.0.2.0/24"]]})
    mandatory_users: Optional[List[UUID]] = Field(default=None, description="The accounts that are challenged even from a trusted address, by user ID. Empty means the exemption in  `trustedIps` holds for everyone.", alias="mandatoryUsers", json_schema_extra={"examples": [["00000000-0000-0000-0000-000000000000"]]})
    mandatory_groups: Optional[List[UUID]] = Field(default=None, description="The groups whose members are challenged even from a trusted address, by group ID, with the same reading of  an empty list as `mandatoryUsers`.", alias="mandatoryGroups", json_schema_extra={"examples": [["00000000-0000-0000-0000-000000000000"]]})
    __properties: ClassVar[List[str]] = ["id", "title", "enabled", "available", "trustedIps", "mandatoryUsers", "mandatoryGroups"]

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
        """Create an instance of TfaSettingsDto from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if trusted_ips (nullable) is None
        # and model_fields_set contains the field
        if self.trusted_ips is None and "trusted_ips" in self.model_fields_set:
            _dict['trustedIps'] = None

        # set to None if mandatory_users (nullable) is None
        # and model_fields_set contains the field
        if self.mandatory_users is None and "mandatory_users" in self.model_fields_set:
            _dict['mandatoryUsers'] = None

        # set to None if mandatory_groups (nullable) is None
        # and model_fields_set contains the field
        if self.mandatory_groups is None and "mandatory_groups" in self.model_fields_set:
            _dict['mandatoryGroups'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TfaSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "enabled": obj.get("enabled"),
            "available": obj.get("available"),
            "trustedIps": obj.get("trustedIps"),
            "mandatoryUsers": obj.get("mandatoryUsers"),
            "mandatoryGroups": obj.get("mandatoryGroups")
        })
        return _obj


