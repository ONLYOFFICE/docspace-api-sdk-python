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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_ai_action_args_prompt import AiAiActionArgsPrompt
from docspace_api_sdk.models.ai_tmcp_item import AiTMCPItem
from typing import Optional, Set
from typing_extensions import Self

class AiAiActionArgs(BaseModel):
    """
    Wire-serializable subset of the engine's `ActionArgs` — drops the engine-injected `signal`/`fetch`; `profile`/`messages` are owned by the engine and never sent by the caller.
    """ # noqa: E501
    tools: Optional[List[AiTMCPItem]] = Field(default=None, description="Extra tools offered to the model for this request.")
    is_reasoning: Optional[StrictBool] = Field(default=None, description="Enable extended thinking / reasoning for this request.", alias="isReasoning")
    prompt: Optional[AiAiActionArgsPrompt] = None
    __properties: ClassVar[List[str]] = ["tools", "isReasoning", "prompt"]

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
        """Create an instance of AiAiActionArgs from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiAiActionArgs from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tools": [AiTMCPItem.from_dict(_item) for _item in obj["tools"]] if obj.get("tools") is not None else None,
            "isReasoning": obj.get("isReasoning"),
            "prompt": AiAiActionArgsPrompt.from_dict(obj["prompt"]) if obj.get("prompt") is not None else None
        })
        return _obj


