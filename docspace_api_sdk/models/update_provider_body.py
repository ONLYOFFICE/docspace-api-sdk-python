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
from docspace_api_sdk.models.model_settings_item_dto import ModelSettingsItemDto
from typing import Optional, Set
from typing_extensions import Self

class UpdateProviderBody(BaseModel):
    """
    Parameters for updating an AI provider's configuration.
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The new display title for the AI provider. If null, the title is not changed.")
    url: Optional[StrictStr] = Field(default=None, description="The new API endpoint URL for the AI provider. If null, the URL is not changed.")
    key: Optional[StrictStr] = Field(default=None, description="The new authentication API key for the AI provider. If null, the key is not changed.")
    model_settings: Optional[List[ModelSettingsItemDto]] = Field(default=None, description="Optional list of model settings changes to apply atomically with the provider update.", alias="modelSettings")
    __properties: ClassVar[List[str]] = ["title", "url", "key", "modelSettings"]

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
        """Create an instance of UpdateProviderBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in model_settings (list)
        _items = []
        if self.model_settings:
            for _item_model_settings in self.model_settings:
                if _item_model_settings:
                    _items.append(_item_model_settings.to_dict())
            _dict['modelSettings'] = _items
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if model_settings (nullable) is None
        # and model_fields_set contains the field
        if self.model_settings is None and "model_settings" in self.model_fields_set:
            _dict['modelSettings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateProviderBody from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "url": obj.get("url"),
            "key": obj.get("key"),
            "modelSettings": [ModelSettingsItemDto.from_dict(_item) for _item in obj["modelSettings"]] if obj.get("modelSettings") is not None else None
        })
        return _obj


