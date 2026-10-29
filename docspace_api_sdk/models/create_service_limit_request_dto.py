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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from uuid import UUID
from docspace_api_sdk.models.service_limit_period import ServiceLimitPeriod
from docspace_api_sdk.models.service_limit_scope import ServiceLimitScope
from typing import Optional, Set
from typing_extensions import Self

class CreateServiceLimitRequestDto(BaseModel):
    """
    The spending limit to create on the AI services: for the portal as a whole, for every user, or for one user.
    """ # noqa: E501
    scope: Optional[ServiceLimitScope] = Field(default=None, description="Whom the limit applies to.")
    user_id: Optional[UUID] = Field(default=None, description="The ID of the portal user a personal limit is set for, as returned in `id` by the people operations.", alias="userId", json_schema_extra={"examples": ["3f2504e0-4f89-11d3-9a0c-0305e82c3301"]})
    amount_value: Optional[Union[Annotated[float, Field(le=10000, strict=True, ge=0)], Annotated[int, Field(le=10000, strict=True, ge=0)]]] = Field(default=None, description="The most money the AI services may cost per period, in their currency, which cannot be chosen. Zero blocks the  AI services completely.", alias="amountValue", json_schema_extra={"examples": [50]})
    quantity_value: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(default=None, description="The largest quantity the AI services may consume per period, in their common unit. Zero blocks the AI services  completely.", alias="quantityValue", json_schema_extra={"examples": [1000]})
    period: Optional[ServiceLimitPeriod] = Field(default=None, description="The window the thresholds apply to, in UTC. A day, week or month is calendar-aligned rather than rolling - a  daily limit resets at midnight UTC, a weekly one on Monday - while a lifetime limit counts from its creation and  never resets.")
    __properties: ClassVar[List[str]] = ["scope", "userId", "amountValue", "quantityValue", "period"]

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
        """Create an instance of CreateServiceLimitRequestDto from a JSON string"""
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
        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['userId'] = None

        # set to None if amount_value (nullable) is None
        # and model_fields_set contains the field
        if self.amount_value is None and "amount_value" in self.model_fields_set:
            _dict['amountValue'] = None

        # set to None if quantity_value (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_value is None and "quantity_value" in self.model_fields_set:
            _dict['quantityValue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateServiceLimitRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scope": obj.get("scope"),
            "userId": obj.get("userId"),
            "amountValue": obj.get("amountValue"),
            "quantityValue": obj.get("quantityValue"),
            "period": obj.get("period")
        })
        return _obj


