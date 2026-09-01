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
from typing import Optional, Set
from typing_extensions import Self

class AiAiSettingsDto(BaseModel):
    """
    The AI module settings.
    """ # noqa: E501
    vectorization_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether document vectorization is enabled.", alias="vectorizationEnabled", json_schema_extra={"examples": [True]})
    vectorization_need_reset: Optional[StrictBool] = Field(default=None, description="Indicates whether the embedding provider API key needs to be reconfigured.", alias="vectorizationNeedReset", json_schema_extra={"examples": [False]})
    ai_ready: Optional[StrictBool] = Field(default=None, description="Indicates whether the AI subsystem is fully configured and operational.", alias="aiReady", json_schema_extra={"examples": [True]})
    embedding_model: Optional[StrictStr] = Field(description="The name of the embedding model used for document vectorization.", alias="embeddingModel", json_schema_extra={"examples": ["text-embedding-3-small"]})
    system_ai_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the system-level AI provider is enabled.", alias="systemAiEnabled", json_schema_extra={"examples": [True]})
    recommended_model_for_forms: Optional[StrictStr] = Field(default=None, description="The identifier of the model recommended for form generation.", alias="recommendedModelForForms", json_schema_extra={"examples": ["gpt-5.4"]})
    __properties: ClassVar[List[str]] = ["vectorizationEnabled", "vectorizationNeedReset", "aiReady", "embeddingModel", "systemAiEnabled", "recommendedModelForForms"]

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
        """Create an instance of AiAiSettingsDto from a JSON string"""
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
        # set to None if embedding_model (nullable) is None
        # and model_fields_set contains the field
        if self.embedding_model is None and "embedding_model" in self.model_fields_set:
            _dict['embeddingModel'] = None

        # set to None if recommended_model_for_forms (nullable) is None
        # and model_fields_set contains the field
        if self.recommended_model_for_forms is None and "recommended_model_for_forms" in self.model_fields_set:
            _dict['recommendedModelForForms'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiAiSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vectorizationEnabled": obj.get("vectorizationEnabled"),
            "vectorizationNeedReset": obj.get("vectorizationNeedReset"),
            "aiReady": obj.get("aiReady"),
            "embeddingModel": obj.get("embeddingModel"),
            "systemAiEnabled": obj.get("systemAiEnabled"),
            "recommendedModelForForms": obj.get("recommendedModelForForms")
        })
        return _obj


