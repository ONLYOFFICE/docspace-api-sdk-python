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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OAuth20Token(BaseModel):
    """
    The OAuth 2.0 token issued by a third-party provider.
    """ # noqa: E501
    access_token: Optional[StrictStr] = Field(default=None, description="The token sent to the provider with every request made on behalf of the account.", json_schema_extra={"examples": ["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."]})
    refresh_token: Optional[StrictStr] = Field(default=None, description="The token used to obtain a new access token when the current one expires. A provider that issues no refresh  token leaves it empty, and the account then has to be connected again to keep working.", json_schema_extra={"examples": ["def50200a1b2c3d4e5f6..."]})
    expires_in: Optional[StrictInt] = Field(default=None, description="How long the access token stays usable, in seconds counted from `timestamp`. Zero means the provider did not  say, and the token is then treated as expired.", json_schema_extra={"examples": [3600]})
    client_id: Optional[StrictStr] = Field(default=None, description="The OAuth 2.0 client ID of the application the token was issued to.", json_schema_extra={"examples": ["my-client-id"]})
    client_secret: Optional[StrictStr] = Field(default=None, description="The client secret of the application the token was issued to, needed when the token is refreshed.", json_schema_extra={"examples": ["my-client-secret"]})
    redirect_uri: Optional[StrictStr] = Field(default=None, description="The redirect URL the authorization code behind this token was obtained with; providers require the same value  again when the token is refreshed.", json_schema_extra={"examples": ["https://app.example.com/callback"]})
    timestamp: Optional[datetime] = Field(default=None, description="When the token was issued, in UTC. This is the point `expires_in` is counted from.", json_schema_extra={"examples": ["2026-01-01T00:00:00Z"]})
    is_expired: Optional[StrictBool] = Field(default=None, description="Whether the access token can no longer be used and has to be refreshed. It is also true when the provider did  not say how long the token lives.", alias="isExpired", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["access_token", "refresh_token", "expires_in", "client_id", "client_secret", "redirect_uri", "timestamp", "isExpired"]

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
        """Create an instance of OAuth20Token from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "is_expired",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if access_token (nullable) is None
        # and model_fields_set contains the field
        if self.access_token is None and "access_token" in self.model_fields_set:
            _dict['access_token'] = None

        # set to None if refresh_token (nullable) is None
        # and model_fields_set contains the field
        if self.refresh_token is None and "refresh_token" in self.model_fields_set:
            _dict['refresh_token'] = None

        # set to None if client_id (nullable) is None
        # and model_fields_set contains the field
        if self.client_id is None and "client_id" in self.model_fields_set:
            _dict['client_id'] = None

        # set to None if client_secret (nullable) is None
        # and model_fields_set contains the field
        if self.client_secret is None and "client_secret" in self.model_fields_set:
            _dict['client_secret'] = None

        # set to None if redirect_uri (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_uri is None and "redirect_uri" in self.model_fields_set:
            _dict['redirect_uri'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth20Token from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access_token": obj.get("access_token"),
            "refresh_token": obj.get("refresh_token"),
            "expires_in": obj.get("expires_in"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "redirect_uri": obj.get("redirect_uri"),
            "timestamp": obj.get("timestamp"),
            "isExpired": obj.get("isExpired")
        })
        return _obj


