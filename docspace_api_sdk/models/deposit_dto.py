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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.operation_status import OperationStatus
from typing import Optional, Set
from typing_extensions import Self

class DepositDto(BaseModel):
    """
    One payment into the portal wallet: when it was made, how much it brought in, how it ended, and whether an  invoice stands behind it.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The identifier of the top-up, which is what `GET api/2.0/portal/payment/customer/deposits/{id}/invoice` takes  to read its invoice.", json_schema_extra={"examples": [15342]})
    var_date: Optional[ApiDateTime] = Field(default=None, description="When the top-up was booked, as an ISO 8601 timestamp that carries its own offset: that of the portal's time  zone, written as `Z` for a portal in UTC - the zone in which `startDate` and `endDate` without an offset are  read.", alias="date")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount that went into the wallet, in `currency`.", json_schema_extra={"examples": [100.0]})
    currency: Optional[StrictStr] = Field(default=None, description="The currency `amount` is expressed in, as a three-letter ISO 4217 code - the accounting currency of the  wallet.", json_schema_extra={"examples": ["USD"]})
    status: Optional[OperationStatus] = Field(default=None, description="How the top-up ended. A pending one is still being settled and may change later, so only a completed one has  actually raised the balance.")
    has_invoice: Optional[StrictBool] = Field(default=None, description="Whether the billing provider holds an invoice for the payment behind the top-up, which is when  `GET api/2.0/portal/payment/customer/deposits/{id}/invoice` can open it. It is `false` for a top-up whose  payment came without one, and asking for its invoice then fails with 404.", alias="hasInvoice", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["id", "date", "amount", "currency", "status", "hasInvoice"]

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
        """Create an instance of DepositDto from a JSON string"""
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
        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DepositDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "date": ApiDateTime.from_dict(obj["date"]) if obj.get("date") is not None else None,
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "status": obj.get("status"),
            "hasInvoice": obj.get("hasInvoice")
        })
        return _obj


