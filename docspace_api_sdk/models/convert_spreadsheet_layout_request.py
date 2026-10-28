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
from docspace_api_sdk.models.convert_spreadsheet_margins_request import ConvertSpreadsheetMarginsRequest
from docspace_api_sdk.models.convert_spreadsheet_page_size_request import ConvertSpreadsheetPageSizeRequest
from typing import Optional, Set
from typing_extensions import Self

class ConvertSpreadsheetLayoutRequest(BaseModel):
    """
    How a spreadsheet converted to PDF is laid out on the page. A field left out takes the document service default.
    """ # noqa: E501
    ignore_print_area: Optional[StrictBool] = Field(default=None, description="Whether the print area chosen in the spreadsheet is ignored; false converts only that area.", alias="ignorePrintArea", json_schema_extra={"examples": [False]})
    orientation: Optional[StrictStr] = Field(default=None, description="The page orientation of the output PDF file: portrait or landscape.", json_schema_extra={"examples": ["landscape"]})
    fit_to_height: Optional[StrictInt] = Field(default=None, description="The number of pages the converted area is fitted into in height; 0 does not fit it.", alias="fitToHeight", json_schema_extra={"examples": [0]})
    scale: Optional[StrictInt] = Field(default=None, description="The scale of the output PDF file, in percent.", json_schema_extra={"examples": [100]})
    fit_to_width: Optional[StrictInt] = Field(default=None, description="The number of pages the converted area is fitted into in width; 0 does not fit it.", alias="fitToWidth", json_schema_extra={"examples": [1]})
    headings: Optional[StrictBool] = Field(default=None, description="Whether the row and column headings are printed in the output PDF file.", json_schema_extra={"examples": [False]})
    grid_lines: Optional[StrictBool] = Field(default=None, description="Whether the grid lines are printed in the output PDF file.", alias="gridLines", json_schema_extra={"examples": [False]})
    margins: Optional[ConvertSpreadsheetMarginsRequest] = Field(default=None, description="The margins of the output PDF file.")
    page_size: Optional[ConvertSpreadsheetPageSizeRequest] = Field(default=None, description="The page size of the output PDF file.", alias="pageSize")
    __properties: ClassVar[List[str]] = ["ignorePrintArea", "orientation", "fitToHeight", "scale", "fitToWidth", "headings", "gridLines", "margins", "pageSize"]

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
        """Create an instance of ConvertSpreadsheetLayoutRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of margins
        if self.margins:
            _dict['margins'] = self.margins.to_dict()
        # override the default output from pydantic by calling `to_dict()` of page_size
        if self.page_size:
            _dict['pageSize'] = self.page_size.to_dict()
        # set to None if ignore_print_area (nullable) is None
        # and model_fields_set contains the field
        if self.ignore_print_area is None and "ignore_print_area" in self.model_fields_set:
            _dict['ignorePrintArea'] = None

        # set to None if orientation (nullable) is None
        # and model_fields_set contains the field
        if self.orientation is None and "orientation" in self.model_fields_set:
            _dict['orientation'] = None

        # set to None if fit_to_height (nullable) is None
        # and model_fields_set contains the field
        if self.fit_to_height is None and "fit_to_height" in self.model_fields_set:
            _dict['fitToHeight'] = None

        # set to None if scale (nullable) is None
        # and model_fields_set contains the field
        if self.scale is None and "scale" in self.model_fields_set:
            _dict['scale'] = None

        # set to None if fit_to_width (nullable) is None
        # and model_fields_set contains the field
        if self.fit_to_width is None and "fit_to_width" in self.model_fields_set:
            _dict['fitToWidth'] = None

        # set to None if headings (nullable) is None
        # and model_fields_set contains the field
        if self.headings is None and "headings" in self.model_fields_set:
            _dict['headings'] = None

        # set to None if grid_lines (nullable) is None
        # and model_fields_set contains the field
        if self.grid_lines is None and "grid_lines" in self.model_fields_set:
            _dict['gridLines'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConvertSpreadsheetLayoutRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ignorePrintArea": obj.get("ignorePrintArea"),
            "orientation": obj.get("orientation"),
            "fitToHeight": obj.get("fitToHeight"),
            "scale": obj.get("scale"),
            "fitToWidth": obj.get("fitToWidth"),
            "headings": obj.get("headings"),
            "gridLines": obj.get("gridLines"),
            "margins": ConvertSpreadsheetMarginsRequest.from_dict(obj["margins"]) if obj.get("margins") is not None else None,
            "pageSize": ConvertSpreadsheetPageSizeRequest.from_dict(obj["pageSize"]) if obj.get("pageSize") is not None else None
        })
        return _obj


