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
from typing import Optional, Set
from typing_extensions import Self

class FirebaseDeviceDto(BaseModel):
    """
    One mobile device of the calling user registered for push notifications.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The id of the registration.", json_schema_extra={"examples": [1]})
    user_id: Optional[UUID] = Field(default=None, description="The account the device belongs to; always the caller.", alias="userId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    tenant_id: Optional[StrictInt] = Field(default=None, description="The portal the registration belongs to; always the current one.", alias="tenantId", json_schema_extra={"examples": [1]})
    firebase_device_token: Optional[StrictStr] = Field(default=None, description="The Firebase token the device was issued, as it was sent at registration.", alias="firebaseDeviceToken", json_schema_extra={"examples": ["fcm-token-123"]})
    application: Optional[StrictStr] = Field(default=None, description="The application the registration is for; `doc` for the Documents application.", json_schema_extra={"examples": ["doc"]})
    is_subscribed: Optional[StrictBool] = Field(default=None, description="Whether the device is currently sent push notifications.", alias="isSubscribed", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["id", "userId", "tenantId", "firebaseDeviceToken", "application", "isSubscribed"]

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
        """Create an instance of FirebaseDeviceDto from a JSON string"""
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
        # set to None if firebase_device_token (nullable) is None
        # and model_fields_set contains the field
        if self.firebase_device_token is None and "firebase_device_token" in self.model_fields_set:
            _dict['firebaseDeviceToken'] = None

        # set to None if application (nullable) is None
        # and model_fields_set contains the field
        if self.application is None and "application" in self.model_fields_set:
            _dict['application'] = None

        # set to None if is_subscribed (nullable) is None
        # and model_fields_set contains the field
        if self.is_subscribed is None and "is_subscribed" in self.model_fields_set:
            _dict['isSubscribed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FirebaseDeviceDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "userId": obj.get("userId"),
            "tenantId": obj.get("tenantId"),
            "firebaseDeviceToken": obj.get("firebaseDeviceToken"),
            "application": obj.get("application"),
            "isSubscribed": obj.get("isSubscribed")
        })
        return _obj


