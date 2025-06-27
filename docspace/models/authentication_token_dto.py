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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AuthenticationTokenDto(BaseModel):
    """
    The authentication token parameters.
    """ # noqa: E501
    token: Optional[StrictStr] = Field(default=None, description="The authentication token.")
    expires: Optional[datetime] = Field(default=None, description="The token expiration time.")
    sms: Optional[StrictBool] = Field(default=None, description="Specifies if the authentication code is sent by SMS or not.")
    phone_noise: Optional[StrictStr] = Field(default=None, description="The phone number.", alias="phoneNoise")
    tfa: Optional[StrictBool] = Field(default=None, description="Specifies if the two-factor application is used or not.")
    tfa_key: Optional[StrictStr] = Field(default=None, description="The two-factor authentication key.", alias="tfaKey")
    confirm_url: Optional[StrictStr] = Field(default=None, description="The confirmation email URL.", alias="confirmUrl")
    __properties: ClassVar[List[str]] = ["token", "expires", "sms", "phoneNoise", "tfa", "tfaKey", "confirmUrl"]

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
        """Create an instance of AuthenticationTokenDto from a JSON string"""
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
        # set to None if token (nullable) is None
        # and model_fields_set contains the field
        if self.token is None and "token" in self.model_fields_set:
            _dict['token'] = None

        # set to None if phone_noise (nullable) is None
        # and model_fields_set contains the field
        if self.phone_noise is None and "phone_noise" in self.model_fields_set:
            _dict['phoneNoise'] = None

        # set to None if tfa_key (nullable) is None
        # and model_fields_set contains the field
        if self.tfa_key is None and "tfa_key" in self.model_fields_set:
            _dict['tfaKey'] = None

        # set to None if confirm_url (nullable) is None
        # and model_fields_set contains the field
        if self.confirm_url is None and "confirm_url" in self.model_fields_set:
            _dict['confirmUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthenticationTokenDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token": obj.get("token"),
            "expires": obj.get("expires"),
            "sms": obj.get("sms"),
            "phoneNoise": obj.get("phoneNoise"),
            "tfa": obj.get("tfa"),
            "tfaKey": obj.get("tfaKey"),
            "confirmUrl": obj.get("confirmUrl")
        })
        return _obj


