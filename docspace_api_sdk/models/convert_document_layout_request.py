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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ConvertDocumentLayoutRequest(BaseModel):
    """
    The layout of forms printed as pdf documents or images.
    """ # noqa: E501
    draw_place_holders: Optional[StrictBool] = Field(default=None, description="Whether an empty form field shows its placeholder text in the result; false leaves it blank.", alias="drawPlaceHolders", json_schema_extra={"examples": [True]})
    draw_form_highlight: Optional[StrictBool] = Field(default=None, description="Whether form fields keep their highlight colour in the result; false draws them without it.", alias="drawFormHighlight", json_schema_extra={"examples": [False]})
    is_print: Optional[StrictBool] = Field(default=None, description="Whether the print mode is turned on. It only applies to a docx converted into pdf: with the print mode off  the highlight flag does nothing and the placeholder flag saves the forms in the pdf.", alias="isPrint", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["drawPlaceHolders", "drawFormHighlight", "isPrint"]

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
        """Create an instance of ConvertDocumentLayoutRequest from a JSON string"""
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
        # set to None if draw_place_holders (nullable) is None
        # and model_fields_set contains the field
        if self.draw_place_holders is None and "draw_place_holders" in self.model_fields_set:
            _dict['drawPlaceHolders'] = None

        # set to None if draw_form_highlight (nullable) is None
        # and model_fields_set contains the field
        if self.draw_form_highlight is None and "draw_form_highlight" in self.model_fields_set:
            _dict['drawFormHighlight'] = None

        # set to None if is_print (nullable) is None
        # and model_fields_set contains the field
        if self.is_print is None and "is_print" in self.model_fields_set:
            _dict['isPrint'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConvertDocumentLayoutRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "drawPlaceHolders": obj.get("drawPlaceHolders"),
            "drawFormHighlight": obj.get("drawFormHighlight"),
            "isPrint": obj.get("isPrint")
        })
        return _obj


