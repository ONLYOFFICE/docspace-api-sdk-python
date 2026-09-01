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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike
from typing import Optional, Set
from typing_extensions import Self

class AiChatEvent(BaseModel):
    """
    Discriminated event emitted by the streaming methods of `AIEngine`. The engine never invokes user-supplied middleware or callbacks directly — every observable side-effect is encoded as a `ChatEvent` so the same stream can be replayed over SSE, WebSocket, or in-process.  Pause point: `tool-call-pending` is the only stop. The UI must execute the tool itself (consulting `autoAllow` to decide between the silent path and the approve dialog) and resume via `AIEngine.approveToolCall` or `AIEngine.denyToolCall`.  Other variants are pure data:  - `message-start` / `message-delta` / `message-end` — assistant reply lifecycle. - `message-incomplete` — the provider returned an error or incomplete status. - `thread-title` — auto-generated title ready for a new thread.
    """ # noqa: E501
    type: StrictStr = Field(description="Emitted once per `sendWithStream` call, immediately after the user message has been persisted by storage and before the assistant stream starts. Carries the storage-assigned `id` and `createdAt`. The UI uses it to render the user bubble — no client-side optimistic placeholder is needed, which keeps the runtime tree free of phantom nodes from index-fallback ids.")
    message: Optional[AiThreadMessageLike] = Field(default=None, description="The message the event is about, in the state it has reached.")
    message_id: Optional[StrictStr] = Field(default=None, description="The storage identifier of that message.", alias="messageId")
    idx: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The zero-based position of the pending tool call within the message.")
    thread_id: Optional[StrictStr] = Field(default=None, description="The thread the event belongs to.", alias="threadId")
    auto_allow: Optional[StrictBool] = Field(default=None, description="The consumer should execute the tool without prompting the user. True when the tool is in the persisted always-allow list, or the tool itself opts in via `TMCPItem.requireApproval === false` (host tools default to this). For a client-side tool with a server-side engine, this lets the engine return the pending call already flagged auto-allow so the client runs it and streams the result back without a dialog round-trip.", alias="autoAllow")
    server_executed: Optional[StrictBool] = Field(default=None, description="Set when the tool is served by a server-side system source: the consumer must NOT execute it locally — only show the approval UI (unless `autoAllow`) and resume via `approveToolCall` (no `result` needed) / `denyToolCall`. The engine runs it in-engine.", alias="serverExecuted")
    title: Optional[StrictStr] = Field(default=None, description="The generated thread title.")
    profile_id: Optional[StrictStr] = Field(default=None, description="The profile that generated the title, when one was used.", alias="profileId")
    __properties: ClassVar[List[str]] = ["type", "message", "messageId", "idx", "threadId", "autoAllow", "serverExecuted", "title", "profileId"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['user-message-stored', 'message-start', 'message-delta', 'message-end', 'message-incomplete', 'tool-call-pending', 'thread-title']):
            raise ValueError("must be one of enum values ('user-message-stored', 'message-start', 'message-delta', 'message-end', 'message-incomplete', 'tool-call-pending', 'thread-title')")
        return value

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
        """Create an instance of AiChatEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiChatEvent from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "message": AiThreadMessageLike.from_dict(obj["message"]) if obj.get("message") is not None else None,
            "messageId": obj.get("messageId"),
            "idx": obj.get("idx"),
            "threadId": obj.get("threadId"),
            "autoAllow": obj.get("autoAllow"),
            "serverExecuted": obj.get("serverExecuted"),
            "title": obj.get("title"),
            "profileId": obj.get("profileId")
        })
        return _obj


