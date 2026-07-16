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
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionBalanceInfo(BaseModel):
    """
    The information about the current subscription and its unused balance.
    """ # noqa: E501
    total_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total cost of the current billing period (the sum across all subscription items).", alias="totalCost")
    currency: Optional[StrictStr] = Field(default=None, description="The three-character ISO 4217 currency symbol of the subscription.")
    period_start: Optional[datetime] = Field(default=None, description="The start of the current billing period.", alias="periodStart")
    period_end: Optional[datetime] = Field(default=None, description="The end of the current billing period.", alias="periodEnd")
    period_used_until: Optional[datetime] = Field(default=None, description="The boundary of the used part of the period (the moment of the request).", alias="periodUsedUntil")
    days_elapsed: Optional[StrictInt] = Field(default=None, description="The number of days elapsed since the start of the period (inclusive).", alias="daysElapsed")
    remaining_balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unused balance of the subscription, in the subscription currency.", alias="remainingBalance")
    remaining_balance_in_wallet_currency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The unused balance of the subscription, converted to the wallet currency.", alias="remainingBalanceInWalletCurrency")
    wallet_currency: Optional[StrictStr] = Field(default=None, description="The three-character ISO 4217 currency symbol of the wallet.", alias="walletCurrency")
    __properties: ClassVar[List[str]] = ["totalCost", "currency", "periodStart", "periodEnd", "periodUsedUntil", "daysElapsed", "remainingBalance", "remainingBalanceInWalletCurrency", "walletCurrency"]

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
        """Create an instance of SubscriptionBalanceInfo from a JSON string"""
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

        # set to None if wallet_currency (nullable) is None
        # and model_fields_set contains the field
        if self.wallet_currency is None and "wallet_currency" in self.model_fields_set:
            _dict['walletCurrency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionBalanceInfo from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalCost": obj.get("totalCost"),
            "currency": obj.get("currency"),
            "periodStart": obj.get("periodStart"),
            "periodEnd": obj.get("periodEnd"),
            "periodUsedUntil": obj.get("periodUsedUntil"),
            "daysElapsed": obj.get("daysElapsed"),
            "remainingBalance": obj.get("remainingBalance"),
            "remainingBalanceInWalletCurrency": obj.get("remainingBalanceInWalletCurrency"),
            "walletCurrency": obj.get("walletCurrency")
        })
        return _obj


