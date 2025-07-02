# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace-api-python.models.tenant_industry import TenantIndustry
from docspace-api-python.models.tenant_status import TenantStatus
from docspace-api-python.models.tenant_trusted_domains_type import TenantTrustedDomainsType
from typing import Optional, Set
from typing_extensions import Self

class TenantDto(BaseModel):
    """
    The tenant parameters.
    """ # noqa: E501
    affiliate_id: Optional[StrictStr] = Field(default=None, description="The affiliate ID.", alias="affiliateId")
    tenant_alias: Optional[StrictStr] = Field(default=None, description="The tenant alias.", alias="tenantAlias")
    calls: Optional[StrictBool] = Field(default=None, description="Specifies if the calls are available for this tenant or not.")
    campaign: Optional[StrictStr] = Field(default=None, description="The tenant campaign.")
    creation_date_time: Optional[datetime] = Field(default=None, description="The tenant creation date and time.", alias="creationDateTime")
    hosted_region: Optional[StrictStr] = Field(default=None, description="The hosted region.", alias="hostedRegion")
    tenant_id: Optional[StrictInt] = Field(default=None, description="The tenant ID.", alias="tenantId")
    industry: Optional[TenantIndustry] = None
    language: Optional[StrictStr] = Field(default=None, description="The tenant language.")
    last_modified: Optional[datetime] = Field(default=None, description="The date and time when the tenant was last modified.", alias="lastModified")
    mapped_domain: Optional[StrictStr] = Field(default=None, description="The tenant mapped domain.", alias="mappedDomain")
    name: Optional[StrictStr] = Field(default=None, description="The tenant name.")
    owner_id: Optional[StrictStr] = Field(default=None, description="The tenant owner ID.", alias="ownerId")
    payment_id: Optional[StrictStr] = Field(default=None, description="The tenant payment ID.", alias="paymentId")
    spam: Optional[StrictBool] = Field(default=None, description="Specifies if the ONLYOFFICE newsletter is allowed or not.")
    status: Optional[TenantStatus] = None
    status_change_date: Optional[datetime] = Field(default=None, description="The date and time when the tenant status was changed.", alias="statusChangeDate")
    time_zone: Optional[StrictStr] = Field(default=None, description="The tenant time zone.", alias="timeZone")
    trusted_domains: Optional[List[StrictStr]] = Field(default=None, description="The list of tenant trusted domains.", alias="trustedDomains")
    trusted_domains_raw: Optional[StrictStr] = Field(default=None, description="The tenant trusted domains in the string format.", alias="trustedDomainsRaw")
    trusted_domains_type: Optional[TenantTrustedDomainsType] = Field(default=None, alias="trustedDomainsType")
    version: Optional[StrictInt] = Field(default=None, description="The tenant version")
    version_changed: Optional[datetime] = Field(default=None, description="The date and time when the tenant version was changed.", alias="versionChanged")
    region: Optional[StrictStr] = Field(default=None, description="The tenant AWS region.")
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


