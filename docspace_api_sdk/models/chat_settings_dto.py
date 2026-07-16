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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_model_capabilities import AiModelCapabilities
from docspace_api_sdk.models.chat_multimodal_settings_dto import ChatMultimodalSettingsDto
from typing import Optional, Set
from typing_extensions import Self

class ChatSettingsDto(BaseModel):
    """
    The chat settings parameters.
    """ # noqa: E501
    provider_id: Optional[StrictInt] = Field(default=None, description="The AI provider ID.", alias="providerId")
    model_id: Optional[StrictStr] = Field(default=None, description="The AI model ID used for chat completions.", alias="modelId")
    model_alias: Optional[StrictStr] = Field(default=None, description="The AI model display alias.", alias="modelAlias")
    prompt: Optional[StrictStr] = Field(default=None, description="The system prompt for the chat.")
    multimodal: Optional[ChatMultimodalSettingsDto] = None
    thinking: Optional[StrictBool] = Field(default=None, description="Indicates whether the model supports extended thinking mode.")
    capabilities: Optional[AiModelCapabilities] = None
    internal: Optional[StrictBool] = Field(default=None, description="Indicates whether this is an internal AI gateway provider.")
    __properties: ClassVar[List[str]] = ["providerId", "modelId", "modelAlias", "prompt", "multimodal", "thinking", "capabilities", "internal"]

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
        """Create an instance of ChatSettingsDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "internal",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of multimodal
        if self.multimodal:
            _dict['multimodal'] = self.multimodal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of capabilities
        if self.capabilities:
            _dict['capabilities'] = self.capabilities.to_dict()
        # set to None if model_id (nullable) is None
        # and model_fields_set contains the field
        if self.model_id is None and "model_id" in self.model_fields_set:
            _dict['modelId'] = None

        # set to None if model_alias (nullable) is None
        # and model_fields_set contains the field
        if self.model_alias is None and "model_alias" in self.model_fields_set:
            _dict['modelAlias'] = None

        # set to None if prompt (nullable) is None
        # and model_fields_set contains the field
        if self.prompt is None and "prompt" in self.model_fields_set:
            _dict['prompt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChatSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "providerId": obj.get("providerId"),
            "modelId": obj.get("modelId"),
            "modelAlias": obj.get("modelAlias"),
            "prompt": obj.get("prompt"),
            "multimodal": ChatMultimodalSettingsDto.from_dict(obj["multimodal"]) if obj.get("multimodal") is not None else None,
            "thinking": obj.get("thinking"),
            "capabilities": AiModelCapabilities.from_dict(obj["capabilities"]) if obj.get("capabilities") is not None else None,
            "internal": obj.get("internal")
        })
        return _obj


