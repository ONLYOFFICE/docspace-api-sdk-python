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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GeneratePresentationToolCallParametersDto(BaseModel):
    """
    The generate presentation tool call parameters.
    """ # noqa: E501
    topic: Optional[StrictStr] = Field(default=None, description="What the generated presentation is about.", json_schema_extra={"examples": ["Sales results for 2026"]})
    slide_count: Optional[StrictStr] = Field(default=None, description="How many slides to generate, as the request spelled it.", alias="slideCount", json_schema_extra={"examples": ["12"]})
    style: Optional[StrictStr] = Field(default=None, description="The visual style the slides should be generated in.", json_schema_extra={"examples": ["minimal"]})
    __properties: ClassVar[List[str]] = ["topic", "slideCount", "style"]

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
        """Create an instance of GeneratePresentationToolCallParametersDto from a JSON string"""
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
        # set to None if topic (nullable) is None
        # and model_fields_set contains the field
        if self.topic is None and "topic" in self.model_fields_set:
            _dict['topic'] = None

        # set to None if slide_count (nullable) is None
        # and model_fields_set contains the field
        if self.slide_count is None and "slide_count" in self.model_fields_set:
            _dict['slideCount'] = None

        # set to None if style (nullable) is None
        # and model_fields_set contains the field
        if self.style is None and "style" in self.model_fields_set:
            _dict['style'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GeneratePresentationToolCallParametersDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "topic": obj.get("topic"),
            "slideCount": obj.get("slideCount"),
            "style": obj.get("style")
        })
        return _obj


