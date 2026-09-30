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
from docspace_api_sdk.models.ai_entry_pricing_dto_ai_chat_price_dto import AiEntryPricingDtoAiChatPriceDto
from docspace_api_sdk.models.ai_entry_pricing_dto_ai_embedding_price_dto import AiEntryPricingDtoAiEmbeddingPriceDto
from docspace_api_sdk.models.ai_entry_pricing_dto_ai_image_price_dto import AiEntryPricingDtoAiImagePriceDto
from docspace_api_sdk.models.ai_entry_pricing_dto_decimal import AiEntryPricingDtoDecimal
from docspace_api_sdk.models.currency_info import CurrencyInfo
from typing import Optional, Set
from typing_extensions import Self

class AiPricesDto(BaseModel):
    """
    What the AI features cost out of the portal wallet, grouped by the kind of model, in one currency.
    """ # noqa: E501
    chat: Optional[List[AiEntryPricingDtoAiChatPriceDto]] = Field(description="The chat models on offer, each priced per million prompt and completion tokens. A model listed here is one  the installation can bill for, not necessarily one this portal may use -  `GET api/2.0/portal/payment/ai-model/restrictions` says which are allowed.", json_schema_extra={"examples": [[{"id": "gpt-4o", "alias": "GPT-4o", "provider": "openai", "image": "https://cdn.example.com/providers/openai.png", "price": {"prompt": 5.0, "completion": 15.0}}]]})
    embedding: Optional[List[AiEntryPricingDtoAiEmbeddingPriceDto]] = Field(description="The embedding models on offer, priced per million tokens of input; an embedding model has no completion  side, so its price object carries `prompt` alone.", json_schema_extra={"examples": [[{"id": "text-embedding-3-large", "alias": "Text Embedding 3 Large", "provider": "openai", "image": "https://cdn.example.com/providers/openai.png", "price": {"prompt": 0.13}}]]})
    image: Optional[List[AiEntryPricingDtoAiImagePriceDto]] = Field(description="The image models on offer, priced per million prompt and completion tokens plus a price for each image  produced.", json_schema_extra={"examples": [[{"id": "gpt-5.4-image-2", "alias": "GPT 5.4 Image 2", "provider": "OpenRouter", "image": "https://cdn.example.com/providers/openai.png", "price": {"prompt": 8.0, "completion": 15.0, "image": 30.0}}]]})
    web_search: Optional[List[AiEntryPricingDtoDecimal]] = Field(description="The web search providers on offer. Their `price` is a bare number - the cost of one search - rather than  an object, because there are no tokens to distinguish.", alias="webSearch", json_schema_extra={"examples": [[{"id": "web-search", "alias": "Web Search", "provider": "tavily", "image": "https://cdn.example.com/providers/tavily.png", "price": 0.01}]]})
    currency: CurrencyInfo = Field(description="The currency every price above is expressed in, with its ISO code and symbol. One answer never mixes  currencies, so this is the only place to read it.")
    __properties: ClassVar[List[str]] = ["chat", "embedding", "image", "webSearch", "currency"]

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
        """Create an instance of AiPricesDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in web_search (list)
        _items = []
        if self.web_search:
            for _item_web_search in self.web_search:
                if _item_web_search:
                    _items.append(_item_web_search.to_dict())
            _dict['webSearch'] = _items
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

        # set to None if web_search (nullable) is None
        # and model_fields_set contains the field
        if self.web_search is None and "web_search" in self.model_fields_set:
            _dict['webSearch'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiPricesDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chat": [AiEntryPricingDtoAiChatPriceDto.from_dict(_item) for _item in obj["chat"]] if obj.get("chat") is not None else None,
            "embedding": [AiEntryPricingDtoAiEmbeddingPriceDto.from_dict(_item) for _item in obj["embedding"]] if obj.get("embedding") is not None else None,
            "image": [AiEntryPricingDtoAiImagePriceDto.from_dict(_item) for _item in obj["image"]] if obj.get("image") is not None else None,
            "webSearch": [AiEntryPricingDtoDecimal.from_dict(_item) for _item in obj["webSearch"]] if obj.get("webSearch") is not None else None,
            "currency": CurrencyInfo.from_dict(obj["currency"]) if obj.get("currency") is not None else None
        })
        return _obj


