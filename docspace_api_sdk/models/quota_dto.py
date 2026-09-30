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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.price_dto import PriceDto
from docspace_api_sdk.models.tenant_entity_quota_settings import TenantEntityQuotaSettings
from docspace_api_sdk.models.tenant_quota_feature_dto import TenantQuotaFeatureDto
from docspace_api_sdk.models.tenant_quota_settings import TenantQuotaSettings
from typing import Optional, Set
from typing_extensions import Self

class QuotaDto(BaseModel):
    """
    A quota - a plan, an add-on or a wallet service - with its price, the features it switches on and their limits.
    """ # noqa: E501
    id: StrictInt = Field(description="The identifier of the quota, which is what the tariff reports as a quota `id` and what a purchase names.  A negative value belongs to a built-in quota rather than one on the price list.", json_schema_extra={"examples": [1]})
    title: Optional[StrictStr] = Field(default=None, description="The quota name in the portal language, for printing rather than matching. It is empty when this build  ships no wording for the quota, which is normal for a quota that is not on the public price list.", json_schema_extra={"examples": ["Basic Plan"]})
    price: PriceDto = Field(description="What the quota costs, in the currency resolved for the request. Its `value` is empty for a quota that is  not sold for money, which is what `free`, `trial` and `nonProfit` describe.")
    non_profit: StrictBool = Field(description="Whether this is the non-profit quota, which is granted rather than bought. A portal on it cannot buy any  other plan, so a catalogue asked for plans returns this one alone.", alias="nonProfit", json_schema_extra={"examples": [False]})
    free: StrictBool = Field(description="Whether this is the free quota a portal falls back to when nothing is paid for. It has no end date and  the tightest limits of any quota.", json_schema_extra={"examples": [True]})
    trial: StrictBool = Field(description="Whether this is the trial quota, which grants the paid limits for a while and then expires. A trial is not  extended by paying - a plan has to be bought instead.", json_schema_extra={"examples": [False]})
    features: Optional[List[TenantQuotaFeatureDto]] = Field(description="The features the quota switches on, each with the limit it grants and, on the quota the portal is  actually on, how much of that limit is already used. A feature that is absent is off, so the list is the  whole truth about what the quota includes.", json_schema_extra={"examples": [[{"id": "00000000-0000-0000-0000-000000000001", "title": "Premium Storage"}]]})
    users_quota: Optional[TenantEntityQuotaSettings] = Field(default=None, description="The per-member storage allowance an administrator has set on top of the quota, and whether it is applied  at all. It describes the live portal rather than this quota, so every entry of a catalogue listing repeats  the same values, and it is empty unless the portal is a server installation or its plan includes  statistics.", alias="usersQuota")
    rooms_quota: Optional[TenantEntityQuotaSettings] = Field(default=None, description="The same kind of per-room storage override, filled in and read the same way as `usersQuota`.", alias="roomsQuota")
    ai_agents_quota: Optional[TenantEntityQuotaSettings] = Field(default=None, description="The same kind of per-agent storage override for AI agents, filled in and read the same way as  `usersQuota`.", alias="aiAgentsQuota")
    tenant_custom_quota: Optional[TenantQuotaSettings] = Field(default=None, description="The storage allowance an administrator has set for the portal as a whole, which caps it below what the  quota grants. Filled in under the same conditions as `usersQuota`.", alias="tenantCustomQuota")
    due_date: Optional[datetime] = Field(default=None, description="When the quota runs out, in UTC. It is empty on a quota from the catalogue, which has no date until it is  bought, and on a quota that never expires.", alias="dueDate", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    __properties: ClassVar[List[str]] = ["id", "title", "price", "nonProfit", "free", "trial", "features", "usersQuota", "roomsQuota", "aiAgentsQuota", "tenantCustomQuota", "dueDate"]

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
        """Create an instance of QuotaDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item_features in self.features:
                if _item_features:
                    _items.append(_item_features.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of users_quota
        if self.users_quota:
            _dict['usersQuota'] = self.users_quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rooms_quota
        if self.rooms_quota:
            _dict['roomsQuota'] = self.rooms_quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ai_agents_quota
        if self.ai_agents_quota:
            _dict['aiAgentsQuota'] = self.ai_agents_quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tenant_custom_quota
        if self.tenant_custom_quota:
            _dict['tenantCustomQuota'] = self.tenant_custom_quota.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if features (nullable) is None
        # and model_fields_set contains the field
        if self.features is None and "features" in self.model_fields_set:
            _dict['features'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['dueDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuotaDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "price": PriceDto.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "nonProfit": obj.get("nonProfit"),
            "free": obj.get("free"),
            "trial": obj.get("trial"),
            "features": [TenantQuotaFeatureDto.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "usersQuota": TenantEntityQuotaSettings.from_dict(obj["usersQuota"]) if obj.get("usersQuota") is not None else None,
            "roomsQuota": TenantEntityQuotaSettings.from_dict(obj["roomsQuota"]) if obj.get("roomsQuota") is not None else None,
            "aiAgentsQuota": TenantEntityQuotaSettings.from_dict(obj["aiAgentsQuota"]) if obj.get("aiAgentsQuota") is not None else None,
            "tenantCustomQuota": TenantQuotaSettings.from_dict(obj["tenantCustomQuota"]) if obj.get("tenantCustomQuota") is not None else None,
            "dueDate": obj.get("dueDate")
        })
        return _obj


