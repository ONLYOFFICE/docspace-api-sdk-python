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

class DocsCloudPayment(BaseModel):
    """
    Represents the payment information of a DocsCloud tenant.
    """ # noqa: E501
    cart_id: Optional[StrictStr] = Field(default=None, description="The cart ID.", alias="cartId", json_schema_extra={"examples": ["CartId"]})
    product_id: Optional[StrictInt] = Field(default=None, description="The product ID.", alias="productId", json_schema_extra={"examples": [12345]})
    status: Optional[StrictInt] = Field(default=None, description="The payment status.", json_schema_extra={"examples": [1]})
    interval_unit: Optional[StrictInt] = Field(default=None, description="The interval unit.", alias="intervalUnit", json_schema_extra={"examples": [1]})
    is_year: Optional[StrictBool] = Field(default=None, description="Whether the payment interval is yearly.", alias="isYear", json_schema_extra={"examples": [False]})
    is_prepaid: Optional[StrictBool] = Field(default=None, description="Whether the payment is prepaid.", alias="isPrepaid", json_schema_extra={"examples": [False]})
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity.", json_schema_extra={"examples": [10]})
    currency: Optional[StrictStr] = Field(default=None, description="The three-character ISO 4217 currency symbol of the payment.", json_schema_extra={"examples": ["USD"]})
    __properties: ClassVar[List[str]] = ["cartId", "productId", "status", "intervalUnit", "isYear", "isPrepaid", "quantity", "currency"]

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
        """Create an instance of DocsCloudPayment from a JSON string"""
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
        # set to None if cart_id (nullable) is None
        # and model_fields_set contains the field
        if self.cart_id is None and "cart_id" in self.model_fields_set:
            _dict['cartId'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocsCloudPayment from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cartId": obj.get("cartId"),
            "productId": obj.get("productId"),
            "status": obj.get("status"),
            "intervalUnit": obj.get("intervalUnit"),
            "isYear": obj.get("isYear"),
            "isPrepaid": obj.get("isPrepaid"),
            "quantity": obj.get("quantity"),
            "currency": obj.get("currency")
        })
        return _obj


