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
from typing import Optional, Set
from typing_extensions import Self

class UpcomingPaymentDto(BaseModel):
    """
    One charge the portal is going to be billed for at the start of the next period.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The quota that is going to be charged. When a switch to another quota is scheduled, this is the quota  being switched to, so it can differ from what `GET api/2.0/portal/tariff` reports for today.", json_schema_extra={"examples": [-11]})
    name: Optional[StrictStr] = Field(default=None, description="The quota's stable key, which is the same identifier the wallet operations use for a service.", json_schema_extra={"examples": ["storage"]})
    title: Optional[StrictStr] = Field(default=None, description="The quota name in the portal language, meant to be printed on an invoice preview.", json_schema_extra={"examples": ["Business plan"]})
    unit_of_measure: Optional[StrictStr] = Field(default=None, description="What `quantity` counts, in the portal language - seats, administrators, gigabytes. It is empty for a quota  that is simply on or off.", alias="unitOfMeasure", json_schema_extra={"examples": ["admins"]})
    quantity: Optional[StrictInt] = Field(default=None, description="How much is going to be charged for, which is the quantity scheduled for the next period when one has been  scheduled and today's quantity otherwise.", json_schema_extra={"examples": [100]})
    wallet: Optional[StrictBool] = Field(default=None, description="Whether the charge is paid out of the portal wallet rather than from the subscription.", json_schema_extra={"examples": [True]})
    due_date: Optional[ApiDateTime] = Field(default=None, description="When the charge falls due, in the portal time zone.", alias="dueDate")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="What the charge comes to: the unit price of the quota multiplied by `quantity`. Taxes are not part of it,  and a quota with no price of its own is not listed at all rather than listed with a zero.", json_schema_extra={"examples": [14]})
    currency: Optional[StrictStr] = Field(default=None, description="The currency `amount` is expressed in, as a three-letter ISO 4217 code. It follows the portal's billing  account, so every entry of one answer carries the same code.", json_schema_extra={"examples": ["USD"]})
    __properties: ClassVar[List[str]] = ["id", "name", "title", "unitOfMeasure", "quantity", "wallet", "dueDate", "amount", "currency"]

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
        """Create an instance of UpcomingPaymentDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of due_date
        if self.due_date:
            _dict['dueDate'] = self.due_date.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if unit_of_measure (nullable) is None
        # and model_fields_set contains the field
        if self.unit_of_measure is None and "unit_of_measure" in self.model_fields_set:
            _dict['unitOfMeasure'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpcomingPaymentDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "title": obj.get("title"),
            "unitOfMeasure": obj.get("unitOfMeasure"),
            "quantity": obj.get("quantity"),
            "wallet": obj.get("wallet"),
            "dueDate": ApiDateTime.from_dict(obj["dueDate"]) if obj.get("dueDate") is not None else None,
            "amount": obj.get("amount"),
            "currency": obj.get("currency")
        })
        return _obj


