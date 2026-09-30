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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace_api_sdk.models.ai_provider_type import AiProviderType
from docspace_api_sdk.models.ai_reasoning_support import AiReasoningSupport
from typing import Optional, Set
from typing_extensions import Self

class AiModel(BaseModel):
    """
    AI model metadata. Describes a single model available from a provider.
    """ # noqa: E501
    id: StrictStr = Field(description="Model identifier as used by the provider API (e.g. `gpt-4o`, `claude-sonnet-4-20250514`).", json_schema_extra={"examples": ["gpt-4o"]})
    name: StrictStr = Field(description="Human-readable model name for display in the UI.", json_schema_extra={"examples": ["GPT-4o"]})
    provider: AiProviderType = Field(description="Provider that offers this model.")
    reasoning: Optional[StrictBool] = Field(default=None, description="Whether this model supports extended thinking / chain-of-thought reasoning.", json_schema_extra={"examples": [False]})
    reasoning_support: Optional[AiReasoningSupport] = Field(default=None, description="What the model can do with extended thinking, when the provider's catalogue says so (OpenRouter and the ONLYOFFICE route report a per-model `reasoning` object). Copied onto the profile at save time; absent, the widget falls back to the provider's id-based table.", alias="reasoningSupport")
    capabilities: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Bitmask of model capabilities (Chat, Image, Vision, Tools, etc.). Used to filter models per `ActionType`.", json_schema_extra={"examples": [7]})
    __properties: ClassVar[List[str]] = ["id", "name", "provider", "reasoning", "reasoningSupport", "capabilities"]

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
        """Create an instance of AiModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of provider
        if self.provider:
            _dict['provider'] = self.provider.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reasoning_support
        if self.reasoning_support:
            _dict['reasoningSupport'] = self.reasoning_support.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiModel from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "provider": AiProviderType.from_dict(obj["provider"]) if obj.get("provider") is not None else None,
            "reasoning": obj.get("reasoning"),
            "reasoningSupport": AiReasoningSupport.from_dict(obj["reasoningSupport"]) if obj.get("reasoningSupport") is not None else None,
            "capabilities": obj.get("capabilities")
        })
        return _obj


