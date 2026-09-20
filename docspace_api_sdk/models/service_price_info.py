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
from docspace_api_sdk.models.discount_category import DiscountCategory
from docspace_api_sdk.models.price_status import PriceStatus
from docspace_api_sdk.models.price_time_unit import PriceTimeUnit
from docspace_api_sdk.models.time_bound import TimeBound
from typing import Optional, Set
from typing_extensions import Self

class ServicePriceInfo(BaseModel):
    """
    Represents a price of the service.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The price unique identifier.", json_schema_extra={"examples": [12345]})
    account_number: Optional[StrictInt] = Field(default=None, description="The account number.", alias="accountNumber", json_schema_extra={"examples": [1010]})
    service_id: Optional[StrictInt] = Field(default=None, description="The service ID.", alias="serviceId", json_schema_extra={"examples": [12345]})
    time_unit: Optional[PriceTimeUnit] = Field(default=None, description="The time unit the price is bound to.", alias="timeUnit")
    cost_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost price.", alias="costPrice", json_schema_extra={"examples": [1500.75]})
    extra_charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The extra charge added to the cost price.", alias="extraCharge", json_schema_extra={"examples": [1500.75]})
    service_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The resulting service price.", alias="servicePrice", json_schema_extra={"examples": [1500.75]})
    quota: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The quota the price is set for.", json_schema_extra={"examples": [100]})
    time_bound: Optional[TimeBound] = Field(default=None, description="The period the price is effective in.", alias="timeBound")
    status: Optional[PriceStatus] = Field(default=None, description="The price status.")
    created: Optional[datetime] = Field(default=None, description="The date and time when the price was created.", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    discount_category_id: Optional[StrictInt] = Field(default=None, description="The discount category ID.", alias="discountCategoryId", json_schema_extra={"examples": [12345]})
    discount_category: Optional[DiscountCategory] = Field(default=None, description="The discount category.", alias="discountCategory")
    __properties: ClassVar[List[str]] = ["id", "accountNumber", "serviceId", "timeUnit", "costPrice", "extraCharge", "servicePrice", "quota", "timeBound", "status", "created", "discountCategoryId", "discountCategory"]

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
        """Create an instance of ServicePriceInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of time_bound
        if self.time_bound:
            _dict['timeBound'] = self.time_bound.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_category
        if self.discount_category:
            _dict['discountCategory'] = self.discount_category.to_dict()
        # set to None if quota (nullable) is None
        # and model_fields_set contains the field
        if self.quota is None and "quota" in self.model_fields_set:
            _dict['quota'] = None

        # set to None if discount_category_id (nullable) is None
        # and model_fields_set contains the field
        if self.discount_category_id is None and "discount_category_id" in self.model_fields_set:
            _dict['discountCategoryId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServicePriceInfo from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accountNumber": obj.get("accountNumber"),
            "serviceId": obj.get("serviceId"),
            "timeUnit": obj.get("timeUnit"),
            "costPrice": obj.get("costPrice"),
            "extraCharge": obj.get("extraCharge"),
            "servicePrice": obj.get("servicePrice"),
            "quota": obj.get("quota"),
            "timeBound": TimeBound.from_dict(obj["timeBound"]) if obj.get("timeBound") is not None else None,
            "status": obj.get("status"),
            "created": obj.get("created"),
            "discountCategoryId": obj.get("discountCategoryId"),
            "discountCategory": DiscountCategory.from_dict(obj["discountCategory"]) if obj.get("discountCategory") is not None else None
        })
        return _obj


