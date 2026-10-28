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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.quota_state import QuotaState
from typing import Optional, Set
from typing_extensions import Self

class TariffQuotaDto(BaseModel):
    """
    One quota the subscription is made of - the plan itself or an add-on - with its quantity and its own deadline.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The quota this entry stands for. `GET api/2.0/portal/payment/quotas` describes the quota behind the ID,  including what its `quantity` counts; a negative ID belongs to a built-in quota rather than a purchased  one.", json_schema_extra={"examples": [-11]})
    quantity: Optional[StrictInt] = Field(default=None, description="How much of the quota the portal holds, in whatever the quota itself is measured in - seats for a plan,  gigabytes for storage. It is `1` for a quota that is simply on or off.", json_schema_extra={"examples": [500]})
    wallet: Optional[StrictBool] = Field(default=None, description="Whether the quota is paid for out of the portal wallet as it is consumed, rather than being part of the  subscription charged per period.", json_schema_extra={"examples": [True]})
    additional: Optional[StrictBool] = Field(default=None, description="Whether this is an add-on bought on top of the plan rather than the plan itself. Exactly one entry of  `quotas` is the plan, and the rest are add-ons.", json_schema_extra={"examples": [True]})
    due_date: Optional[ApiDateTime] = Field(default=None, description="When this quota runs out, in the portal time zone. An add-on can end earlier or later than the  subscription; a quota with no deadline of its own reports the subscription's `dueDate` instead of an empty  value.", alias="dueDate")
    next_quantity: Optional[StrictInt] = Field(default=None, description="The quantity the next period is going to be charged for, when a change has been scheduled. It is empty  while `quantity` simply carries over.", alias="nextQuantity", json_schema_extra={"examples": [100]})
    next_quota: Optional[StrictInt] = Field(default=None, description="The quota this one is scheduled to be replaced by at the start of the next period, empty when no such  switch is planned. `GET api/2.0/portal/tariff/upcoming` already reports the charge for the replacement.", alias="nextQuota", json_schema_extra={"examples": [2]})
    state: Optional[QuotaState] = Field(default=None, description="Whether the quota is still running or its deadline has passed. It is empty for a quota that has no  deadline of its own, which means it lasts as long as the subscription does.")
    __properties: ClassVar[List[str]] = ["id", "quantity", "wallet", "additional", "dueDate", "nextQuantity", "nextQuota", "state"]

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
        """Create an instance of TariffQuotaDto from a JSON string"""
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
        # set to None if next_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.next_quantity is None and "next_quantity" in self.model_fields_set:
            _dict['nextQuantity'] = None

        # set to None if next_quota (nullable) is None
        # and model_fields_set contains the field
        if self.next_quota is None and "next_quota" in self.model_fields_set:
            _dict['nextQuota'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TariffQuotaDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "quantity": obj.get("quantity"),
            "wallet": obj.get("wallet"),
            "additional": obj.get("additional"),
            "dueDate": ApiDateTime.from_dict(obj["dueDate"]) if obj.get("dueDate") is not None else None,
            "nextQuantity": obj.get("nextQuantity"),
            "nextQuota": obj.get("nextQuota"),
            "state": obj.get("state")
        })
        return _obj


