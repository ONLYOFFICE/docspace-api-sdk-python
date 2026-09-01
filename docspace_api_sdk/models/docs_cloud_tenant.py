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
from docspace_api_sdk.models.docs_cloud_payment import DocsCloudPayment
from typing import Optional, Set
from typing_extensions import Self

class DocsCloudTenant(BaseModel):
    """
    Represents a DocsCloud tenant of a portal.
    """ # noqa: E501
    dedicated_resource_ex_id: Optional[StrictInt] = Field(default=None, description="The external ID of the dedicated resource the tenant is hosted on.", alias="dedicatedResourceExId", json_schema_extra={"examples": [12345]})
    alias: Optional[StrictStr] = Field(default=None, description="The tenant alias.", json_schema_extra={"examples": ["my-portal"]})
    name: Optional[StrictStr] = Field(default=None, description="The tenant name.", json_schema_extra={"examples": ["My Portal"]})
    modified_date: Optional[datetime] = Field(default=None, description="The date and time when the tenant was last modified.", alias="modifiedDate", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    customer_id: Optional[StrictStr] = Field(default=None, description="The customer ID.", alias="customerId", json_schema_extra={"examples": ["CustomerId"]})
    customer_name: Optional[StrictStr] = Field(default=None, description="The customer name.", alias="customerName", json_schema_extra={"examples": ["CustomerName"]})
    end_date: Optional[datetime] = Field(default=None, description="The date and time when the tenant subscription ends.", alias="endDate", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    resource_type: Optional[StrictInt] = Field(default=None, description="The resource type.", alias="resourceType", json_schema_extra={"examples": [1]})
    is_active: Optional[StrictBool] = Field(default=None, description="Whether the tenant is active (the end date is in the future).", alias="isActive", json_schema_extra={"examples": [False]})
    address: Optional[StrictStr] = Field(default=None, description="The tenant address.", json_schema_extra={"examples": ["https://my-portal.onlyoffice.com"]})
    payment: Optional[DocsCloudPayment] = Field(default=None, description="The tenant payment information.")
    __properties: ClassVar[List[str]] = ["dedicatedResourceExId", "alias", "name", "modifiedDate", "customerId", "customerName", "endDate", "resourceType", "isActive", "address", "payment"]

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
        """Create an instance of DocsCloudTenant from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment
        if self.payment:
            _dict['payment'] = self.payment.to_dict()
        # set to None if alias (nullable) is None
        # and model_fields_set contains the field
        if self.alias is None and "alias" in self.model_fields_set:
            _dict['alias'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if customer_name (nullable) is None
        # and model_fields_set contains the field
        if self.customer_name is None and "customer_name" in self.model_fields_set:
            _dict['customerName'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocsCloudTenant from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dedicatedResourceExId": obj.get("dedicatedResourceExId"),
            "alias": obj.get("alias"),
            "name": obj.get("name"),
            "modifiedDate": obj.get("modifiedDate"),
            "customerId": obj.get("customerId"),
            "customerName": obj.get("customerName"),
            "endDate": obj.get("endDate"),
            "resourceType": obj.get("resourceType"),
            "isActive": obj.get("isActive"),
            "address": obj.get("address"),
            "payment": DocsCloudPayment.from_dict(obj["payment"]) if obj.get("payment") is not None else None
        })
        return _obj


