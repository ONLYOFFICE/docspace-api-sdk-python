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
from typing import Any, ClassVar, Dict, List
from docspace_api_sdk.models.ai_entry_metadata import AiEntryMetadata
from docspace_api_sdk.models.ai_meta_fill200_response_filled_inner import AiMetaFill200ResponseFilledInner
from docspace_api_sdk.models.ai_meta_fill200_response_sources_inner import AiMetaFill200ResponseSourcesInner
from docspace_api_sdk.models.ai_meta_fill200_response_unresolved_inner import AiMetaFill200ResponseUnresolvedInner
from docspace_api_sdk.models.ai_meta_generate200_response_skipped_inner import AiMetaGenerate200ResponseSkippedInner
from typing import Optional, Set
from typing_extensions import Self

class AiMetaFill200Response(BaseModel):
    """
    AiMetaFill200Response
    """ # noqa: E501
    dry_run: StrictBool = Field(description="Whether the values were only proposed (`true`) or written as well.", alias="dryRun")
    metadata: AiEntryMetadata = Field(description="The entry's metadata after the write (or as it stands, with `dryRun`), as `GET api/2.0/files/metadata/{kind}/{id}` returns it.")
    filled: List[AiMetaFill200ResponseFilledInner] = Field(description="The values written, or proposed with `dryRun`: a typed value for a template field, a string for a custom field.")
    unresolved: List[AiMetaFill200ResponseUnresolvedInner] = Field(description="The fields left as they were, with the reason for each.")
    sources: List[AiMetaFill200ResponseSourcesInner] = Field(description="The documents the values were read from.")
    skipped: List[AiMetaGenerate200ResponseSkippedInner] = Field(description="The entries that were left out, with the reason for each.")
    __properties: ClassVar[List[str]] = ["dryRun", "metadata", "filled", "unresolved", "sources", "skipped"]

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
        """Create an instance of AiMetaFill200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in filled (list)
        _items = []
        if self.filled:
            for _item_filled in self.filled:
                if _item_filled:
                    _items.append(_item_filled.to_dict())
            _dict['filled'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in unresolved (list)
        _items = []
        if self.unresolved:
            for _item_unresolved in self.unresolved:
                if _item_unresolved:
                    _items.append(_item_unresolved.to_dict())
            _dict['unresolved'] = _items
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
        """Create an instance of AiMetaFill200Response from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dryRun": obj.get("dryRun"),
            "metadata": AiEntryMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "filled": [AiMetaFill200ResponseFilledInner.from_dict(_item) for _item in obj["filled"]] if obj.get("filled") is not None else None,
            "unresolved": [AiMetaFill200ResponseUnresolvedInner.from_dict(_item) for _item in obj["unresolved"]] if obj.get("unresolved") is not None else None,
            "sources": [AiMetaFill200ResponseSourcesInner.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "skipped": [AiMetaGenerate200ResponseSkippedInner.from_dict(_item) for _item in obj["skipped"]] if obj.get("skipped") is not None else None
        })
        return _obj


