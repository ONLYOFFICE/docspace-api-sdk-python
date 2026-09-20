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
from docspace_api_sdk.models.api_date_time import ApiDateTime
from typing import Optional, Set
from typing_extensions import Self

class ActiveConnectionsItemDto(BaseModel):
    """
    One open connection of a user: where the sign-in behind it came from, and the ID it can be closed by.
    """ # noqa: E501
    id: StrictInt = Field(description="The ID of the sign-in this connection was opened by. Pass it as `loginEventId` to  `PUT api/2.0/security/activeconnections/logout/{loginEventId}` to end this one connection; the item whose  value equals `loginEvent` is the connection the current request uses.", json_schema_extra={"examples": [1]})
    tenant_id: StrictInt = Field(description="The portal the sign-in was made on. The operation never crosses portals, so it is the current one on every  item.", alias="tenantId", json_schema_extra={"examples": [1]})
    user_id: UUID = Field(description="The user the connection belongs to, which is the calling user on every item - the operation cannot report  anyone else's connections.", alias="userId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    mobile: Optional[StrictBool] = Field(default=None, description="Whether the sign-in came from a mobile client. No mobile marker is stored with a connection, so the value  is `false` on every item and tells a caller nothing about the device.", json_schema_extra={"examples": [True]})
    ip: Optional[StrictStr] = Field(default=None, description="The IP address the sign-in came from, with the port stripped off. On the item that matches `loginEvent` it  is taken from the address the current request arrives from instead of the one stored at sign-in.", json_schema_extra={"examples": ["192.0.2.1"]})
    country: Optional[StrictStr] = Field(default=None, description="The English name of the country the IP address is located in. It is empty when the address cannot be  located, which is the normal outcome for private and loopback addresses.", json_schema_extra={"examples": ["United States"]})
    city: Optional[StrictStr] = Field(default=None, description="The city the IP address is located in, empty under the same conditions as `country`.", json_schema_extra={"examples": ["New York"]})
    browser: Optional[StrictStr] = Field(default=None, description="The browser and its version as parsed from the user agent of the sign-in, empty when the client sent no  recognisable one. It is refreshed from the current request on the item that matches `loginEvent`.", json_schema_extra={"examples": ["Chrome 120.0"]})
    platform: Optional[StrictStr] = Field(default=None, description="The operating system as parsed from the user agent of the sign-in, refreshed and left empty under the same  conditions as `browser`.", json_schema_extra={"examples": ["Windows"]})
    var_date: Optional[ApiDateTime] = Field(default=None, description="When the sign-in happened, in the portal time zone rather than in UTC.", alias="date")
    page: Optional[StrictStr] = Field(default=None, description="Where in the portal the sign-in was made from: the referrer of the request that created it, or that  request's own path when it carried no referrer. Long values are cut off at 512 characters.", json_schema_extra={"examples": ["/rooms/shared"]})
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


