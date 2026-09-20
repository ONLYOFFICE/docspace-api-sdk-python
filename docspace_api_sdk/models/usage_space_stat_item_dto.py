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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UsageSpaceStatItemDto(BaseModel):
    """
    The storage one category of a portal module occupies, in the form a statistics page prints it.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The category name in the portal language, HTML-escaped and ready to be rendered as text. What a category  stands for depends on the module asked about - for the Documents module it is a room type.", json_schema_extra={"examples": ["Collaboration rooms"]})
    icon: Optional[StrictStr] = Field(default=None, description="The path of the icon to render beside the name, relative to the portal address. It is empty for a category  that ships no icon.", json_schema_extra={"examples": ["/images/icons/rooms.svg"]})
    disabled: Optional[StrictBool] = Field(default=None, description="Whether the category is switched off for this portal. A disabled category still reports the space it  occupies, so it is worth showing greyed out rather than dropping.", json_schema_extra={"examples": [True]})
    size: Optional[StrictStr] = Field(default=None, description="The occupied space already formatted for display, with its unit and in the portal language - `0 Byte` for  an empty category. It is not a byte count and must not be parsed; the raw numbers live in the quota  reported by `GET api/2.0/portal/quota`.", json_schema_extra={"examples": ["1.5 GB"]})
    url: Optional[StrictStr] = Field(default=None, description="The portal page that lists the contents of this category, relative to the portal address, so a statistics  page can link through to it. It is empty for a category with no page of its own.", json_schema_extra={"examples": ["/rooms/shared"]})
    __properties: ClassVar[List[str]] = ["name", "icon", "disabled", "size", "url"]

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
        """Create an instance of UsageSpaceStatItemDto from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsageSpaceStatItemDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "icon": obj.get("icon"),
            "disabled": obj.get("disabled"),
            "size": obj.get("size"),
            "url": obj.get("url")
        })
        return _obj


