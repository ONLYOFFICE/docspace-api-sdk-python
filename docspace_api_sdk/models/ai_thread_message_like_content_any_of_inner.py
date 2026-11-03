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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_thread_message_like_content_any_of_inner_audio import AiThreadMessageLikeContentAnyOfInnerAudio
from docspace_api_sdk.models.ai_thread_message_like_content_any_of_inner_interrupt import AiThreadMessageLikeContentAnyOfInnerInterrupt
from typing import Optional, Set
from typing_extensions import Self

class AiThreadMessageLikeContentAnyOfInner(BaseModel):
    """
    AiThreadMessageLikeContentAnyOfInner
    """ # noqa: E501
    type: StrictStr = Field(description="Part kind: `text`, `reasoning`, `source`, `image`, `file`, `audio`, `data` or `tool-call`.")
    text: Optional[StrictStr] = Field(default=None, description="The text of a `text` or `reasoning` part.")
    parent_id: Optional[StrictStr] = Field(default=None, description="Id of the part this one belongs to, on `text`, `reasoning`, `source` and `tool-call` parts. On a `reasoning` part the chat library keeps the provider's thinking signature here.", alias="parentId")
    source_type: Optional[StrictStr] = Field(default=None, description="A `source` part's source kind; always `url`.", alias="sourceType")
    id: Optional[StrictStr] = Field(default=None, description="A `source` part's id.")
    url: Optional[StrictStr] = Field(default=None, description="A `source` part's URL.")
    title: Optional[StrictStr] = Field(default=None, description="A `source` part's title.")
    image: Optional[StrictStr] = Field(default=None, description="An `image` part's picture, as a URL (usually a `data:` URL). For an image the user attached, a JSON string `{ ref, title, kind: image }` naming the stored attachment instead.")
    mime_type: Optional[StrictStr] = Field(default=None, description="A `file` part's media type. For a file the user attached, a JSON string `{ ref, title, kind: file, path, type }` naming the stored attachment instead - the chat library carries the reference here.", alias="mimeType")
    data: Optional[StrictStr] = Field(default=None, description="A `file` part's content; empty when the part references an attachment. (A `data` part would carry its payload here too, as any JSON value; neither the chat library nor this service writes one.)")
    filename: Optional[StrictStr] = Field(default=None, description="The file name of a `file` or `image` part.")
    name: Optional[StrictStr] = Field(default=None, description="An `image` part's display name, or a `data` part's name.")
    audio: Optional[AiThreadMessageLikeContentAnyOfInnerAudio] = None
    tool_call_id: Optional[StrictStr] = Field(default=None, description="A `tool-call` part's call id.", alias="toolCallId")
    tool_name: Optional[StrictStr] = Field(default=None, description="A `tool-call` part's tool name.", alias="toolName")
    args: Optional[Dict[str, Any]] = Field(default=None, description="A `tool-call` part's arguments.")
    args_text: Optional[StrictStr] = Field(default=None, description="A `tool-call` part's arguments as the model streamed them, JSON text.", alias="argsText")
    result: Optional[Any] = None
    is_error: Optional[StrictBool] = Field(default=None, description="Whether a `tool-call` part's result is an error.", alias="isError")
    artifact: Optional[Any] = None
    interrupt: Optional[AiThreadMessageLikeContentAnyOfInnerInterrupt] = None
    messages: Optional[List[Dict[str, Any]]] = Field(default=None, description="Messages of a sub-agent run inside a `tool-call` part.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Provider-specific data of a `tool-call` part - for a Gemini call, `{ thoughtSignature }`, which has to be sent back with the call.")
    __properties: ClassVar[List[str]] = ["type", "text", "parentId", "sourceType", "id", "url", "title", "image", "mimeType", "data", "filename", "name", "audio", "toolCallId", "toolName", "args", "argsText", "result", "isError", "artifact", "interrupt", "messages", "metadata"]

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
        """Create an instance of AiThreadMessageLikeContentAnyOfInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of audio
        if self.audio:
            _dict['audio'] = self.audio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interrupt
        if self.interrupt:
            _dict['interrupt'] = self.interrupt.to_dict()
        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

        # set to None if artifact (nullable) is None
        # and model_fields_set contains the field
        if self.artifact is None and "artifact" in self.model_fields_set:
            _dict['artifact'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiThreadMessageLikeContentAnyOfInner from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "text": obj.get("text"),
            "parentId": obj.get("parentId"),
            "sourceType": obj.get("sourceType"),
            "id": obj.get("id"),
            "url": obj.get("url"),
            "title": obj.get("title"),
            "image": obj.get("image"),
            "mimeType": obj.get("mimeType"),
            "data": obj.get("data"),
            "filename": obj.get("filename"),
            "name": obj.get("name"),
            "audio": AiThreadMessageLikeContentAnyOfInnerAudio.from_dict(obj["audio"]) if obj.get("audio") is not None else None,
            "toolCallId": obj.get("toolCallId"),
            "toolName": obj.get("toolName"),
            "args": obj.get("args"),
            "argsText": obj.get("argsText"),
            "result": obj.get("result"),
            "isError": obj.get("isError"),
            "artifact": obj.get("artifact"),
            "interrupt": AiThreadMessageLikeContentAnyOfInnerInterrupt.from_dict(obj["interrupt"]) if obj.get("interrupt") is not None else None,
            "messages": obj.get("messages"),
            "metadata": obj.get("metadata")
        })
        return _obj


