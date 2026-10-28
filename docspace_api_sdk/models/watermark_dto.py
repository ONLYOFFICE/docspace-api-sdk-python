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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace_api_sdk.models.watermark_additions import WatermarkAdditions
from typing import Optional, Set
from typing_extensions import Self

class WatermarkDto(BaseModel):
    """
    The watermark drawn over the documents of a room while they are viewed and printed.
    """ # noqa: E501
    additions: WatermarkAdditions = Field(description="Which details of the reader and of the room are stamped alongside the text. The values combine, so a number  that is not a member on its own is the sum of several of them, and 0 means that only the text is stamped.")
    text: Optional[StrictStr] = Field(default=None, description="The fixed line drawn over the document, printed before the details selected alongside it. Empty when the room  stamps an image instead.", json_schema_extra={"examples": ["Confidential"]})
    rotate: StrictInt = Field(description="How far the stamp is turned, in degrees, with negative values turning it anticlockwise and 0 drawing it  horizontally.", json_schema_extra={"examples": [-45]})
    image_scale: StrictInt = Field(description="How large the image is drawn, as a percentage of its own size. It is 0 for a text watermark, where nothing is  scaled.", alias="imageScale", json_schema_extra={"examples": [100]})
    image_url: Optional[StrictStr] = Field(default=None, description="The address the stamped picture is served from, inside the storage of the room. Empty for a text watermark.", alias="imageUrl", json_schema_extra={"examples": ["https://portal.example.com/storage/watermark_a1b2c3.png"]})
    image_height: Union[StrictFloat, StrictInt] = Field(description="The height the picture is drawn with, in pixels, kept together with the width so that the proportions survive.  It is 0 for a text watermark.", alias="imageHeight", json_schema_extra={"examples": [100.0]})
    image_width: Union[StrictFloat, StrictInt] = Field(description="The width the picture is drawn with, in pixels, kept together with the height so that the proportions survive.  It is 0 for a text watermark.", alias="imageWidth", json_schema_extra={"examples": [200.0]})
    __properties: ClassVar[List[str]] = ["additions", "text", "rotate", "imageScale", "imageUrl", "imageHeight", "imageWidth"]

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
        """Create an instance of WatermarkDto from a JSON string"""
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
        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['imageUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WatermarkDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "additions": obj.get("additions"),
            "text": obj.get("text"),
            "rotate": obj.get("rotate"),
            "imageScale": obj.get("imageScale"),
            "imageUrl": obj.get("imageUrl"),
            "imageHeight": obj.get("imageHeight"),
            "imageWidth": obj.get("imageWidth")
        })
        return _obj


