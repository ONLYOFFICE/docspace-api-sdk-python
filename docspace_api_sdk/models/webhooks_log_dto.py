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
from docspace_api_sdk.models.employee_dto import EmployeeDto
from docspace_api_sdk.models.webhook_trigger import WebhookTrigger
from typing import Optional, Set
from typing_extensions import Self

class WebhooksLogDto(BaseModel):
    """
    One delivery of a webhook event, updated in place by its automatic retries: what was sent where, and what came  back the last time. A manual retry is a delivery record of its own for the same event.
    """ # noqa: E501
    id: StrictInt = Field(description="The identifier of this delivery record, which is what `PUT api/2.0/settings/webhook/{id}/retry` re-sends.  The automatic retries of the delivery update this same record, while a manual retry gets a record and an  identifier of its own.", json_schema_extra={"examples": [1]})
    event_id: Optional[StrictInt] = Field(default=None, description="The identifier of the event the delivery is for, which the receiver sees as `event.id` and in the  `x-docspace-event-id` header. It is the `id` of the event's first delivery record, so it equals `id` there and  stays the same on every manual retry, which makes it the value to group the records of one event by.", alias="eventId", json_schema_extra={"examples": [1]})
    retried_by: Optional[EmployeeDto] = Field(default=None, description="The member who asked for this delivery with a manual retry. It is empty on the first delivery of an event,  which the portal sends by itself.", alias="retriedBy")
    config_name: Optional[StrictStr] = Field(default=None, description="The name of the subscription the delivery belongs to. It is the name as it stands now, so it follows a  later rename of the subscription rather than recording what it was called at the time.", alias="configName", json_schema_extra={"examples": ["Room activity"]})
    trigger: Optional[WebhookTrigger] = Field(default=None, description="The event that caused the delivery, as a single bit rather than a mask - a delivery is always for one  event, even though a subscription covers several.")
    creation_time: Optional[datetime] = Field(default=None, description="When this delivery record was queued, as a UTC instant ending in `Z`. For the first delivery that is when the  event happened; for a manual retry it is the  moment of the retry. Records come back newest first by this moment.", alias="creationTime", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    method: Optional[StrictStr] = Field(default=None, description="The HTTP method the delivery was sent with, which is `POST` for every webhook the portal sends.", json_schema_extra={"examples": ["POST"]})
    route: Optional[StrictStr] = Field(default=None, description="The address the delivery is sent to: the subscription's URL as it stands now. The journal does not keep the  address of each attempt, so after the subscription's URL changes, an older record names the new one too.", json_schema_extra={"examples": ["https://example.com/hooks/docspace"]})
    request_headers: Optional[StrictStr] = Field(default=None, description="The headers the portal sent, serialised as one string, including the signature header a receiver verifies  the payload with.", alias="requestHeaders", json_schema_extra={"examples": ["{\"Accept\":[\"*/*\"],\"x-docspace-event-id\":[\"1\"],\"x-docspace-event-timestamp\":[\"2024-01-15T10:30:00Z\"],\"x-docspace-signature-256\":[\"sha256=9F86D081884C7D659A2FEAA0C55AD015A3BF4F1B2B0B822CD15D6C15B0F00A08\"]}"]})
    request_payload: Optional[StrictStr] = Field(default=None, description="The body the portal sent, which is the event payload as JSON text. It is stored as it was sent, so it  still describes the entity as it looked at the time of the event.", alias="requestPayload", json_schema_extra={"examples": ["{\"event\":{\"id\":1,\"createOn\":\"2024-01-15T10:30:00Z\",\"trigger\":\"file.created\",\"triggerId\":128},\"payload\":{\"id\":42,\"title\":\"Report.docx\"},\"webhook\":{\"id\":7,\"name\":\"Room activity\"}}"]})
    response_headers: Optional[StrictStr] = Field(default=None, description="The headers the target answered with on the latest attempt, serialised the same way as `requestHeaders`. It  is empty until an attempt is answered, and when the target was not reached.", alias="responseHeaders", json_schema_extra={"examples": ["{\"content-type\":\"application/json\"}"]})
    response_payload: Optional[StrictStr] = Field(default=None, description="The body the target answered with on the latest attempt, truncated for storage. Empty under the same  conditions as `responseHeaders`, and also for a target that answers with no body at all. A record the portal  stopped without sending holds the portal's own note here instead - a text that starts with `Not sent:` and  gives the reason - which is not an answer of the target: on a record that never went out `status` is then `0`  and `responseHeaders` is empty, while on one stopped after failed attempts they still describe the last of them.", alias="responsePayload", json_schema_extra={"examples": ["{\"ok\":true}"]})
    status: Optional[StrictInt] = Field(default=None, description="The HTTP status code the target answered on the latest attempt. It is `0` while the first attempt is still  on its way and on one that never reached the target, so `0` is not a failure code - it is the absence of an  answer. While `nextAttemptOn` is set it is the status of the failed attempt that caused the retry.", json_schema_extra={"examples": [200]})
    delivery: Optional[datetime] = Field(default=None, description="When the successful answer came back, as a UTC instant ending in `Z` like `creationTime`. It stays empty until an  attempt succeeds, and for good once the portal has given up retrying.", json_schema_extra={"examples": ["2024-01-15T10:30:00Z"]})
    attempts: Optional[StrictInt] = Field(default=None, description="How many times the portal has tried to deliver this record so far. A failed attempt is retried with  growing pauses - on the default schedule about 1 minute, 5 minutes, 30 minutes, 2, 5 and 10 hours, though  an installation may configure its own - all of them under the same record and the same  `x-docspace-event-id` header, so a receiver can drop a delivery it has already processed. The one exception  is a portal moved to another region while retries are pending: the moved records get new IDs, so the attempts  made there carry a new `x-docspace-event-id`.", json_schema_extra={"examples": [1]})
    next_attempt_on: Optional[datetime] = Field(default=None, description="When the next attempt is due, as a UTC instant ending in `Z` like `creationTime`. While an attempt is being sent  right now it holds the moment that attempt's lease expires, a few minutes ahead, rather than a scheduled retry;  it changes again once the attempt ends. Empty means no attempt will follow: the record is delivered, its retries  ran out, a manual retry of the same event took over from it, or the portal stopped it - because the subscription  was disabled or removed or its address rejected, the subscription's creator may no longer receive the event,  the stored body cannot be read or is in the payload format of a previous version, the portal is removed, the  record waited longer than the retry schedule allows, the portal was restored from a backup taken before the  record was answered, or the portal was moved to another region while the record was being sent. A stopped  record that was never attempted says why in `responsePayload`; one that was keeps the target's last answer there.", alias="nextAttemptOn", json_schema_extra={"examples": ["2024-01-15T10:35:00Z"]})
    __properties: ClassVar[List[str]] = ["id", "eventId", "retriedBy", "configName", "trigger", "creationTime", "method", "route", "requestHeaders", "requestPayload", "responseHeaders", "responsePayload", "status", "delivery", "attempts", "nextAttemptOn"]

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
        # override the default output from pydantic by calling `to_dict()` of retried_by
        if self.retried_by:
            _dict['retriedBy'] = self.retried_by.to_dict()
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

        # set to None if next_attempt_on (nullable) is None
        # and model_fields_set contains the field
        if self.next_attempt_on is None and "next_attempt_on" in self.model_fields_set:
            _dict['nextAttemptOn'] = None

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
            "eventId": obj.get("eventId"),
            "retriedBy": EmployeeDto.from_dict(obj["retriedBy"]) if obj.get("retriedBy") is not None else None,
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
            "delivery": obj.get("delivery"),
            "attempts": obj.get("attempts"),
            "nextAttemptOn": obj.get("nextAttemptOn")
        })
        return _obj


