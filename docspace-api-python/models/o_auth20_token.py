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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OAuth20Token(BaseModel):
    """
    OAuth20Token
    """ # noqa: E501
    access_token: Optional[StrictStr] = None
    refresh_token: Optional[StrictStr] = None
    expires_in: Optional[StrictInt] = None
    client_id: Optional[StrictStr] = None
    client_secret: Optional[StrictStr] = None
    redirect_uri: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    is_expired: Optional[StrictBool] = Field(default=None, alias="isExpired")
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


