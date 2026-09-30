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
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self

class Module(BaseModel):
    """
    The descriptor of a portal module: what it is called, where it starts and how it is pictured.
    """ # noqa: E501
    id: Optional[UUID] = Field(default=None, description="The identifier of the module. It is the same in every portal and in every language, so use it rather than the  title to tell modules apart.", json_schema_extra={"examples": ["e67be73d-f9ae-4ce1-8fec-1880cb518cb4"]})
    app_name: Optional[StrictStr] = Field(default=None, description="The short system name of the module, the one that appears in its addresses and in the portal configuration.  Unlike the title it is not translated.", alias="appName", json_schema_extra={"examples": ["files"]})
    title: Optional[StrictStr] = Field(default=None, description="The display name of the module, already translated for the calling account, so it changes with the language  and must not be compared against a fixed string.", json_schema_extra={"examples": ["Documents"]})
    link: Optional[StrictStr] = Field(default=None, description="The address of the start page of the module, to be opened in a browser rather than called as an API.", json_schema_extra={"examples": ["https://example.com"]})
    icon_url: Optional[StrictStr] = Field(default=None, description="The address of the small icon of the module, meant for a menu entry.", alias="iconUrl", json_schema_extra={"examples": ["https://example.com/icon.svg"]})
    image_url: Optional[StrictStr] = Field(default=None, description="The address of the large image of the module, meant for a tile or a start screen.", alias="imageUrl", json_schema_extra={"examples": ["https://example.com/image.png"]})
    help_url: Optional[StrictStr] = Field(default=None, description="The address of the help section of the module. It is empty when the portal publishes no help for it.", alias="helpUrl", json_schema_extra={"examples": ["https://example.com/help"]})
    description: Optional[StrictStr] = Field(default=None, description="The one-line description of the module shown next to its title, translated for the calling account.", json_schema_extra={"examples": ["File management"]})
    is_primary: Optional[StrictBool] = Field(default=None, description="Whether the portal opens this module first when no other destination is given.", alias="isPrimary", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["id", "appName", "title", "link", "iconUrl", "imageUrl", "helpUrl", "description", "isPrimary"]

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
        """Create an instance of Module from a JSON string"""
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
        # set to None if app_name (nullable) is None
        # and model_fields_set contains the field
        if self.app_name is None and "app_name" in self.model_fields_set:
            _dict['appName'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if icon_url (nullable) is None
        # and model_fields_set contains the field
        if self.icon_url is None and "icon_url" in self.model_fields_set:
            _dict['iconUrl'] = None

        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['imageUrl'] = None

        # set to None if help_url (nullable) is None
        # and model_fields_set contains the field
        if self.help_url is None and "help_url" in self.model_fields_set:
            _dict['helpUrl'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Module from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "appName": obj.get("appName"),
            "title": obj.get("title"),
            "link": obj.get("link"),
            "iconUrl": obj.get("iconUrl"),
            "imageUrl": obj.get("imageUrl"),
            "helpUrl": obj.get("helpUrl"),
            "description": obj.get("description"),
            "isPrimary": obj.get("isPrimary")
        })
        return _obj


