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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace_api_sdk.models.service_limit_period import ServiceLimitPeriod
from docspace_api_sdk.models.service_limit_scope import ServiceLimitScope
from typing import Optional, Set
from typing_extensions import Self

class UserServiceLimitDto(BaseModel):
    """
    The spending limit on the AI services in force for one user: the user's personal limit, or else the limit for every  user, together with the money the user spent against it in the current period.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The service limit ID, used to read, change, switch off or delete the limit through the  `api/2.0/portal/payment/servicelimit` operations. For the limit for every user it is the same for all users.", json_schema_extra={"examples": [42]})
    scope: Optional[ServiceLimitScope] = Field(default=None, description="Whether the limit is the user's own (`Custom`) or the limit for every user (`Global`) the user falls back to.")
    amount_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The most money the AI services may cost the user per period, in `currency`. It is the only threshold a limit on  the AI services has: their services count in different units, so a threshold on a quantity is refused for them.", alias="amountValue", json_schema_extra={"examples": [40]})
    amount_consumed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The money the AI services cost the user in the current period, in `currency`; 0 when nothing was spent yet,  including a user who has never used the AI services.", alias="amountConsumed", json_schema_extra={"examples": [12.5]})
    currency: Optional[StrictStr] = Field(default=None, description="The currency `amountValue` and `amountConsumed` are expressed in; null when the limit has no money threshold.", json_schema_extra={"examples": ["USD"]})
    period: Optional[ServiceLimitPeriod] = Field(default=None, description="The window the threshold applies to. It resets at the start of the next day, week or month in UTC (a week on  Monday), not a fixed time after the first charge; a lifetime limit never resets.")
    period_end: Optional[datetime] = Field(default=None, description="The moment the current period ends and the spending starts over from zero, in UTC. Null for a lifetime limit,  which never resets.", alias="periodEnd", json_schema_extra={"examples": ["2026-10-20T23:59:59.9999999Z"]})
    __properties: ClassVar[List[str]] = ["id", "scope", "amountValue", "amountConsumed", "currency", "period", "periodEnd"]

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
        """Create an instance of UserServiceLimitDto from a JSON string"""
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
        # set to None if amount_value (nullable) is None
        # and model_fields_set contains the field
        if self.amount_value is None and "amount_value" in self.model_fields_set:
            _dict['amountValue'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if period_end (nullable) is None
        # and model_fields_set contains the field
        if self.period_end is None and "period_end" in self.model_fields_set:
            _dict['periodEnd'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserServiceLimitDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "scope": obj.get("scope"),
            "amountValue": obj.get("amountValue"),
            "amountConsumed": obj.get("amountConsumed"),
            "currency": obj.get("currency"),
            "period": obj.get("period"),
            "periodEnd": obj.get("periodEnd")
        })
        return _obj


