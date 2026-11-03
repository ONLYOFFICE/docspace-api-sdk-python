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
from docspace_api_sdk.models.ai_action_args_prompt import AiActionArgsPrompt
from docspace_api_sdk.models.ai_context_room_ref import AiContextRoomRef
from docspace_api_sdk.models.ai_folder_context_ref import AiFolderContextRef
from docspace_api_sdk.models.ai_knowledge_room_ref import AiKnowledgeRoomRef
from docspace_api_sdk.models.ai_mcp_item import AiMCPItem
from docspace_api_sdk.models.ai_reasoning_level import AiReasoningLevel
from typing import Optional, Set
from typing_extensions import Self

class AiActionArgs(BaseModel):
    """
    Per-request options of an AI round: extra tools, the depth of reasoning, a system prompt override and the rooms and folder connected as context.
    """ # noqa: E501
    tools: Optional[List[AiMCPItem]] = Field(default=None, description="Extra tools offered to the model for this request.", json_schema_extra={"examples": [[]]})
    is_reasoning: Optional[StrictBool] = Field(default=None, description="Legacy extended-thinking switch; stands for `medium`. `reasoningLevel` wins when both are set.", alias="isReasoning", json_schema_extra={"examples": [False]})
    reasoning_level: Optional[AiReasoningLevel] = Field(default=None, description="Depth of extended thinking for the round; providers clamp it to what the model accepts.", alias="reasoningLevel")
    prompt: Optional[AiActionArgsPrompt] = None
    tool_instructions: Optional[Dict[str, StrictStr]] = Field(default=None, description="Usage notes of the MCP servers the caller holds the connection to, keyed by server type; folded into the system prompt as advisory text.", alias="toolInstructions")
    context_rooms: Optional[List[AiContextRoomRef]] = Field(default=None, description="Instructions rooms connected to the chat as context, each with the skills the round may use.", alias="contextRooms")
    knowledge_rooms: Optional[List[AiKnowledgeRoomRef]] = Field(default=None, description="Knowledge rooms connected to the chat; the knowledge search tool of the round is limited to them. Each `id` has to be a DocSpace room id.", alias="knowledgeRooms")
    knowledge_room: Optional[AiKnowledgeRoomRef] = Field(default=None, description="A single knowledge room, as an older client sends it. Read only when `knowledgeRooms` is absent; send `knowledgeRooms` instead.", alias="knowledgeRoom")
    folder_context: Optional[AiFolderContextRef] = Field(default=None, description="The folder connected to the chat as the round's context. It becomes the location the model is told the user works in, and the entry the round is attributed to.", alias="folderContext")
    entity_id: Optional[StrictStr] = Field(default=None, description="The entry the round is attributed to. A hint, resolved against the caller's own access.", alias="entityId")
    __properties: ClassVar[List[str]] = ["tools", "isReasoning", "reasoningLevel", "prompt", "toolInstructions", "contextRooms", "knowledgeRooms", "knowledgeRoom", "folderContext", "entityId"]

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
        """Create an instance of AiActionArgs from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item_tools in self.tools:
                if _item_tools:
                    _items.append(_item_tools.to_dict())
            _dict['tools'] = _items
        # override the default output from pydantic by calling `to_dict()` of prompt
        if self.prompt:
            _dict['prompt'] = self.prompt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in context_rooms (list)
        _items = []
        if self.context_rooms:
            for _item_context_rooms in self.context_rooms:
                if _item_context_rooms:
                    _items.append(_item_context_rooms.to_dict())
            _dict['contextRooms'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in knowledge_rooms (list)
        _items = []
        if self.knowledge_rooms:
            for _item_knowledge_rooms in self.knowledge_rooms:
                if _item_knowledge_rooms:
                    _items.append(_item_knowledge_rooms.to_dict())
            _dict['knowledgeRooms'] = _items
        # override the default output from pydantic by calling `to_dict()` of knowledge_room
        if self.knowledge_room:
            _dict['knowledgeRoom'] = self.knowledge_room.to_dict()
        # override the default output from pydantic by calling `to_dict()` of folder_context
        if self.folder_context:
            _dict['folderContext'] = self.folder_context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiActionArgs from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tools": [AiMCPItem.from_dict(_item) for _item in obj["tools"]] if obj.get("tools") is not None else None,
            "isReasoning": obj.get("isReasoning"),
            "reasoningLevel": obj.get("reasoningLevel"),
            "prompt": AiActionArgsPrompt.from_dict(obj["prompt"]) if obj.get("prompt") is not None else None,
            "toolInstructions": obj.get("toolInstructions"),
            "contextRooms": [AiContextRoomRef.from_dict(_item) for _item in obj["contextRooms"]] if obj.get("contextRooms") is not None else None,
            "knowledgeRooms": [AiKnowledgeRoomRef.from_dict(_item) for _item in obj["knowledgeRooms"]] if obj.get("knowledgeRooms") is not None else None,
            "knowledgeRoom": AiKnowledgeRoomRef.from_dict(obj["knowledgeRoom"]) if obj.get("knowledgeRoom") is not None else None,
            "folderContext": AiFolderContextRef.from_dict(obj["folderContext"]) if obj.get("folderContext") is not None else None,
            "entityId": obj.get("entityId")
        })
        return _obj


