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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace-api-python.models.api_date_time import ApiDateTime
from typing import Optional, Set
from typing_extensions import Self

class ActiveConnectionsItemDto(BaseModel):
    """
    The active connection item parameters.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The active connection ID.")
    tenant_id: Optional[StrictInt] = Field(default=None, description="The tenant ID.", alias="tenantId")
    user_id: Optional[StrictStr] = Field(default=None, description="The user ID.", alias="userId")
    mobile: Optional[StrictBool] = Field(default=None, description="Specifies if the active connection has a mobile phone or not.")
    ip: Optional[StrictStr] = Field(default=None, description="The IP address of the active connection.")
    country: Optional[StrictStr] = Field(default=None, description="The active connection country.")
    city: Optional[StrictStr] = Field(default=None, description="The active connection city.")
    browser: Optional[StrictStr] = Field(default=None, description="The active connection browser.")
    platform: Optional[StrictStr] = Field(default=None, description="The active connection platform.")
    var_date: Optional[ApiDateTime] = Field(default=None, alias="date")
    page: Optional[StrictStr] = Field(default=None, description="The active connection page.")
    __properties: ClassVar[List[str]] = ["id", "tenantId", "userId", "mobile", "ip", "country", "city", "browser", "platform", "date", "page"]

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
        """Create an instance of ActiveConnectionsItemDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_date
        if self.var_date:
            _dict['date'] = self.var_date.to_dict()
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
        """Create an instance of ActiveConnectionsItemDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "tenantId": obj.get("tenantId"),
            "userId": obj.get("userId"),
            "mobile": obj.get("mobile"),
            "ip": obj.get("ip"),
            "country": obj.get("country"),
            "city": obj.get("city"),
            "browser": obj.get("browser"),
            "platform": obj.get("platform"),
            "date": ApiDateTime.from_dict(obj["date"]) if obj.get("date") is not None else None,
            "page": obj.get("page")
        })
        return _obj


