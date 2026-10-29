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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ServiceLimitUsageDto(BaseModel):
    """
    What has been spent against a spending limit in its current period, and what is left.
    """ # noqa: E501
    period_start: Optional[datetime] = Field(default=None, description="The start of the current period, in UTC.", alias="periodStart", json_schema_extra={"examples": ["2026-10-18T00:00:00Z"]})
    period_end: Optional[datetime] = Field(default=None, description="The end of the current period, in UTC: the moment the spending starts again from zero. Null for a lifetime  limit, which never resets.", alias="periodEnd", json_schema_extra={"examples": ["2026-10-18T23:59:59Z"]})
    amount_consumed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The money charged in the current period, in the currency of the limit.", alias="amountConsumed", json_schema_extra={"examples": [12.5]})
    amount_available: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The money still available in the current period: the threshold less what was charged and what is reserved for  operations in progress, never below zero. Null when the limit has no money threshold.", alias="amountAvailable", json_schema_extra={"examples": [27.5]})
    quantity_consumed: Optional[StrictInt] = Field(default=None, description="The quantity consumed in the current period, in the unit of the limit.", alias="quantityConsumed", json_schema_extra={"examples": [250]})
    quantity_available: Optional[StrictInt] = Field(default=None, description="The quantity still available in the current period, never below zero; null when the limit has no quantity  threshold.", alias="quantityAvailable", json_schema_extra={"examples": [750]})
    __properties: ClassVar[List[str]] = ["periodStart", "periodEnd", "amountConsumed", "amountAvailable", "quantityConsumed", "quantityAvailable"]

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
        """Create an instance of ServiceLimitUsageDto from a JSON string"""
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
        # set to None if period_end (nullable) is None
        # and model_fields_set contains the field
        if self.period_end is None and "period_end" in self.model_fields_set:
            _dict['periodEnd'] = None

        # set to None if amount_available (nullable) is None
        # and model_fields_set contains the field
        if self.amount_available is None and "amount_available" in self.model_fields_set:
            _dict['amountAvailable'] = None

        # set to None if quantity_available (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_available is None and "quantity_available" in self.model_fields_set:
            _dict['quantityAvailable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceLimitUsageDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "periodStart": obj.get("periodStart"),
            "periodEnd": obj.get("periodEnd"),
            "amountConsumed": obj.get("amountConsumed"),
            "amountAvailable": obj.get("amountAvailable"),
            "quantityConsumed": obj.get("quantityConsumed"),
            "quantityAvailable": obj.get("quantityAvailable")
        })
        return _obj


