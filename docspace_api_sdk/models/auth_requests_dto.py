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
from docspace_api_sdk.models.confirm_data import ConfirmData
from docspace_api_sdk.models.recaptcha_type import RecaptchaType
from typing import Optional, Set
from typing_extensions import Self

class AuthRequestsDto(BaseModel):
    """
    The credentials a sign-in is attempted with: a portal password, a confirmation key, or a third-party account.
    """ # noqa: E501
    user_name: Optional[StrictStr] = Field(default=None, description="The account signing in, given as its email address or its portal user name. It is required for a password  sign-in and ignored when the credentials are a confirmation key or a third-party account.", alias="userName", json_schema_extra={"examples": ["user@example.com"]})
    password: Optional[StrictStr] = Field(default=None, description="The password in the clear. Send either this or `passwordHash`, never both; hashing it in the client with the  parameters from `GET api/2.0/settings?withpassword=true` and sending `passwordHash` instead keeps the plain  password off the wire.", json_schema_extra={"examples": ["SecurePassword123!"]})
    password_hash: Optional[StrictStr] = Field(default=None, description="The password already hashed in the client. It has to be produced with the `salt`, iteration count and hash  size that `GET api/2.0/settings?withpassword=true` publishes, or the portal cannot recognise it; a value sent  here takes the place of `password`.", alias="passwordHash", json_schema_extra={"examples": ["5f4dcc3b5aa765d61d8327deb882cf99"]})
    provider: Optional[StrictStr] = Field(default=None, description="The third-party identity provider the account is being signed in through, by its internal key such as  `google` or `linkedin`. Sending it switches the call to a third-party sign-in, which needs `accessToken` or  `serializedProfile` and is only allowed on a self-hosted installation or a tariff that includes third-party  sign-in.", json_schema_extra={"examples": ["google"]})
    access_token: Optional[StrictStr] = Field(default=None, description="The access token the provider named in `provider` issued for the account, passed on unchanged for the portal  to verify with that provider. The portal then matches the address it gets back against its own accounts, so a  valid token for an address unknown here is answered as no such user.", alias="accessToken", json_schema_extra={"examples": ["ya29.a0AfH6SMBx..."]})
    serialized_profile: Optional[StrictStr] = Field(default=None, description="The third-party profile already fetched and serialised by the caller, as an alternative to `accessToken` for  a provider whose profile the client holds. It identifies the account by the address it carries.", alias="serializedProfile", json_schema_extra={"examples": ["{\"name\":\"John Doe\",\"email\":\"john@example.com\"}"]})
    code_o_auth: Optional[StrictStr] = Field(default=None, description="The OAuth authorization code obtained from the provider, for a flow that has not been exchanged for an access  token yet. It is recorded with the sign-in rather than replacing `accessToken`.", alias="codeOAuth", json_schema_extra={"examples": ["4/0AY0e-g7..."]})
    session: Optional[StrictBool] = Field(default=None, description="Whether the issued token is tied to the browser session. When it is, the answer carries no `expires` and the  token dies with the session; otherwise it lives for the portal session lifetime.", json_schema_extra={"examples": [True]})
    confirm_data: Optional[ConfirmData] = Field(default=None, description="The confirmation link data, as a third way to identify the account beside a password and a third-party  account. Send it when the sign-in comes from a link the portal mailed, in which case `userName` and the  password fields are not read.", alias="confirmData")
    recaptcha_type: Optional[RecaptchaType] = Field(default=None, description="Which CAPTCHA service the proof in `recaptchaResponse` came from. It has to match the service the  installation is configured with, which `GET api/2.0/settings` publishes together with the site key.", alias="recaptchaType")
    recaptcha_response: Optional[StrictStr] = Field(default=None, description="The token the CAPTCHA widget produced in the browser, passed on unchanged for the portal to verify. It is  only demanded once repeated failures have made the portal ask for a challenge, and it is single-use, so a  retry needs a freshly solved one.", alias="recaptchaResponse", json_schema_extra={"examples": ["03AGdBq25..."]})
    culture: Optional[StrictStr] = Field(default=None, description="The language the sign-in messages and any letter that follows are written in, as a culture name such as  `en-US`. A culture the installation does not have falls back to the portal language.", json_schema_extra={"examples": ["en-US"]})
    __properties: ClassVar[List[str]] = ["userName", "password", "passwordHash", "provider", "accessToken", "serializedProfile", "codeOAuth", "session", "confirmData", "recaptchaType", "recaptchaResponse", "culture"]

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
        """Create an instance of AuthRequestsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of confirm_data
        if self.confirm_data:
            _dict['confirmData'] = self.confirm_data.to_dict()
        # set to None if user_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_name is None and "user_name" in self.model_fields_set:
            _dict['userName'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if password_hash (nullable) is None
        # and model_fields_set contains the field
        if self.password_hash is None and "password_hash" in self.model_fields_set:
            _dict['passwordHash'] = None

        # set to None if provider (nullable) is None
        # and model_fields_set contains the field
        if self.provider is None and "provider" in self.model_fields_set:
            _dict['provider'] = None

        # set to None if access_token (nullable) is None
        # and model_fields_set contains the field
        if self.access_token is None and "access_token" in self.model_fields_set:
            _dict['accessToken'] = None

        # set to None if serialized_profile (nullable) is None
        # and model_fields_set contains the field
        if self.serialized_profile is None and "serialized_profile" in self.model_fields_set:
            _dict['serializedProfile'] = None

        # set to None if code_o_auth (nullable) is None
        # and model_fields_set contains the field
        if self.code_o_auth is None and "code_o_auth" in self.model_fields_set:
            _dict['codeOAuth'] = None

        # set to None if recaptcha_response (nullable) is None
        # and model_fields_set contains the field
        if self.recaptcha_response is None and "recaptcha_response" in self.model_fields_set:
            _dict['recaptchaResponse'] = None

        # set to None if culture (nullable) is None
        # and model_fields_set contains the field
        if self.culture is None and "culture" in self.model_fields_set:
            _dict['culture'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthRequestsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "userName": obj.get("userName"),
            "password": obj.get("password"),
            "passwordHash": obj.get("passwordHash"),
            "provider": obj.get("provider"),
            "accessToken": obj.get("accessToken"),
            "serializedProfile": obj.get("serializedProfile"),
            "codeOAuth": obj.get("codeOAuth"),
            "session": obj.get("session"),
            "confirmData": ConfirmData.from_dict(obj["confirmData"]) if obj.get("confirmData") is not None else None,
            "recaptchaType": obj.get("recaptchaType"),
            "recaptchaResponse": obj.get("recaptchaResponse"),
            "culture": obj.get("culture")
        })
        return _obj


