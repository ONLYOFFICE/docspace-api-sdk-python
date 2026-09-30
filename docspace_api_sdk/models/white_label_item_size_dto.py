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
    The pixel box a logo slot is drawn in, in the shape the imaging library reports a geometry.
    """ # noqa: E501
    aspect_ratio: Optional[StrictBool] = Field(default=None, description="Whether the numbers are to be read as an aspect ratio rather than as pixels. Always `false` on the sizes  this API reports.", alias="aspectRatio", json_schema_extra={"examples": [False]})
    fill_area: Optional[StrictBool] = Field(default=None, description="Whether an image would be scaled to cover the box rather than to fit inside it. Always `false` here.", alias="fillArea", json_schema_extra={"examples": [False]})
    greater: Optional[StrictBool] = Field(default=None, description="Whether scaling would apply only to an image larger than the box. Always `false` here.", json_schema_extra={"examples": [False]})
    height: Optional[StrictInt] = Field(default=None, description="The height of the box in pixels - one of the two fields of this object that carry information.", json_schema_extra={"examples": [48]})
    ignore_aspect_ratio: Optional[StrictBool] = Field(default=None, description="Whether scaling would be allowed to distort the image. Always `false` here.", alias="ignoreAspectRatio", json_schema_extra={"examples": [False]})
    is_percentage: Optional[StrictBool] = Field(default=None, description="Whether `width` and `height` are to be read as percentages. Always `false` here, so both are pixels.", alias="isPercentage", json_schema_extra={"examples": [False]})
    less: Optional[StrictBool] = Field(default=None, description="Whether scaling would apply only to an image smaller than the box. Always `false` here.", json_schema_extra={"examples": [False]})
    limit_pixels: Optional[StrictBool] = Field(default=None, description="Whether the box is to be read as a total pixel-area budget instead of as two dimensions. Always `false`  here.", alias="limitPixels", json_schema_extra={"examples": [False]})
    width: Optional[StrictInt] = Field(default=None, description="The width of the box in pixels - the other field of this object that carries information.", json_schema_extra={"examples": [422]})
    x: Optional[StrictInt] = Field(default=None, description="The horizontal offset of the box from the origin. Always `0` here.", json_schema_extra={"examples": [0]})
    y: Optional[StrictInt] = Field(default=None, description="The vertical offset of the box from the origin. Always `0` here.", json_schema_extra={"examples": [0]})
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


