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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.webhook_trigger import WebhookTrigger
from typing import Optional, Set
from typing_extensions import Self

class WebhooksLogDto(BaseModel):
    """
    One delivery attempt of a webhook: what was sent where, and what came back.
    """ # noqa: E501
    id: StrictInt = Field(description="The identifier of this attempt, which is what the `eventId` filter of  `GET api/2.0/settings/webhooks/log` picks one record by and what  `PUT api/2.0/settings/webhook/{id}/retry` re-sends. A retry produces a new record with a new identifier  and leaves this one as it is.", json_schema_extra={"examples": [1]})
    config_name: Optional[StrictStr] = Field(default=None, description="The name of the subscription the attempt belongs to. It is the name as it stands now, so it follows a  later rename of the subscription rather than recording what it was called at the time.", alias="configName", json_schema_extra={"examples": ["Room activity"]})
    trigger: Optional[WebhookTrigger] = Field(default=None, description="The event that caused the attempt, as a single bit rather than a mask - a delivery is always for one  event, even though a subscription covers several.")
    creation_time: Optional[datetime] = Field(default=None, description="When the attempt was queued, as a UTC instant - unlike the dates of the subscription itself, which come  in the portal time zone. Records come back newest first by this moment.", alias="creationTime", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    method: Optional[StrictStr] = Field(default=None, description="The HTTP method the delivery was sent with, which is `POST` for every webhook the portal sends.", json_schema_extra={"examples": ["POST"]})
    route: Optional[StrictStr] = Field(default=None, description="The address the delivery was sent to, which is the subscription's URL as it stood at the time - so an  older record can name an address the subscription no longer uses.", json_schema_extra={"examples": ["https://example.com/hooks/docspace"]})
    request_headers: Optional[StrictStr] = Field(default=None, description="The headers the portal sent, serialised as one string, including the signature header a receiver verifies  the payload with.", alias="requestHeaders", json_schema_extra={"examples": ["{\"x-docspace-signature\":\"9f86d081884c7d65\"}"]})
    request_payload: Optional[StrictStr] = Field(default=None, description="The body the portal sent, which is the event payload as JSON text. It is stored as it was sent, so it  still describes the entity as it looked at the time of the event.", alias="requestPayload", json_schema_extra={"examples": ["{\"id\":42,\"title\":\"report.docx\"}"]})
    response_headers: Optional[StrictStr] = Field(default=None, description="The headers the target answered with, serialised the same way as `requestHeaders`. It is empty while the  attempt is still on its way and on an attempt that never reached the target.", alias="responseHeaders", json_schema_extra={"examples": ["{\"content-type\":\"application/json\"}"]})
    response_payload: Optional[StrictStr] = Field(default=None, description="The body the target answered with, truncated for storage. Empty under the same conditions as  `responseHeaders`, and also for a target that answers with no body at all.", alias="responsePayload", json_schema_extra={"examples": ["{\"ok\":true}"]})
    status: Optional[StrictInt] = Field(default=None, description="The HTTP status code the target answered. It is `0` while the attempt is still on its way and on one that  never reached the target, so `0` is not a failure code - it is the absence of an answer.", json_schema_extra={"examples": [200]})
    delivery: Optional[datetime] = Field(default=None, description="When the answer came back, as a UTC instant like `creationTime`. It is empty while the attempt is still on  its way, which together with `status` is how a pending record is told from a finished one.", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    __properties: ClassVar[List[str]] = ["id", "configName", "trigger", "creationTime", "method", "route", "requestHeaders", "requestPayload", "responseHeaders", "responsePayload", "status", "delivery"]

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
        """Create an instance of WebhooksLogDto from a JSON string"""
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
        # set to None if config_name (nullable) is None
        # and model_fields_set contains the field
        if self.config_name is None and "config_name" in self.model_fields_set:
            _dict['configName'] = None

        # set to None if method (nullable) is None
        # and model_fields_set contains the field
        if self.method is None and "method" in self.model_fields_set:
            _dict['method'] = None

        # set to None if route (nullable) is None
        # and model_fields_set contains the field
        if self.route is None and "route" in self.model_fields_set:
            _dict['route'] = None

        # set to None if request_headers (nullable) is None
        # and model_fields_set contains the field
        if self.request_headers is None and "request_headers" in self.model_fields_set:
            _dict['requestHeaders'] = None

        # set to None if request_payload (nullable) is None
        # and model_fields_set contains the field
        if self.request_payload is None and "request_payload" in self.model_fields_set:
            _dict['requestPayload'] = None

        # set to None if response_headers (nullable) is None
        # and model_fields_set contains the field
        if self.response_headers is None and "response_headers" in self.model_fields_set:
            _dict['responseHeaders'] = None

        # set to None if response_payload (nullable) is None
        # and model_fields_set contains the field
        if self.response_payload is None and "response_payload" in self.model_fields_set:
            _dict['responsePayload'] = None

        # set to None if delivery (nullable) is None
        # and model_fields_set contains the field
        if self.delivery is None and "delivery" in self.model_fields_set:
            _dict['delivery'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhooksLogDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "configName": obj.get("configName"),
            "trigger": obj.get("trigger"),
            "creationTime": obj.get("creationTime"),
            "method": obj.get("method"),
            "route": obj.get("route"),
            "requestHeaders": obj.get("requestHeaders"),
            "requestPayload": obj.get("requestPayload"),
            "responseHeaders": obj.get("responseHeaders"),
            "responsePayload": obj.get("responsePayload"),
            "status": obj.get("status"),
            "delivery": obj.get("delivery")
        })
        return _obj


