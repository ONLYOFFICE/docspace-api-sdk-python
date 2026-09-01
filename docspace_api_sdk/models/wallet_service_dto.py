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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.price_dto import PriceDto
from docspace_api_sdk.models.tenant_entity_quota_settings import TenantEntityQuotaSettings
from docspace_api_sdk.models.tenant_quota_feature_dto import TenantQuotaFeatureDto
from docspace_api_sdk.models.tenant_quota_settings import TenantQuotaSettings
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field
from docspace_api_sdk.models.quota_dto import QuotaDto

class WalletServiceDto(QuotaDto):
    """
    The wallet service information.
    """

    inner_services: Optional[List[WalletServiceDto]] = Field(default=None, description="The list of inner services.", alias="innerServices", json_schema_extra={"examples": [[{"title": "File Storage", "size": 1073741824}]]})
    service_name: Optional[StrictStr] = Field(default=None, description="The service name.", alias="serviceName", json_schema_extra={"examples": ["backup"]})

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
        """Create an instance of WalletServiceDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in inner_services (list)
        _items = []
        if self.inner_services:
            for _item_inner_services in self.inner_services:
                if _item_inner_services:
                    _items.append(_item_inner_services.to_dict())
            _dict['innerServices'] = _items
        # set to None if inner_services (nullable) is None
        # and model_fields_set contains the field
        if self.inner_services is None and "inner_services" in self.model_fields_set:
            _dict['innerServices'] = None

        # set to None if service_name (nullable) is None
        # and model_fields_set contains the field
        if self.service_name is None and "service_name" in self.model_fields_set:
            _dict['serviceName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance from a dict"""
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        base_obj = super().from_dict(obj)
        base_dict = base_obj.model_dump() if hasattr(base_obj, "model_dump") else dict(base_obj or {})

        extra_fields = {
            "innerServices": [WalletServiceDto.from_dict(_item) for _item in obj["innerServices"]] if obj.get("innerServices") is not None else None,
            "serviceName": obj.get("serviceName")
        }
        all_fields = {**base_dict, **extra_fields}
        return cls.model_validate(all_fields)


