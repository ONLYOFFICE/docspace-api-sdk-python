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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_open_ai_tool_call_delta import AiOpenAIToolCallDelta
from typing import Optional, Set
from typing_extensions import Self

class AiOpenAIChoiceDelta(BaseModel):
    """
    The incremental part of one choice - what this chunk adds to the assistant message.
    """ # noqa: E501
    role: Optional[StrictStr] = Field(default=None, description="Sent on the first chunk only, always `assistant`.")
    content: Optional[StrictStr] = Field(default=None, description="The text this chunk appends. Null when the chunk carries no text.")
    tool_calls: Optional[List[AiOpenAIToolCallDelta]] = Field(default=None, description="The tool calls the model requested, emitted in place of text.")
    __properties: ClassVar[List[str]] = ["role", "content", "tool_calls"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['assistant']):
            raise ValueError("must be one of enum values ('assistant')")
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
        """Create an instance of AiOpenAIChoiceDelta from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tool_calls (list)
        _items = []
        if self.tool_calls:
            for _item_tool_calls in self.tool_calls:
                if _item_tool_calls:
                    _items.append(_item_tool_calls.to_dict())
            _dict['tool_calls'] = _items
        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['content'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiOpenAIChoiceDelta from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "role": obj.get("role"),
            "content": obj.get("content"),
            "tool_calls": [AiOpenAIToolCallDelta.from_dict(_item) for _item in obj["tool_calls"]] if obj.get("tool_calls") is not None else None
        })
        return _obj


