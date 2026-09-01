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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from docspace_api_sdk.models.message_action import MessageAction
from typing import Optional, Set
from typing_extensions import Self

class LoginEventDto(BaseModel):
    """
    The login event parameters.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The login event ID.", json_schema_extra={"examples": [1]})
    var_date: Optional[datetime] = Field(default=None, description="The login event date.", alias="date", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    user: Optional[StrictStr] = Field(default=None, description="The user name of the login event.", json_schema_extra={"examples": ["John Doe"]})
    user_id: Optional[UUID] = Field(default=None, description="The user ID of the login event.", alias="userId", json_schema_extra={"examples": ["{}"]})
    login: Optional[StrictStr] = Field(default=None, description="The user login of the login event.", json_schema_extra={"examples": ["user@example.com"]})
    action: Optional[StrictStr] = Field(default=None, description="The login event action.", json_schema_extra={"examples": ["User logged in"]})
    action_id: Optional[MessageAction] = Field(default=None, description="The login-related action to filter events by.", alias="actionId")
    ip: Optional[StrictStr] = Field(default=None, description="The login event IP.", json_schema_extra={"examples": ["192.0.2.1"]})
    country: Optional[StrictStr] = Field(default=None, description="The login event country.", json_schema_extra={"examples": ["United States"]})
    city: Optional[StrictStr] = Field(default=None, description="The login event city.", json_schema_extra={"examples": ["New York"]})
    browser: Optional[StrictStr] = Field(default=None, description="The login event browser.", json_schema_extra={"examples": ["Chrome 120.0"]})
    platform: Optional[StrictStr] = Field(default=None, description="The login event platform.", json_schema_extra={"examples": ["Windows"]})
    page: Optional[StrictStr] = Field(default=None, description="The login event page.", json_schema_extra={"examples": ["/login"]})
    __properties: ClassVar[List[str]] = ["id", "date", "user", "userId", "login", "action", "actionId", "ip", "country", "city", "browser", "platform", "page"]

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
        """Create an instance of LoginEventDto from a JSON string"""
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
        # set to None if var_date (nullable) is None
        # and model_fields_set contains the field
        if self.var_date is None and "var_date" in self.model_fields_set:
            _dict['date'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if login (nullable) is None
        # and model_fields_set contains the field
        if self.login is None and "login" in self.model_fields_set:
            _dict['login'] = None

        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if browser (nullable) is None
        # and model_fields_set contains the field
        if self.browser is None and "browser" in self.model_fields_set:
            _dict['browser'] = None

        # set to None if platform (nullable) is None
        # and model_fields_set contains the field
        if self.platform is None and "platform" in self.model_fields_set:
            _dict['platform'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoginEventDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "date": obj.get("date"),
            "user": obj.get("user"),
            "userId": obj.get("userId"),
            "login": obj.get("login"),
            "action": obj.get("action"),
            "actionId": obj.get("actionId"),
            "ip": obj.get("ip"),
            "country": obj.get("country"),
            "city": obj.get("city"),
            "browser": obj.get("browser"),
            "platform": obj.get("platform"),
            "page": obj.get("page")
        })
        return _obj


