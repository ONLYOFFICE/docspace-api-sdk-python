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
from typing import Optional, Set
from typing_extensions import Self

class ActiveServiceDto(BaseModel):
    """
    Represents an active wallet service (quota) of the current portal.
    """ # noqa: E501
    service: Optional[StrictStr] = Field(default=None, description="The name of the service.", json_schema_extra={"examples": ["disk-storage"]})
    service_unit: Optional[StrictStr] = Field(default=None, description="The unit of measurement for the service.", alias="serviceUnit", json_schema_extra={"examples": ["GB"]})
    subscription: Optional[StrictBool] = Field(default=None, description="Indicates whether the service is subscription-based.", json_schema_extra={"examples": [True]})
    title: Optional[StrictStr] = Field(default=None, description="The title of the service.", json_schema_extra={"examples": ["Additional disk storage"]})
    limit: Optional[StrictInt] = Field(default=None, description="The service limit. Populated only for the subscription-based services.", json_schema_extra={"examples": [500]})
    used: Optional[StrictInt] = Field(default=None, description="The current service usage. Populated only for the subscription-based services.", json_schema_extra={"examples": [320]})
    __properties: ClassVar[List[str]] = ["service", "serviceUnit", "subscription", "title", "limit", "used"]

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
        """Create an instance of ActiveServiceDto from a JSON string"""
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
        # set to None if service (nullable) is None
        # and model_fields_set contains the field
        if self.service is None and "service" in self.model_fields_set:
            _dict['service'] = None

        # set to None if service_unit (nullable) is None
        # and model_fields_set contains the field
        if self.service_unit is None and "service_unit" in self.model_fields_set:
            _dict['serviceUnit'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if used (nullable) is None
        # and model_fields_set contains the field
        if self.used is None and "used" in self.model_fields_set:
            _dict['used'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ActiveServiceDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "service": obj.get("service"),
            "serviceUnit": obj.get("serviceUnit"),
            "subscription": obj.get("subscription"),
            "title": obj.get("title"),
            "limit": obj.get("limit"),
            "used": obj.get("used")
        })
        return _obj


