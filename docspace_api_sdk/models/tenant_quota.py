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
from typing import Optional, Set
from typing_extensions import Self

class TenantQuota(BaseModel):
    """
    The current tenant quota.
    """ # noqa: E501
    tenant_id: Optional[StrictInt] = Field(default=None, description="The tenant ID.", alias="tenantId", json_schema_extra={"examples": [1]})
    name: Optional[StrictStr] = Field(default=None, description="The tenant name.", json_schema_extra={"examples": ["Default"]})
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The tenant price.", json_schema_extra={"examples": [10.0]})
    price_currency_symbol: Optional[StrictStr] = Field(default=None, description="The tenant price currency symbol.", alias="priceCurrencySymbol", json_schema_extra={"examples": ["$"]})
    price_iso_currency_symbol: Optional[StrictStr] = Field(default=None, description="The tenant price three-character ISO 4217 currency symbol.", alias="priceISOCurrencySymbol", json_schema_extra={"examples": ["USD"]})
    product_id: Optional[StrictStr] = Field(default=None, description="The tenant product ID.", alias="productId", json_schema_extra={"examples": ["64"]})
    service_name: Optional[StrictStr] = Field(default=None, description="The service name.", alias="serviceName", json_schema_extra={"examples": ["backup"]})
    service_group: Optional[StrictStr] = Field(default=None, description="The service group.", alias="serviceGroup", json_schema_extra={"examples": ["services"]})
    visible: Optional[StrictBool] = Field(default=None, description="Specifies if the tenant quota is visible or not.", json_schema_extra={"examples": [True]})
    wallet: Optional[StrictBool] = Field(default=None, description="Specifies if the tenant quota applies to the wallet or not", json_schema_extra={"examples": [True]})
    additional: Optional[StrictBool] = Field(default=None, description="Specifies if the tenant quota is primary or additional.", json_schema_extra={"examples": [False]})
    due_date: Optional[datetime] = Field(default=None, description="The quota due date.", alias="dueDate", json_schema_extra={"examples": ["2021-01-01T00:00:00"]})
    features: Optional[StrictStr] = Field(default=None, description="The tenant quota features.", json_schema_extra={"examples": ["audit,ldap,sso"]})
    max_file_size: Optional[StrictInt] = Field(default=None, description="The tenant maximum file size.", alias="maxFileSize", json_schema_extra={"examples": [25000000]})
    max_total_size: Optional[StrictInt] = Field(default=None, description="The tenant maximum total size.", alias="maxTotalSize", json_schema_extra={"examples": [25000000000]})
    count_user: Optional[StrictInt] = Field(default=None, description="The number of portal users.", alias="countUser", json_schema_extra={"examples": [100]})
    count_room_admin: Optional[StrictInt] = Field(default=None, description="The number of portal room administrators.", alias="countRoomAdmin", json_schema_extra={"examples": [10]})
    users_in_room: Optional[StrictInt] = Field(default=None, description="The number of room users.", alias="usersInRoom", json_schema_extra={"examples": [50]})
    count_room: Optional[StrictInt] = Field(default=None, description="The number of rooms.", alias="countRoom", json_schema_extra={"examples": [500]})
    non_profit: Optional[StrictBool] = Field(default=None, description="Specifies if the tenant quota is nonprofit or not.", alias="nonProfit", json_schema_extra={"examples": [False]})
    trial: Optional[StrictBool] = Field(default=None, description="Specifies if the tenant quota is trial or not.", json_schema_extra={"examples": [False]})
    free: Optional[StrictBool] = Field(default=None, description="Specifies if the tenant quota is free or not.", json_schema_extra={"examples": [False]})
    update: Optional[StrictBool] = Field(default=None, description="Specifies if the tenant quota is updated or not.", json_schema_extra={"examples": [False]})
    audit: Optional[StrictBool] = Field(default=None, description="Specifies if the audit trail is available or not.", json_schema_extra={"examples": [True]})
    docs_edition: Optional[StrictBool] = Field(default=None, description="Specifies if ONLYOFFICE Docs is included in the tenant quota or not.", alias="docsEdition", json_schema_extra={"examples": [True]})
    ldap: Optional[StrictBool] = Field(default=None, description="Specifies if the LDAP settings are available or not.", json_schema_extra={"examples": [True]})
    sso: Optional[StrictBool] = Field(default=None, description="Specifies if the SSO settings are available or not.", json_schema_extra={"examples": [True]})
    statistic: Optional[StrictBool] = Field(default=None, description="Specifies if the statistics settings are available or not.", json_schema_extra={"examples": [True]})
    branding: Optional[StrictBool] = Field(default=None, description="Specifies if the branding settings are available or not.", json_schema_extra={"examples": [True]})
    customization: Optional[StrictBool] = Field(default=None, description="Specifies if the customization settings are available or not.", json_schema_extra={"examples": [True]})
    lifetime: Optional[StrictBool] = Field(default=None, description="Specifies if the license has the lifetime settings or not.", json_schema_extra={"examples": [False]})
    automation_api: Optional[StrictBool] = Field(default=None, description="Specifies if the Automation API is available or not.", alias="automationApi", json_schema_extra={"examples": [True]})
    custom: Optional[StrictBool] = Field(default=None, description="Specifies if the custom domain URL is available or not.", json_schema_extra={"examples": [False]})
    restore: Optional[StrictBool] = Field(default=None, description="Specifies if the restore is enabled or not.", json_schema_extra={"examples": [True]})
    oauth: Optional[StrictBool] = Field(default=None, description="Specifies if Oauth is available or not.", json_schema_extra={"examples": [True]})
    content_search: Optional[StrictBool] = Field(default=None, description="Specifies if the content search is available or not.", alias="contentSearch", json_schema_extra={"examples": [True]})
    third_party: Optional[StrictBool] = Field(default=None, description="Specifies if the third-party accounts linking is available or not.", alias="thirdParty", json_schema_extra={"examples": [True]})
    year: Optional[StrictBool] = Field(default=None, description="Specifies if the tenant quota is yearly subscription or not.", json_schema_extra={"examples": [True]})
    count_free_backup: Optional[StrictInt] = Field(default=None, description="The number of free backups within a month.", alias="countFreeBackup", json_schema_extra={"examples": [1]})
    backup: Optional[StrictBool] = Field(default=None, description="Specifies if the backup enabled as a wallet service or not.", json_schema_extra={"examples": [True]})
    count_ai_agent: Optional[StrictInt] = Field(default=None, description="The number of AI agents.", alias="countAIAgent", json_schema_extra={"examples": [5]})
    ai_tools: Optional[StrictBool] = Field(default=None, description="Specifies if the AI tools enabled as a wallet service or not.", alias="aiTools", json_schema_extra={"examples": [True]})
    ai_search: Optional[StrictBool] = Field(default=None, description="Specifies if the AI search enabled as a wallet service or not.", alias="aiSearch", json_schema_extra={"examples": [True]})
    docs_cloud: Optional[StrictInt] = Field(default=None, description="The number of DocsCloud users.", alias="docsCloud", json_schema_extra={"examples": [True]})
    docs_cloud_dev_pack: Optional[StrictBool] = Field(default=None, description="Specifies if the DocsCloudDevPack enabled or not.", alias="docsCloudDevPack", json_schema_extra={"examples": [True]})
    docs_cloud_trial: Optional[StrictBool] = Field(default=None, description="Specifies if the DocsCloudTrial enabled or not.", alias="docsCloudTrial", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["tenantId", "name", "price", "priceCurrencySymbol", "priceISOCurrencySymbol", "productId", "serviceName", "serviceGroup", "visible", "wallet", "additional", "dueDate", "features", "maxFileSize", "maxTotalSize", "countUser", "countRoomAdmin", "usersInRoom", "countRoom", "nonProfit", "trial", "free", "update", "audit", "docsEdition", "ldap", "sso", "statistic", "branding", "customization", "lifetime", "automationApi", "custom", "restore", "oauth", "contentSearch", "thirdParty", "year", "countFreeBackup", "backup", "countAIAgent", "aiTools", "aiSearch", "docsCloud", "docsCloudDevPack", "docsCloudTrial"]

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
        """Create an instance of TenantQuota from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if price_currency_symbol (nullable) is None
        # and model_fields_set contains the field
        if self.price_currency_symbol is None and "price_currency_symbol" in self.model_fields_set:
            _dict['priceCurrencySymbol'] = None

        # set to None if price_iso_currency_symbol (nullable) is None
        # and model_fields_set contains the field
        if self.price_iso_currency_symbol is None and "price_iso_currency_symbol" in self.model_fields_set:
            _dict['priceISOCurrencySymbol'] = None

        # set to None if product_id (nullable) is None
        # and model_fields_set contains the field
        if self.product_id is None and "product_id" in self.model_fields_set:
            _dict['productId'] = None

        # set to None if service_name (nullable) is None
        # and model_fields_set contains the field
        if self.service_name is None and "service_name" in self.model_fields_set:
            _dict['serviceName'] = None

        # set to None if service_group (nullable) is None
        # and model_fields_set contains the field
        if self.service_group is None and "service_group" in self.model_fields_set:
            _dict['serviceGroup'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['dueDate'] = None

        # set to None if features (nullable) is None
        # and model_fields_set contains the field
        if self.features is None and "features" in self.model_fields_set:
            _dict['features'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantQuota from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "name": obj.get("name"),
            "price": obj.get("price"),
            "priceCurrencySymbol": obj.get("priceCurrencySymbol"),
            "priceISOCurrencySymbol": obj.get("priceISOCurrencySymbol"),
            "productId": obj.get("productId"),
            "serviceName": obj.get("serviceName"),
            "serviceGroup": obj.get("serviceGroup"),
            "visible": obj.get("visible"),
            "wallet": obj.get("wallet"),
            "additional": obj.get("additional"),
            "dueDate": obj.get("dueDate"),
            "features": obj.get("features"),
            "maxFileSize": obj.get("maxFileSize"),
            "maxTotalSize": obj.get("maxTotalSize"),
            "countUser": obj.get("countUser"),
            "countRoomAdmin": obj.get("countRoomAdmin"),
            "usersInRoom": obj.get("usersInRoom"),
            "countRoom": obj.get("countRoom"),
            "nonProfit": obj.get("nonProfit"),
            "trial": obj.get("trial"),
            "free": obj.get("free"),
            "update": obj.get("update"),
            "audit": obj.get("audit"),
            "docsEdition": obj.get("docsEdition"),
            "ldap": obj.get("ldap"),
            "sso": obj.get("sso"),
            "statistic": obj.get("statistic"),
            "branding": obj.get("branding"),
            "customization": obj.get("customization"),
            "lifetime": obj.get("lifetime"),
            "automationApi": obj.get("automationApi"),
            "custom": obj.get("custom"),
            "restore": obj.get("restore"),
            "oauth": obj.get("oauth"),
            "contentSearch": obj.get("contentSearch"),
            "thirdParty": obj.get("thirdParty"),
            "year": obj.get("year"),
            "countFreeBackup": obj.get("countFreeBackup"),
            "backup": obj.get("backup"),
            "countAIAgent": obj.get("countAIAgent"),
            "aiTools": obj.get("aiTools"),
            "aiSearch": obj.get("aiSearch"),
            "docsCloud": obj.get("docsCloud"),
            "docsCloudDevPack": obj.get("docsCloudDevPack"),
            "docsCloudTrial": obj.get("docsCloudTrial")
        })
        return _obj


