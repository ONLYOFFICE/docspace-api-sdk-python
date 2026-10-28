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
from docspace_api_sdk.models.employee_dto import EmployeeDto
from docspace_api_sdk.models.webhook_trigger import WebhookTrigger
from typing import Optional, Set
from typing_extensions import Self

class WebhooksConfigDto(BaseModel):
    """
    One webhook subscription of the portal: where deliveries go, which events they cover, and how they have fared.
    """ # noqa: E501
    id: StrictInt = Field(description="The identifier of the subscription, which is what `PUT api/2.0/settings/webhook`,  `DELETE api/2.0/settings/webhook/{id}` and the `configId` filter of the delivery log address it by.", json_schema_extra={"examples": [1]})
    name: Optional[StrictStr] = Field(default=None, description="The label the subscription was given, free text with no meaning to the portal.", json_schema_extra={"examples": ["Room activity"]})
    uri: Optional[StrictStr] = Field(default=None, description="The address every delivery is posted to. The signing secret that lets the receiver verify a delivery is  never part of this answer, so it has to be kept from the moment the subscription was created.", json_schema_extra={"examples": ["https://example.com/hooks/docspace"]})
    enabled: Optional[StrictBool] = Field(default=None, description="Whether the subscription is delivering. While it is `false` events are dropped rather than queued, so  nothing arrives late after it is switched back on.", json_schema_extra={"examples": [True]})
    ssl: Optional[StrictBool] = Field(default=None, description="Whether the certificate of `uri` is verified before a delivery. While it is `false` a self-signed  certificate is accepted as well.", json_schema_extra={"examples": [True]})
    triggers: Optional[WebhookTrigger] = Field(default=None, description="The events the subscription covers, as the bits of `GET api/2.0/settings/webhook/triggers` added  together. `0` is the catch-all and means every event, not none.")
    target_id: Optional[StrictStr] = Field(default=None, description="The single room or file the subscription is narrowed to, empty for a subscription that covers the whole  portal. It is kept as an opaque value, so both a numeric and a third-party identifier can appear.", alias="targetId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000001"]})
    created_by: Optional[EmployeeDto] = Field(default=None, description="The member who created the subscription, which is also who a non-administrator is limited to seeing. It is  empty for a subscription created by a portal background job.", alias="createdBy")
    created_on: Optional[datetime] = Field(default=None, description="When the subscription was created, in the portal time zone.", alias="createdOn", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    modified_by: Optional[EmployeeDto] = Field(default=None, description="The member who last changed the subscription, empty while nobody has changed it since it was created.", alias="modifiedBy")
    modified_on: Optional[datetime] = Field(default=None, description="When it was last changed, in the portal time zone, and empty under the same condition as `modifiedBy`.", alias="modifiedOn", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    last_failure_on: Optional[datetime] = Field(default=None, description="When a delivery last failed, in the portal time zone. It is empty for a subscription that has never  failed, and it is not cleared by a later success - compare it with `lastSuccessOn` to see which came last.", alias="lastFailureOn", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    last_failure_content: Optional[StrictStr] = Field(default=None, description="What the target answered on that failure, truncated, for diagnosing without opening the delivery log. It  is empty when the failure produced no body at all, a timeout for instance.", alias="lastFailureContent", json_schema_extra={"examples": ["502 Bad Gateway"]})
    last_success_on: Optional[datetime] = Field(default=None, description="When a delivery last succeeded, in the portal time zone, empty for a subscription that has never  delivered. Both this and `lastFailureOn` being empty means nothing has been attempted yet.", alias="lastSuccessOn", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    __properties: ClassVar[List[str]] = ["id", "name", "uri", "enabled", "ssl", "triggers", "targetId", "createdBy", "createdOn", "modifiedBy", "modifiedOn", "lastFailureOn", "lastFailureContent", "lastSuccessOn"]

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
        """Create an instance of WebhooksConfigDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_by
        if self.modified_by:
            _dict['modifiedBy'] = self.modified_by.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if uri (nullable) is None
        # and model_fields_set contains the field
        if self.uri is None and "uri" in self.model_fields_set:
            _dict['uri'] = None

        # set to None if target_id (nullable) is None
        # and model_fields_set contains the field
        if self.target_id is None and "target_id" in self.model_fields_set:
            _dict['targetId'] = None

        # set to None if created_on (nullable) is None
        # and model_fields_set contains the field
        if self.created_on is None and "created_on" in self.model_fields_set:
            _dict['createdOn'] = None

        # set to None if modified_on (nullable) is None
        # and model_fields_set contains the field
        if self.modified_on is None and "modified_on" in self.model_fields_set:
            _dict['modifiedOn'] = None

        # set to None if last_failure_on (nullable) is None
        # and model_fields_set contains the field
        if self.last_failure_on is None and "last_failure_on" in self.model_fields_set:
            _dict['lastFailureOn'] = None

        # set to None if last_failure_content (nullable) is None
        # and model_fields_set contains the field
        if self.last_failure_content is None and "last_failure_content" in self.model_fields_set:
            _dict['lastFailureContent'] = None

        # set to None if last_success_on (nullable) is None
        # and model_fields_set contains the field
        if self.last_success_on is None and "last_success_on" in self.model_fields_set:
            _dict['lastSuccessOn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhooksConfigDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "uri": obj.get("uri"),
            "enabled": obj.get("enabled"),
            "ssl": obj.get("ssl"),
            "triggers": obj.get("triggers"),
            "targetId": obj.get("targetId"),
            "createdBy": EmployeeDto.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "createdOn": obj.get("createdOn"),
            "modifiedBy": EmployeeDto.from_dict(obj["modifiedBy"]) if obj.get("modifiedBy") is not None else None,
            "modifiedOn": obj.get("modifiedOn"),
            "lastFailureOn": obj.get("lastFailureOn"),
            "lastFailureContent": obj.get("lastFailureContent"),
            "lastSuccessOn": obj.get("lastSuccessOn")
        })
        return _obj


