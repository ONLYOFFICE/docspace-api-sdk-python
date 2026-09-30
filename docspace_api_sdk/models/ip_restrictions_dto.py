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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ip_restriction_base import IpRestrictionBase
from typing import Optional, Set
from typing_extensions import Self

class IpRestrictionsDto(BaseModel):
    """
    The addresses allowed to reach the portal, and whether the restriction is enforced.
    """ # noqa: E501
    ip_restrictions: Optional[List[IpRestrictionBase]] = Field(description="The allowed addresses, each entry pairing a single IPv4 or IPv6 address with the flag that limits it to  administrators. This is the whole list that is to hold afterwards: entries not repeated here are deleted.  Ranges written as `from-to` and CIDR blocks are refused with 400, even though the portal matches such forms  when they are already stored. Enforcement spares only the portal owner and the installation own networks, so  a list without the caller address locks the remaining administrators out.", alias="ipRestrictions", json_schema_extra={"examples": [[{"ip": "192.0.2.1", "forAdmin": False}]]})
    enable: Optional[StrictBool] = Field(default=None, description="Whether the list is enforced. Leaving it out follows the list - on when addresses are sent, off when the list  is empty - and sending `true` with an empty list is refused with 400, since that would admit nobody.", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["ipRestrictions", "enable"]

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
        """Create an instance of IpRestrictionsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ip_restrictions (list)
        _items = []
        if self.ip_restrictions:
            for _item_ip_restrictions in self.ip_restrictions:
                if _item_ip_restrictions:
                    _items.append(_item_ip_restrictions.to_dict())
            _dict['ipRestrictions'] = _items
        # set to None if ip_restrictions (nullable) is None
        # and model_fields_set contains the field
        if self.ip_restrictions is None and "ip_restrictions" in self.model_fields_set:
            _dict['ipRestrictions'] = None

        # set to None if enable (nullable) is None
        # and model_fields_set contains the field
        if self.enable is None and "enable" in self.model_fields_set:
            _dict['enable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IpRestrictionsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipRestrictions": [IpRestrictionBase.from_dict(_item) for _item in obj["ipRestrictions"]] if obj.get("ipRestrictions") is not None else None,
            "enable": obj.get("enable")
        })
        return _obj


