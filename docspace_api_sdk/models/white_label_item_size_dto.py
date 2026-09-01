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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WhiteLabelItemSizeDto(BaseModel):
    """
    The white label logo size parameters.
    """ # noqa: E501
    aspect_ratio: Optional[StrictBool] = Field(default=None, description="Specifies whether the size is an aspect ratio.", alias="aspectRatio", json_schema_extra={"examples": [False]})
    fill_area: Optional[StrictBool] = Field(default=None, description="Specifies whether the logo is resized based on the smallest fitting dimension.", alias="fillArea", json_schema_extra={"examples": [False]})
    greater: Optional[StrictBool] = Field(default=None, description="Specifies whether the logo is resized only if it is greater than the size.", json_schema_extra={"examples": [False]})
    height: Optional[StrictInt] = Field(default=None, description="The logo height, in pixels.", json_schema_extra={"examples": [48]})
    ignore_aspect_ratio: Optional[StrictBool] = Field(default=None, description="Specifies whether the logo is resized without preserving the aspect ratio.", alias="ignoreAspectRatio", json_schema_extra={"examples": [False]})
    is_percentage: Optional[StrictBool] = Field(default=None, description="Specifies whether the width and height are expressed as percentages.", alias="isPercentage", json_schema_extra={"examples": [False]})
    less: Optional[StrictBool] = Field(default=None, description="Specifies whether the logo is resized only if it is less than the size.", json_schema_extra={"examples": [False]})
    limit_pixels: Optional[StrictBool] = Field(default=None, description="Specifies whether the logo is resized using a pixel area count limit.", alias="limitPixels", json_schema_extra={"examples": [False]})
    width: Optional[StrictInt] = Field(default=None, description="The logo width, in pixels.", json_schema_extra={"examples": [422]})
    x: Optional[StrictInt] = Field(default=None, description="The X offset from the origin, in pixels.", json_schema_extra={"examples": [0]})
    y: Optional[StrictInt] = Field(default=None, description="The Y offset from the origin, in pixels.", json_schema_extra={"examples": [0]})
    __properties: ClassVar[List[str]] = ["aspectRatio", "fillArea", "greater", "height", "ignoreAspectRatio", "isPercentage", "less", "limitPixels", "width", "x", "y"]

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
        """Create an instance of WhiteLabelItemSizeDto from a JSON string"""
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
        """Create an instance of WhiteLabelItemSizeDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aspectRatio": obj.get("aspectRatio"),
            "fillArea": obj.get("fillArea"),
            "greater": obj.get("greater"),
            "height": obj.get("height"),
            "ignoreAspectRatio": obj.get("ignoreAspectRatio"),
            "isPercentage": obj.get("isPercentage"),
            "less": obj.get("less"),
            "limitPixels": obj.get("limitPixels"),
            "width": obj.get("width"),
            "x": obj.get("x"),
            "y": obj.get("y")
        })
        return _obj


