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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_action_args import AiActionArgs
from typing import Optional, Set
from typing_extensions import Self

class AiRegenerateStreamRequest(BaseModel):
    """
    AiRegenerateStreamRequest
    """ # noqa: E501
    thread_id: StrictStr = Field(description="Target thread (must already exist).", alias="threadId")
    message_id: Optional[StrictStr] = Field(default=None, description="The user message to re-roll from: everything stored after it is deleted. When omitted, or no longer in the thread, the last user message is used.", alias="messageId")
    keep_count: Optional[StrictInt] = Field(default=None, description="How many messages from the start of the thread to keep, used when `messageId` does not resolve. The message at `keepCount - 1` has to be a user message; otherwise the value is ignored.", alias="keepCount")
    expected_length: Optional[StrictInt] = Field(default=None, description="The thread length the caller saw when it computed `keepCount`. When it differs from the stored length, `keepCount` is discarded and the last user message is used instead.", alias="expectedLength")
    action_args: Optional[AiActionArgs] = Field(default=None, description="Per-request options of the round: extra tools, reasoning, a prompt override and the connected context.", alias="actionArgs")
    entity_id: Optional[StrictStr] = Field(default=None, description="Optional entity (room) scope for profile resolution.", alias="entityId")
    context_entity_id: Optional[StrictStr] = Field(default=None, description="The folder or room the user is in. Tools run against it and the model is told it is the user's location; falls back to `entityId` when omitted.", alias="contextEntityId")
    profile_id: Optional[StrictStr] = Field(default=None, description="Session-level profile override for this request only.", alias="profileId")
    __properties: ClassVar[List[str]] = ["threadId", "messageId", "keepCount", "expectedLength", "actionArgs", "entityId", "contextEntityId", "profileId"]

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
        """Create an instance of AiRegenerateStreamRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of action_args
        if self.action_args:
            _dict['actionArgs'] = self.action_args.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiRegenerateStreamRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "threadId": obj.get("threadId"),
            "messageId": obj.get("messageId"),
            "keepCount": obj.get("keepCount"),
            "expectedLength": obj.get("expectedLength"),
            "actionArgs": AiActionArgs.from_dict(obj["actionArgs"]) if obj.get("actionArgs") is not None else None,
            "entityId": obj.get("entityId"),
            "contextEntityId": obj.get("contextEntityId"),
            "profileId": obj.get("profileId")
        })
        return _obj


