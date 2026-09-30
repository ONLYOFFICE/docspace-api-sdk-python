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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OperationTokenUsage(BaseModel):
    """
    Tokens an AI operation consumed, as recorded in the operation metadata. A kind the provider did not report is `0`.
    """ # noqa: E501
    total_tokens: Optional[StrictInt] = Field(default=None, description="All tokens of the request: prompt plus completion.", alias="totalTokens", json_schema_extra={"examples": [20747]})
    prompt_tokens: Optional[StrictInt] = Field(default=None, description="Tokens sent to the model, cached ones included.", alias="promptTokens", json_schema_extra={"examples": [19332]})
    completion_tokens: Optional[StrictInt] = Field(default=None, description="Tokens the model generated, reasoning ones included.", alias="completionTokens", json_schema_extra={"examples": [1415]})
    cached_tokens: Optional[StrictInt] = Field(default=None, description="Part of the prompt tokens read from the provider cache.", alias="cachedTokens", json_schema_extra={"examples": [19226]})
    cache_write_tokens: Optional[StrictInt] = Field(default=None, description="Part of the prompt tokens written to the provider cache.", alias="cacheWriteTokens", json_schema_extra={"examples": [104]})
    reasoning_tokens: Optional[StrictInt] = Field(default=None, description="Part of the completion tokens the model spent on reasoning.", alias="reasoningTokens", json_schema_extra={"examples": [68]})
    image_tokens: Optional[StrictInt] = Field(default=None, description="Tokens spent on images.", alias="imageTokens", json_schema_extra={"examples": [0]})
    __properties: ClassVar[List[str]] = ["totalTokens", "promptTokens", "completionTokens", "cachedTokens", "cacheWriteTokens", "reasoningTokens", "imageTokens"]

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
        """Create an instance of OperationTokenUsage from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OperationTokenUsage from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalTokens": obj.get("totalTokens"),
            "promptTokens": obj.get("promptTokens"),
            "completionTokens": obj.get("completionTokens"),
            "cachedTokens": obj.get("cachedTokens"),
            "cacheWriteTokens": obj.get("cacheWriteTokens"),
            "reasoningTokens": obj.get("reasoningTokens"),
            "imageTokens": obj.get("imageTokens")
        })
        return _obj


