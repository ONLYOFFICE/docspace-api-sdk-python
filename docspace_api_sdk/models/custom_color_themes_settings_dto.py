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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.custom_color_themes_settings_item import CustomColorThemesSettingsItem
from typing import Optional, Set
from typing_extensions import Self

class CustomColorThemesSettingsDto(BaseModel):
    """
    The colour themes the portal offers, which of them is applied, and how many the plan allows.
    """ # noqa: E501
    themes: Optional[List[CustomColorThemesSettingsItem]] = Field(default=None, description="Every theme the portal can apply, ordered by ID, with the built-in ones first because they were created  first. It is never empty - the built-in themes cannot be deleted - and a custom theme is one whose ID is  higher than the built-in ones.", json_schema_extra={"examples": [[{"id": 1, "name": "Custom Theme"}]]})
    selected: Optional[StrictInt] = Field(default=None, description="The ID of the theme in `themes` that is currently applied to the whole portal. Deleting the applied theme  moves it to the lowest remaining ID, so it can change without anyone having chosen a new one.", json_schema_extra={"examples": [1]})
    limit: Optional[StrictInt] = Field(default=None, description="How many entries `themes` may hold in total, built-in ones included; `0` means the plan caps nothing. Once  the cap is reached `PUT api/2.0/settings/colortheme` drops a new theme silently instead of failing, so  compare this with the length of `themes` to tell whether a save took effect.", json_schema_extra={"examples": [1]})
    __properties: ClassVar[List[str]] = ["themes", "selected", "limit"]

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
        """Create an instance of CustomColorThemesSettingsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in themes (list)
        _items = []
        if self.themes:
            for _item_themes in self.themes:
                if _item_themes:
                    _items.append(_item_themes.to_dict())
            _dict['themes'] = _items
        # set to None if themes (nullable) is None
        # and model_fields_set contains the field
        if self.themes is None and "themes" in self.model_fields_set:
            _dict['themes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomColorThemesSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "themes": [CustomColorThemesSettingsItem.from_dict(_item) for _item in obj["themes"]] if obj.get("themes") is not None else None,
            "selected": obj.get("selected"),
            "limit": obj.get("limit")
        })
        return _obj


