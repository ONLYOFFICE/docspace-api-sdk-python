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
from docspace_api_sdk.models.api_date_time import ApiDateTime
from docspace_api_sdk.models.tariff_quota_dto import TariffQuotaDto
from docspace_api_sdk.models.tariff_state import TariffState
from typing import Optional, Set
from typing_extensions import Self

class TariffDto(BaseModel):
    """
    The subscription this portal runs on: its state, the end of the current period, and the quotas it is made of.
    """ # noqa: E501
    open_source: Optional[StrictBool] = Field(default=None, description="Whether the installation runs the open-source build, which has no paid plan at all. This flag and the two  below describe the build rather than the subscription, and all three are left empty for a caller without  the portal-settings right.", alias="openSource", json_schema_extra={"examples": [False]})
    enterprise: Optional[StrictBool] = Field(default=None, description="Whether the installation runs on an Enterprise licence file, which is what makes the licence operations  under `api/2.0/settings/license` usable.", json_schema_extra={"examples": [True]})
    developer: Optional[StrictBool] = Field(default=None, description="Whether the installation runs on a Developer licence, an Enterprise licence meant for embedding rather  than for production use.", json_schema_extra={"examples": [False]})
    id: Optional[StrictInt] = Field(default=None, description="The identifier of the subscription record itself, for quoting when a charge has to be traced. It is filled  in for a caller with the portal-settings right only, and nothing accepts it as an argument.", json_schema_extra={"examples": [1]})
    state: Optional[TariffState] = Field(default=None, description="How the subscription stands: on trial, paid, inside the grace period that follows the due date, or unpaid.  It is the one field every caller gets, whatever their role, so a client can warn about payment without  needing administrator rights.")
    due_date: Optional[ApiDateTime] = Field(default=None, description="When the current period ends, in the portal time zone. It is filled in for a room or DocSpace  administrator only, and set to the largest value a date can hold for a subscription that never ends.", alias="dueDate")
    delay_due_date: Optional[ApiDateTime] = Field(default=None, description="When the grace period after `dueDate` runs out and the portal is cut off, in the portal time zone. Filled  in under the same conditions as `dueDate`, and equal to it when the plan grants no grace period.", alias="delayDueDate")
    license_date: Optional[ApiDateTime] = Field(default=None, description="When the licence file behind the subscription was issued, in the portal time zone. It is meaningful on a  server installation and filled in for a caller with the portal-settings right only.", alias="licenseDate")
    customer_id: Optional[StrictStr] = Field(default=None, description="The account in the billing system the subscription is charged to, empty for a portal that has never been  billed. Filled in for a caller with the portal-settings right only.", alias="customerId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000001"]})
    quotas: Optional[List[TariffQuotaDto]] = Field(default=None, description="The quotas the subscription is made of - the plan itself and its add-ons - with the overdue ones listed  alongside the current ones, so an entry here is not proof that it is still being paid for; read each  entry's own `state` for that. Filled in for a caller with the portal-settings right only.", json_schema_extra={"examples": [[{"id": 1, "quantity": 500}]]})
    __properties: ClassVar[List[str]] = ["openSource", "enterprise", "developer", "id", "state", "dueDate", "delayDueDate", "licenseDate", "customerId", "quotas"]

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
        """Create an instance of TariffDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of delay_due_date
        if self.delay_due_date:
            _dict['delayDueDate'] = self.delay_due_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of license_date
        if self.license_date:
            _dict['licenseDate'] = self.license_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in quotas (list)
        _items = []
        if self.quotas:
            for _item_quotas in self.quotas:
                if _item_quotas:
                    _items.append(_item_quotas.to_dict())
            _dict['quotas'] = _items
        # set to None if open_source (nullable) is None
        # and model_fields_set contains the field
        if self.open_source is None and "open_source" in self.model_fields_set:
            _dict['openSource'] = None

        # set to None if enterprise (nullable) is None
        # and model_fields_set contains the field
        if self.enterprise is None and "enterprise" in self.model_fields_set:
            _dict['enterprise'] = None

        # set to None if developer (nullable) is None
        # and model_fields_set contains the field
        if self.developer is None and "developer" in self.model_fields_set:
            _dict['developer'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if quotas (nullable) is None
        # and model_fields_set contains the field
        if self.quotas is None and "quotas" in self.model_fields_set:
            _dict['quotas'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TariffDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "openSource": obj.get("openSource"),
            "enterprise": obj.get("enterprise"),
            "developer": obj.get("developer"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "dueDate": ApiDateTime.from_dict(obj["dueDate"]) if obj.get("dueDate") is not None else None,
            "delayDueDate": ApiDateTime.from_dict(obj["delayDueDate"]) if obj.get("delayDueDate") is not None else None,
            "licenseDate": ApiDateTime.from_dict(obj["licenseDate"]) if obj.get("licenseDate") is not None else None,
            "customerId": obj.get("customerId"),
            "quotas": [TariffQuotaDto.from_dict(_item) for _item in obj["quotas"]] if obj.get("quotas") is not None else None
        })
        return _obj


