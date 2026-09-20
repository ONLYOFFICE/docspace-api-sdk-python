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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SmtpSettingsDto(BaseModel):
    """
    The mail server the portal sends its letters through.
    """ # noqa: E501
    host: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The host name or address of the mail server. On a cloud portal that has saved no relay of its own every  field of this object comes back empty, because the installation's own server is not disclosed - only  `isDefaultSettings` is set there.", json_schema_extra={"examples": ["mail.example.com"]})
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=None, description="The port the mail server is reached on - conventionally 25 or 587 without encryption from the start, 465  with it. It is empty when no port was stored, in which case the portal falls back to its own default.", json_schema_extra={"examples": [25]})
    sender_address: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The address the letters are sent from, which appears in the From header and is what a reply goes to.", alias="senderAddress", json_schema_extra={"examples": ["notify@example.com"]})
    sender_display_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The name shown beside that address in a recipient's mailbox.", alias="senderDisplayName", json_schema_extra={"examples": ["Postman"]})
    credentials_user_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The account the portal signs in to the mail server as, meaningful only while `enableAuth` is `true`.", alias="credentialsUserName", json_schema_extra={"examples": ["notify@example.com"]})
    credentials_user_password: Optional[StrictStr] = Field(default=None, description="Always empty here: the stored password is never returned, so a client that sends these settings back has  to supply it again rather than echoing what it read.", alias="credentialsUserPassword", json_schema_extra={"examples": [""]})
    enable_ssl: Optional[StrictBool] = Field(default=None, description="Whether the connection to the mail server is encrypted.", alias="enableSSL", json_schema_extra={"examples": [True]})
    enable_auth: Optional[StrictBool] = Field(default=None, description="Whether the portal signs in to the mail server at all. While it is `false` the credentials above are  ignored and the server is expected to accept mail unauthenticated.", alias="enableAuth", json_schema_extra={"examples": [True]})
    use_ntlm: Optional[StrictBool] = Field(default=None, description="Always `false` here: the flag is accepted when settings are saved but is not stored, so it never comes  back set and says nothing about how the portal authenticates.", alias="useNtlm", json_schema_extra={"examples": [False]})
    is_default_settings: Optional[StrictBool] = Field(default=None, description="Whether the portal is still on the mail configuration of the installation rather than on a relay of its  own. `DELETE api/2.0/smtpsettings/smtp` puts it back to `true`, and while it is `true` on a cloud portal  the fields above are blank rather than showing the installation's server.", alias="isDefaultSettings", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["host", "port", "senderAddress", "senderDisplayName", "credentialsUserName", "credentialsUserPassword", "enableSSL", "enableAuth", "useNtlm", "isDefaultSettings"]

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
        """Create an instance of SmtpSettingsDto from a JSON string"""
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
        # set to None if host (nullable) is None
        # and model_fields_set contains the field
        if self.host is None and "host" in self.model_fields_set:
            _dict['host'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if sender_address (nullable) is None
        # and model_fields_set contains the field
        if self.sender_address is None and "sender_address" in self.model_fields_set:
            _dict['senderAddress'] = None

        # set to None if sender_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.sender_display_name is None and "sender_display_name" in self.model_fields_set:
            _dict['senderDisplayName'] = None

        # set to None if credentials_user_name (nullable) is None
        # and model_fields_set contains the field
        if self.credentials_user_name is None and "credentials_user_name" in self.model_fields_set:
            _dict['credentialsUserName'] = None

        # set to None if credentials_user_password (nullable) is None
        # and model_fields_set contains the field
        if self.credentials_user_password is None and "credentials_user_password" in self.model_fields_set:
            _dict['credentialsUserPassword'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SmtpSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": obj.get("host"),
            "port": obj.get("port"),
            "senderAddress": obj.get("senderAddress"),
            "senderDisplayName": obj.get("senderDisplayName"),
            "credentialsUserName": obj.get("credentialsUserName"),
            "credentialsUserPassword": obj.get("credentialsUserPassword"),
            "enableSSL": obj.get("enableSSL"),
            "enableAuth": obj.get("enableAuth"),
            "useNtlm": obj.get("useNtlm"),
            "isDefaultSettings": obj.get("isDefaultSettings")
        })
        return _obj


