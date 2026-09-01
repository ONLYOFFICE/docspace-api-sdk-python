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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CustomerMonthlyUsageDto(BaseModel):
    """
    Aggregated customer spending for a single calendar month.
    """ # noqa: E501
    year: Optional[StrictInt] = Field(default=None, description="The calendar year.", json_schema_extra={"examples": [2025]})
    month: Optional[StrictInt] = Field(default=None, description="The calendar month (1-12).", json_schema_extra={"examples": [1]})
    currency: Optional[StrictStr] = Field(default=None, description="The three-character ISO 4217 currency symbol of the amounts.", json_schema_extra={"examples": ["USD"]})
    total_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount charged across all services in this month.", alias="totalAmount", json_schema_extra={"examples": [199.98]})
    operation_count: Optional[StrictInt] = Field(default=None, description="The number of individual purchase operations in this month.", alias="operationCount", json_schema_extra={"examples": [3]})
    __properties: ClassVar[List[str]] = ["year", "month", "currency", "totalAmount", "operationCount"]

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
        """Create an instance of CustomerMonthlyUsageDto from a JSON string"""
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
        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerMonthlyUsageDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "year": obj.get("year"),
            "month": obj.get("month"),
            "currency": obj.get("currency"),
            "totalAmount": obj.get("totalAmount"),
            "operationCount": obj.get("operationCount")
        })
        return _obj


