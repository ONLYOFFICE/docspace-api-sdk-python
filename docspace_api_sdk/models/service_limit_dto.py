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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from uuid import UUID
from docspace_api_sdk.models.service_limit_period import ServiceLimitPeriod
from docspace_api_sdk.models.service_limit_scope import ServiceLimitScope
from docspace_api_sdk.models.service_limit_usage_dto import ServiceLimitUsageDto
from typing import Optional, Set
from typing_extensions import Self

class ServiceLimitDto(BaseModel):
    """
    A spending limit on the AI services: for the portal as a whole, for every user, or for one user.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The service limit ID, used to read, change, switch off or delete the limit. In the list of the users the same  ID repeats for every user the limit for every user applies to.", json_schema_extra={"examples": [42]})
    service_group_name: Optional[StrictStr] = Field(default=None, description="The limited service group; the AI services are `ai-services`.", alias="serviceGroupName", json_schema_extra={"examples": ["ai-services"]})
    customer_account_number: Optional[StrictInt] = Field(default=None, description="The number of the billing account of the portal the limit belongs to.", alias="customerAccountNumber", json_schema_extra={"examples": [12345]})
    scope: Optional[ServiceLimitScope] = Field(default=None, description="Whom the limit applies to.")
    user_id: Optional[UUID] = Field(default=None, description="The ID of the portal user the limit applies to: the user of a personal limit, or, in the list of the users, the  user a limit for every user applies to. Null for a limit of the portal as a whole, and for a limit for every  user read on its own.", alias="userId", json_schema_extra={"examples": ["3f2504e0-4f89-11d3-9a0c-0305e82c3301"]})
    amount_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The most money the AI services may cost per period, in `currency`; null when the limit has no money threshold.", alias="amountValue", json_schema_extra={"examples": [50]})
    currency: Optional[StrictStr] = Field(default=None, description="The currency `amountValue` is expressed in; null when the limit has no money threshold.", json_schema_extra={"examples": ["USD"]})
    quantity_value: Optional[StrictInt] = Field(default=None, description="The largest quantity the AI services may consume per period, in `serviceUnit`; null when the limit has no  quantity threshold.", alias="quantityValue", json_schema_extra={"examples": [1000]})
    service_unit: Optional[StrictStr] = Field(default=None, description="The unit `quantityValue` is expressed in; null when the limit has no quantity threshold.", alias="serviceUnit", json_schema_extra={"examples": ["request"]})
    period: Optional[ServiceLimitPeriod] = Field(default=None, description="The window the thresholds apply to. A day, week or month resets at the start of the next one in UTC (a week on  Monday), not a fixed time after the first charge; a lifetime limit never resets.")
    period_end: Optional[datetime] = Field(default=None, description="The last moment of the current period, in UTC, after which the spending starts over from zero; null for a  lifetime limit, which never resets. Filled for every limit, the limit for every user included, whose spending is  counted per user.", alias="periodEnd", json_schema_extra={"examples": ["2026-10-22T23:59:59.9999999Z"]})
    usage_from: Optional[datetime] = Field(default=None, description="The moment a lifetime limit counts from, in UTC; null for the other periods.", alias="usageFrom", json_schema_extra={"examples": ["2026-10-01T09:12:00Z"]})
    enabled: Optional[StrictBool] = Field(default=None, description="Whether the limit is in force. A switched-off limit no longer restricts the AI services and can be switched  back on.", json_schema_extra={"examples": [True]})
    created: Optional[datetime] = Field(default=None, description="The date and time when the limit was created, in UTC.", json_schema_extra={"examples": ["2026-09-01T10:30:00Z"]})
    modified: Optional[datetime] = Field(default=None, description="The date and time when the limit was last changed, in UTC.", json_schema_extra={"examples": ["2026-09-15T08:00:00Z"]})
    usage: Optional[ServiceLimitUsageDto] = Field(default=None, description="What was spent against the limit in its current period and what is left. Filled for the limit of the portal as  a whole and in the list of the users; null where the spending is not read, such as for a limit read by its ID  or the limit for every user, whose spending is counted per user.")
    __properties: ClassVar[List[str]] = ["id", "serviceGroupName", "customerAccountNumber", "scope", "userId", "amountValue", "currency", "quantityValue", "serviceUnit", "period", "periodEnd", "usageFrom", "enabled", "created", "modified", "usage"]

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
        """Create an instance of ServiceLimitDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of usage
        if self.usage:
            _dict['usage'] = self.usage.to_dict()
        # set to None if service_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.service_group_name is None and "service_group_name" in self.model_fields_set:
            _dict['serviceGroupName'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['userId'] = None

        # set to None if amount_value (nullable) is None
        # and model_fields_set contains the field
        if self.amount_value is None and "amount_value" in self.model_fields_set:
            _dict['amountValue'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if quantity_value (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_value is None and "quantity_value" in self.model_fields_set:
            _dict['quantityValue'] = None

        # set to None if service_unit (nullable) is None
        # and model_fields_set contains the field
        if self.service_unit is None and "service_unit" in self.model_fields_set:
            _dict['serviceUnit'] = None

        # set to None if period_end (nullable) is None
        # and model_fields_set contains the field
        if self.period_end is None and "period_end" in self.model_fields_set:
            _dict['periodEnd'] = None

        # set to None if usage_from (nullable) is None
        # and model_fields_set contains the field
        if self.usage_from is None and "usage_from" in self.model_fields_set:
            _dict['usageFrom'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceLimitDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "serviceGroupName": obj.get("serviceGroupName"),
            "customerAccountNumber": obj.get("customerAccountNumber"),
            "scope": obj.get("scope"),
            "userId": obj.get("userId"),
            "amountValue": obj.get("amountValue"),
            "currency": obj.get("currency"),
            "quantityValue": obj.get("quantityValue"),
            "serviceUnit": obj.get("serviceUnit"),
            "period": obj.get("period"),
            "periodEnd": obj.get("periodEnd"),
            "usageFrom": obj.get("usageFrom"),
            "enabled": obj.get("enabled"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "usage": ServiceLimitUsageDto.from_dict(obj["usage"]) if obj.get("usage") is not None else None
        })
        return _obj


