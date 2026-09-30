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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AiChatPriceDto(BaseModel):
    """
    What a chat model charges, split by the direction the tokens flow in.
    """ # noqa: E501
    prompt: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost of one million tokens sent to the model, which includes the conversation history resent with  every turn and not just the newest message.", json_schema_extra={"examples": [5.0]})
    completion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost of one million tokens the model writes back. It is normally the dearer of the two directions.", json_schema_extra={"examples": [15.0]})
    prompt_cache_read: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost of one million prompt tokens served from the prompt cache. It is absent when the model does not  support prompt caching.", alias="promptCacheRead", json_schema_extra={"examples": [0.2]})
    prompt_cache_write: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost of one million prompt tokens written to the prompt cache with the default lifetime. It is absent  when the model does not support prompt caching.", alias="promptCacheWrite", json_schema_extra={"examples": [2.5]})
    prompt_cache_write1_h: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cost of one million prompt tokens written to the prompt cache with a one-hour lifetime. It is absent  when the model offers no such option.", alias="promptCacheWrite1H", json_schema_extra={"examples": [4.0]})
    __properties: ClassVar[List[str]] = ["prompt", "completion", "promptCacheRead", "promptCacheWrite", "promptCacheWrite1H"]

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
        """Create an instance of AiChatPriceDto from a JSON string"""
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
        # set to None if prompt_cache_read (nullable) is None
        # and model_fields_set contains the field
        if self.prompt_cache_read is None and "prompt_cache_read" in self.model_fields_set:
            _dict['promptCacheRead'] = None

        # set to None if prompt_cache_write (nullable) is None
        # and model_fields_set contains the field
        if self.prompt_cache_write is None and "prompt_cache_write" in self.model_fields_set:
            _dict['promptCacheWrite'] = None

        # set to None if prompt_cache_write1_h (nullable) is None
        # and model_fields_set contains the field
        if self.prompt_cache_write1_h is None and "prompt_cache_write1_h" in self.model_fields_set:
            _dict['promptCacheWrite1H'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiChatPriceDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prompt": obj.get("prompt"),
            "completion": obj.get("completion"),
            "promptCacheRead": obj.get("promptCacheRead"),
            "promptCacheWrite": obj.get("promptCacheWrite"),
            "promptCacheWrite1H": obj.get("promptCacheWrite1H")
        })
        return _obj


