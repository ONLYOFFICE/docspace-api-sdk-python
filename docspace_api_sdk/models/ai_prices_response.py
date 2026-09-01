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
from docspace_api_sdk.models.ai_chat_model_pricing import AiChatModelPricing
from docspace_api_sdk.models.ai_embedding_model_pricing import AiEmbeddingModelPricing
from docspace_api_sdk.models.ai_image_model_pricing import AiImageModelPricing
from docspace_api_sdk.models.ai_web_search_pricing import AiWebSearchPricing
from docspace_api_sdk.models.currency_info import CurrencyInfo
from typing import Optional, Set
from typing_extensions import Self

class AiPricesResponse(BaseModel):
    """
    The AI price list: per-model pricing for every model kind, in a single currency.
    """ # noqa: E501
    chat: Optional[List[AiChatModelPricing]] = Field(description="The pricing of every available chat model.")
    embedding: Optional[List[AiEmbeddingModelPricing]] = Field(description="The pricing of every available embedding model.")
    image: Optional[List[AiImageModelPricing]] = Field(description="The pricing of every available image model.")
    search: Optional[List[AiWebSearchPricing]] = Field(description="The pricing of every available web search provider.")
    currency: CurrencyInfo = Field(description="The currency the AI prices are quoted in.")
    __properties: ClassVar[List[str]] = ["chat", "embedding", "image", "search", "currency"]

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
        """Create an instance of AiPricesResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in chat (list)
        _items = []
        if self.chat:
            for _item_chat in self.chat:
                if _item_chat:
                    _items.append(_item_chat.to_dict())
            _dict['chat'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in embedding (list)
        _items = []
        if self.embedding:
            for _item_embedding in self.embedding:
                if _item_embedding:
                    _items.append(_item_embedding.to_dict())
            _dict['embedding'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in image (list)
        _items = []
        if self.image:
            for _item_image in self.image:
                if _item_image:
                    _items.append(_item_image.to_dict())
            _dict['image'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in search (list)
        _items = []
        if self.search:
            for _item_search in self.search:
                if _item_search:
                    _items.append(_item_search.to_dict())
            _dict['search'] = _items
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # set to None if chat (nullable) is None
        # and model_fields_set contains the field
        if self.chat is None and "chat" in self.model_fields_set:
            _dict['chat'] = None

        # set to None if embedding (nullable) is None
        # and model_fields_set contains the field
        if self.embedding is None and "embedding" in self.model_fields_set:
            _dict['embedding'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if search (nullable) is None
        # and model_fields_set contains the field
        if self.search is None and "search" in self.model_fields_set:
            _dict['search'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiPricesResponse from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chat": [AiChatModelPricing.from_dict(_item) for _item in obj["chat"]] if obj.get("chat") is not None else None,
            "embedding": [AiEmbeddingModelPricing.from_dict(_item) for _item in obj["embedding"]] if obj.get("embedding") is not None else None,
            "image": [AiImageModelPricing.from_dict(_item) for _item in obj["image"]] if obj.get("image") is not None else None,
            "search": [AiWebSearchPricing.from_dict(_item) for _item in obj["search"]] if obj.get("search") is not None else None,
            "currency": CurrencyInfo.from_dict(obj["currency"]) if obj.get("currency") is not None else None
        })
        return _obj


