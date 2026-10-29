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
from typing import Any, ClassVar, Dict, List
from docspace_api_sdk.models.ai_entry_metadata_custom_fields_inner import AiEntryMetadataCustomFieldsInner
from docspace_api_sdk.models.ai_entry_metadata_templates_inner import AiEntryMetadataTemplatesInner
from typing import Optional, Set
from typing_extensions import Self

class AiEntryMetadata(BaseModel):
    """
    AiEntryMetadata
    """ # noqa: E501
    templates: List[AiEntryMetadataTemplatesInner]
    custom_fields: List[AiEntryMetadataCustomFieldsInner] = Field(alias="customFields")
    __properties: ClassVar[List[str]] = ["templates", "customFields"]

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
        """Create an instance of AiEntryMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in templates (list)
        _items = []
        if self.templates:
            for _item_templates in self.templates:
                if _item_templates:
                    _items.append(_item_templates.to_dict())
            _dict['templates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item_custom_fields in self.custom_fields:
                if _item_custom_fields:
                    _items.append(_item_custom_fields.to_dict())
            _dict['customFields'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiEntryMetadata from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "templates": [AiEntryMetadataTemplatesInner.from_dict(_item) for _item in obj["templates"]] if obj.get("templates") is not None else None,
            "customFields": [AiEntryMetadataCustomFieldsInner.from_dict(_item) for _item in obj["customFields"]] if obj.get("customFields") is not None else None
        })
        return _obj


