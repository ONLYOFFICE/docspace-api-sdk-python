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
from uuid import UUID
from docspace_api_sdk.models.tenant_industry import TenantIndustry
from docspace_api_sdk.models.tenant_status import TenantStatus
from docspace_api_sdk.models.tenant_trusted_domains_type import TenantTrustedDomainsType
from typing import Optional, Set
from typing_extensions import Self

class TenantDto(BaseModel):
    """
    The record of one portal: its name, owner, language, time zone and lifecycle state.
    """ # noqa: E501
    affiliate_id: Optional[StrictStr] = Field(default=None, description="The partner the portal was signed up through, empty for a portal that came in directly. It is bookkeeping  for the vendor and has no bearing on what the portal may do.", alias="affiliateId", json_schema_extra={"examples": ["AFF12345"]})
    tenant_alias: Optional[StrictStr] = Field(default=None, description="The portal's own name within the installation, which together with the installation's base domain forms  the address it is reached at. A caller without the portal-settings right gets `tenantId` alone, so an  empty value here is the sign that the rest of this object was withheld rather than unset.", alias="tenantAlias", json_schema_extra={"examples": ["my-company"]})
    calls: Optional[StrictBool] = Field(default=None, description="Whether telephony is switched on for the portal. It is carried over from portal registration and stays  `false` on a DocSpace portal, where the feature does not exist.", json_schema_extra={"examples": [True]})
    campaign: Optional[StrictStr] = Field(default=None, description="The marketing campaign the portal was signed up under, empty for a portal that came in outside one. Like  `affiliateId`, it is bookkeeping only.", json_schema_extra={"examples": ["WINTER2024"]})
    creation_date_time: Optional[datetime] = Field(default=None, description="When the portal was created, in UTC rather than in the portal time zone.", alias="creationDateTime", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    hosted_region: Optional[StrictStr] = Field(default=None, description="The data-centre region written on the portal record itself, as opposed to `region`, which is looked up  from the hosting service. It is empty on a server installation.", alias="hostedRegion", json_schema_extra={"examples": ["EU"]})
    tenant_id: Optional[StrictInt] = Field(default=None, description="The numeric identifier of the portal inside the installation. It is the one field every caller gets,  whatever their rights.", alias="tenantId", json_schema_extra={"examples": [1]})
    industry: Optional[TenantIndustry] = Field(default=None, description="The line of business chosen when the portal was created. It only steers what the vendor suggests and  restricts nothing.")
    language: Optional[StrictStr] = Field(default=None, description="The default language of the portal as a culture name, the same value `GET api/2.0/settings` reports as  `culture`. A member may have a language of their own, which this does not reflect.", json_schema_extra={"examples": ["en-US"]})
    last_modified: Optional[datetime] = Field(default=None, description="When any field of this record last changed, in UTC. It does not move when portal settings outside this  record are changed.", alias="lastModified", json_schema_extra={"examples": ["2024-02-10T14:20:00Z"]})
    mapped_domain: Optional[StrictStr] = Field(default=None, description="The custom domain the portal answers on in addition to its own address, empty when none has been set up.", alias="mappedDomain", json_schema_extra={"examples": ["mycompany.example.com"]})
    name: Optional[StrictStr] = Field(default=None, description="The portal title as shown to people, which is what `GET api/2.0/settings` returns as  `greetingSettings`. It is free text, unlike `tenantAlias`, and empty until someone sets it.", json_schema_extra={"examples": ["My Company"]})
    owner_id: Optional[UUID] = Field(default=None, description="The portal owner, the one account that cannot be removed or demoted.  `PUT api/2.0/settings/owner` hands the role over.", alias="ownerId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000001"]})
    payment_id: Optional[StrictStr] = Field(default=None, description="The portal's identifier in the billing system, empty for a portal that has never been billed. The  subscription itself is read with `GET api/2.0/portal/tariff`.", alias="paymentId", json_schema_extra={"examples": ["PAY123456789"]})
    spam: Optional[StrictBool] = Field(default=None, description="Whether the owner agreed to receive the vendor's newsletter. Despite the name it does not mark the portal  as a spammer and affects nothing but marketing mail.", json_schema_extra={"examples": [False]})
    status: Optional[TenantStatus] = Field(default=None, description="The lifecycle state of the portal. Anything other than active means most operations are refused for the  moment, because the portal is being transferred, restored, encrypted or removed.")
    status_change_date: Optional[datetime] = Field(default=None, description="When `status` last changed, in UTC. For a portal pending removal it is the moment the countdown to  deletion started.", alias="statusChangeDate", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    time_zone: Optional[StrictStr] = Field(default=None, description="The portal time zone, which is the zone the dates this API calls portal time are expressed in. It may be  stored as a Windows identifier here, while `GET api/2.0/settings` always reports the IANA form.", alias="timeZone", json_schema_extra={"examples": ["America/New_York"]})
    trusted_domains: Optional[List[StrictStr]] = Field(default=None, description="The mail domains a new member may register or be invited from without confirming the address. It is empty  whenever `trustedDomainsType` is not `Custom`.", alias="trustedDomains", json_schema_extra={"examples": [["example.com", "trusted.com"]]})
    trusted_domains_raw: Optional[StrictStr] = Field(default=None, description="The same domains as the single stored string they are kept in, separated by commas. Read  `trustedDomains` instead; this one exists because it is what the record holds.", alias="trustedDomainsRaw", json_schema_extra={"examples": ["example.com,trusted.com"]})
    trusted_domains_type: Optional[TenantTrustedDomainsType] = Field(default=None, description="How the mail domains are applied: no domain trusted, every domain trusted, or only the listed ones. Only  the last of the three makes `trustedDomains` meaningful.", alias="trustedDomainsType")
    version: Optional[StrictInt] = Field(default=None, description="The identifier of the portal version the installation pins this portal to, which is an internal number  and not the product version string that `GET api/2.0/settings` reports as `version`.", json_schema_extra={"examples": [2]})
    version_changed: Optional[datetime] = Field(default=None, description="When `version` last changed, in UTC. It stays at its zero value on a portal whose version has never been  switched.", alias="versionChanged", json_schema_extra={"examples": ["2024-02-01T09:00:00Z"]})
    region: Optional[StrictStr] = Field(default=None, description="The data-centre region the portal is actually served from, looked up from the hosting service. It is  empty on a server installation and also whenever the installation's portal cache is switched off, so an  empty value does not mean the portal has no region - `hostedRegion` is the value from the record itself.", json_schema_extra={"examples": ["us-east-1"]})
    __properties: ClassVar[List[str]] = ["affiliateId", "tenantAlias", "calls", "campaign", "creationDateTime", "hostedRegion", "tenantId", "industry", "language", "lastModified", "mappedDomain", "name", "ownerId", "paymentId", "spam", "status", "statusChangeDate", "timeZone", "trustedDomains", "trustedDomainsRaw", "trustedDomainsType", "version", "versionChanged", "region"]

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
        """Create an instance of TenantDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "creation_date_time",
            "tenant_id",
            "status_change_date",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if affiliate_id (nullable) is None
        # and model_fields_set contains the field
        if self.affiliate_id is None and "affiliate_id" in self.model_fields_set:
            _dict['affiliateId'] = None

        # set to None if tenant_alias (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_alias is None and "tenant_alias" in self.model_fields_set:
            _dict['tenantAlias'] = None

        # set to None if campaign (nullable) is None
        # and model_fields_set contains the field
        if self.campaign is None and "campaign" in self.model_fields_set:
            _dict['campaign'] = None

        # set to None if hosted_region (nullable) is None
        # and model_fields_set contains the field
        if self.hosted_region is None and "hosted_region" in self.model_fields_set:
            _dict['hostedRegion'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if mapped_domain (nullable) is None
        # and model_fields_set contains the field
        if self.mapped_domain is None and "mapped_domain" in self.model_fields_set:
            _dict['mappedDomain'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if payment_id (nullable) is None
        # and model_fields_set contains the field
        if self.payment_id is None and "payment_id" in self.model_fields_set:
            _dict['paymentId'] = None

        # set to None if time_zone (nullable) is None
        # and model_fields_set contains the field
        if self.time_zone is None and "time_zone" in self.model_fields_set:
            _dict['timeZone'] = None

        # set to None if trusted_domains (nullable) is None
        # and model_fields_set contains the field
        if self.trusted_domains is None and "trusted_domains" in self.model_fields_set:
            _dict['trustedDomains'] = None

        # set to None if trusted_domains_raw (nullable) is None
        # and model_fields_set contains the field
        if self.trusted_domains_raw is None and "trusted_domains_raw" in self.model_fields_set:
            _dict['trustedDomainsRaw'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "affiliateId": obj.get("affiliateId"),
            "tenantAlias": obj.get("tenantAlias"),
            "calls": obj.get("calls"),
            "campaign": obj.get("campaign"),
            "creationDateTime": obj.get("creationDateTime"),
            "hostedRegion": obj.get("hostedRegion"),
            "tenantId": obj.get("tenantId"),
            "industry": obj.get("industry"),
            "language": obj.get("language"),
            "lastModified": obj.get("lastModified"),
            "mappedDomain": obj.get("mappedDomain"),
            "name": obj.get("name"),
            "ownerId": obj.get("ownerId"),
            "paymentId": obj.get("paymentId"),
            "spam": obj.get("spam"),
            "status": obj.get("status"),
            "statusChangeDate": obj.get("statusChangeDate"),
            "timeZone": obj.get("timeZone"),
            "trustedDomains": obj.get("trustedDomains"),
            "trustedDomainsRaw": obj.get("trustedDomainsRaw"),
            "trustedDomainsType": obj.get("trustedDomainsType"),
            "version": obj.get("version"),
            "versionChanged": obj.get("versionChanged"),
            "region": obj.get("region")
        })
        return _obj


