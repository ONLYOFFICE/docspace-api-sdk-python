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
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self

class ActiveConnectionsItemDto(BaseModel):
    """
    The active connection item parameters.
    """ # noqa: E501
    id: StrictInt = Field(description="The active connection ID.", json_schema_extra={"examples": [1]})
    tenant_id: StrictInt = Field(description="The tenant ID.", alias="tenantId", json_schema_extra={"examples": [1]})
    user_id: UUID = Field(description="The user ID.", alias="userId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    mobile: Optional[StrictBool] = Field(default=None, description="Specifies if the active connection has a mobile phone or not.", json_schema_extra={"examples": [True]})
    ip: Optional[StrictStr] = Field(default=None, description="The IP address of the active connection.", json_schema_extra={"examples": ["192.0.2.1"]})
    country: Optional[StrictStr] = Field(default=None, description="The active connection country.", json_schema_extra={"examples": ["United States"]})
    city: Optional[StrictStr] = Field(default=None, description="The active connection city.", json_schema_extra={"examples": ["New York"]})
    browser: Optional[StrictStr] = Field(default=None, description="The active connection browser.", json_schema_extra={"examples": ["Chrome 120.0"]})
    platform: Optional[StrictStr] = Field(default=None, description="The active connection platform.", json_schema_extra={"examples": ["Windows"]})
    var_date: Optional[datetime] = Field(default=None, description="The active connection date.", alias="date", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    page: Optional[StrictStr] = Field(default=None, description="The active connection page.", json_schema_extra={"examples": ["/rooms/shared"]})
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

        # set to None if var_date (nullable) is None
        # and model_fields_set contains the field
        if self.var_date is None and "var_date" in self.model_fields_set:
            _dict['date'] = None

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
            "date": obj.get("date"),
            "page": obj.get("page")
        })
        return _obj


