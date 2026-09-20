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
from typing import Optional, Set
from typing_extensions import Self

class WizardRequestsDto(BaseModel):
    """
    What the initial setup wizard needs to finish a new portal: the owner credentials and the portal locale.
    """ # noqa: E501
    email: Optional[StrictStr] = Field(description="The address the portal owner account is created with, which is also the address every administrative letter  goes to afterwards. It has to be a well-formed email address; a malformed one leaves the wizard unfinished.", json_schema_extra={"examples": ["user@example.com"]})
    password_hash: Optional[StrictStr] = Field(description="The owner password, already hashed in the client rather than sent in the clear. Hash it with the `salt`,  iteration count and hash size that `GET api/2.0/settings?withpassword=true` publishes, so the portal can  recognise it later; an empty value leaves the wizard unfinished.", alias="passwordHash", json_schema_extra={"examples": ["2DYmIoA/aYKEksFocEf6uw=="]})
    lng: Optional[StrictStr] = Field(default=None, description="The portal interface language, as a culture name such as `en-US`. It has to be one of the cultures enabled  for the installation, and an unknown one leaves the shipped default in place instead of failing the wizard.", json_schema_extra={"examples": ["en-US"]})
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone every portal date is rendered in, as an IANA identifier such as `Europe/Riga`. A value that  matches nothing falls back to UTC rather than failing the wizard.", alias="timeZone", json_schema_extra={"examples": ["UTC"]})
    ami_id: Optional[StrictStr] = Field(default=None, description="The identifier of the Amazon Machine Image the portal was launched from, for an installation started from an  AWS image. It is recorded for the installation record only and changes nothing about the portal; leave it out  anywhere else.", alias="amiId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000001"]})
    subscribe_from_site: Optional[StrictBool] = Field(default=None, description="Whether the owner agrees to receive product news at the address in `email`. It is a mailing consent and has  no bearing on the portal notifications, which are subscribed separately.", alias="subscribeFromSite", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["email", "passwordHash", "lng", "timeZone", "amiId", "subscribeFromSite"]

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
        """Create an instance of WizardRequestsDto from a JSON string"""
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
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if password_hash (nullable) is None
        # and model_fields_set contains the field
        if self.password_hash is None and "password_hash" in self.model_fields_set:
            _dict['passwordHash'] = None

        # set to None if lng (nullable) is None
        # and model_fields_set contains the field
        if self.lng is None and "lng" in self.model_fields_set:
            _dict['lng'] = None

        # set to None if time_zone (nullable) is None
        # and model_fields_set contains the field
        if self.time_zone is None and "time_zone" in self.model_fields_set:
            _dict['timeZone'] = None

        # set to None if ami_id (nullable) is None
        # and model_fields_set contains the field
        if self.ami_id is None and "ami_id" in self.model_fields_set:
            _dict['amiId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WizardRequestsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "passwordHash": obj.get("passwordHash"),
            "lng": obj.get("lng"),
            "timeZone": obj.get("timeZone"),
            "amiId": obj.get("amiId"),
            "subscribeFromSite": obj.get("subscribeFromSite")
        })
        return _obj


