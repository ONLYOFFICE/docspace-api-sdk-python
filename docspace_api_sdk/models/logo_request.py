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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class LogoRequest(BaseModel):
    """
    The logo request parameters.
    """ # noqa: E501
    tmp_file: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The path to the temporary image file.", alias="tmpFile", json_schema_extra={"examples": ["/tmp/logo.png"]})
    x: Optional[Annotated[int, Field(le=1280, strict=True, ge=0)]] = Field(default=None, description="The X coordinate of the rectangle starting point.", json_schema_extra={"examples": [0]})
    y: Optional[Annotated[int, Field(le=1280, strict=True, ge=0)]] = Field(default=None, description="The Y coordinate of the rectangle starting point.", json_schema_extra={"examples": [0]})
    width: Optional[Annotated[int, Field(le=1280, strict=True, ge=1)]] = Field(default=None, description="The rectangle width.", json_schema_extra={"examples": [100]})
    height: Optional[Annotated[int, Field(le=1280, strict=True, ge=1)]] = Field(default=None, description="The rectangle height.", json_schema_extra={"examples": [100]})
    __properties: ClassVar[List[str]] = ["tmpFile", "x", "y", "width", "height"]

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
        """Create an instance of LogoRequest from a JSON string"""
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
        """Create an instance of LogoRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tmpFile": obj.get("tmpFile"),
            "x": obj.get("x"),
            "y": obj.get("y"),
            "width": obj.get("width"),
            "height": obj.get("height")
        })
        return _obj


