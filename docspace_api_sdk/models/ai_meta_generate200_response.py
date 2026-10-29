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
from docspace_api_sdk.models.ai_meta_generate200_response_fields_inner import AiMetaGenerate200ResponseFieldsInner
from docspace_api_sdk.models.ai_meta_generate200_response_skipped_inner import AiMetaGenerate200ResponseSkippedInner
from docspace_api_sdk.models.ai_meta_generate200_response_sources_inner import AiMetaGenerate200ResponseSourcesInner
from typing import Optional, Set
from typing_extensions import Self

class AiMetaGenerate200Response(BaseModel):
    """
    AiMetaGenerate200Response
    """ # noqa: E501
    fields: List[AiMetaGenerate200ResponseFieldsInner] = Field(description="The proposed custom metadata fields with the values the text supports.")
    sources: List[AiMetaGenerate200ResponseSourcesInner] = Field(description="The documents the proposal was read from.")
    skipped: List[AiMetaGenerate200ResponseSkippedInner] = Field(description="The entries that were left out, with the reason for each.")
    __properties: ClassVar[List[str]] = ["fields", "sources", "skipped"]

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
        """Create an instance of AiMetaGenerate200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item_sources in self.sources:
                if _item_sources:
                    _items.append(_item_sources.to_dict())
            _dict['sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in skipped (list)
        _items = []
        if self.skipped:
            for _item_skipped in self.skipped:
                if _item_skipped:
                    _items.append(_item_skipped.to_dict())
            _dict['skipped'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiMetaGenerate200Response from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fields": [AiMetaGenerate200ResponseFieldsInner.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "sources": [AiMetaGenerate200ResponseSourcesInner.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "skipped": [AiMetaGenerate200ResponseSkippedInner.from_dict(_item) for _item in obj["skipped"]] if obj.get("skipped") is not None else None
        })
        return _obj


