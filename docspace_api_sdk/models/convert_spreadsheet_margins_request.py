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

class ConvertSpreadsheetMarginsRequest(BaseModel):
    """
    The margins of the output PDF file, each a length with its unit: mm, cm or in.
    """ # noqa: E501
    left: Optional[StrictStr] = Field(default=None, description="The left margin of the output PDF file.", json_schema_extra={"examples": ["0.7in"]})
    right: Optional[StrictStr] = Field(default=None, description="The right margin of the output PDF file.", json_schema_extra={"examples": ["0.7in"]})
    top: Optional[StrictStr] = Field(default=None, description="The top margin of the output PDF file.", json_schema_extra={"examples": ["0.75in"]})
    bottom: Optional[StrictStr] = Field(default=None, description="The bottom margin of the output PDF file.", json_schema_extra={"examples": ["0.75in"]})
    __properties: ClassVar[List[str]] = ["left", "right", "top", "bottom"]

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
        """Create an instance of ConvertSpreadsheetMarginsRequest from a JSON string"""
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
        # set to None if left (nullable) is None
        # and model_fields_set contains the field
        if self.left is None and "left" in self.model_fields_set:
            _dict['left'] = None

        # set to None if right (nullable) is None
        # and model_fields_set contains the field
        if self.right is None and "right" in self.model_fields_set:
            _dict['right'] = None

        # set to None if top (nullable) is None
        # and model_fields_set contains the field
        if self.top is None and "top" in self.model_fields_set:
            _dict['top'] = None

        # set to None if bottom (nullable) is None
        # and model_fields_set contains the field
        if self.bottom is None and "bottom" in self.model_fields_set:
            _dict['bottom'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConvertSpreadsheetMarginsRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "left": obj.get("left"),
            "right": obj.get("right"),
            "top": obj.get("top"),
            "bottom": obj.get("bottom")
        })
        return _obj


