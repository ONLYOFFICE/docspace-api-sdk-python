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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SmtpSettingsDto(BaseModel):
    """
    The SMTP settings parameters.
    """ # noqa: E501
    host: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The SMTP host.")
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=None, description="The SMTP port.")
    sender_address: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The sender address.", alias="senderAddress")
    sender_display_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The sender display name.", alias="senderDisplayName")
    credentials_user_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The credentials username.", alias="credentialsUserName")
    credentials_user_password: Optional[StrictStr] = Field(default=None, description="The credentials user password.", alias="credentialsUserPassword")
    enable_ssl: Optional[StrictBool] = Field(default=None, description="Specifies whether the SSL is enabled or not.", alias="enableSSL")
    enable_auth: Optional[StrictBool] = Field(default=None, description="Specifies whether the authentication is enabled or not.", alias="enableAuth")
    use_ntlm: Optional[StrictBool] = Field(default=None, description="Specifies whether to use NTLM or not.", alias="useNtlm")
    is_default_settings: Optional[StrictBool] = Field(default=None, description="Specifies if the current settings are default or not.", alias="isDefaultSettings")
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


