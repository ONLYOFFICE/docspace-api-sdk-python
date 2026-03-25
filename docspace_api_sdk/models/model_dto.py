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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_chat_price import AiChatPrice
from docspace_api_sdk.models.currency_info import CurrencyInfo
from typing import Optional, Set
from typing_extensions import Self

class ModelDto(BaseModel):
    """
    The AI model information.
    """ # noqa: E501
    provider_id: Optional[StrictInt] = Field(default=None, description="The unique identifier of the AI provider that offers this model.", alias="providerId")
    provider_title: Optional[StrictStr] = Field(description="The human-readable display name of the AI provider (e.g., OpenAI, Anthropic).", alias="providerTitle")
    model_id: Optional[StrictStr] = Field(description="The model identifier as recognized by the AI provider (e.g., gpt-4o, claude-sonnet-4-20250514).", alias="modelId")
    price: Optional[AiChatPrice] = None
    currency: Optional[CurrencyInfo] = None
    __properties: ClassVar[List[str]] = ["providerId", "providerTitle", "modelId", "price", "currency"]

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
        """Create an instance of ModelDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # set to None if provider_title (nullable) is None
        # and model_fields_set contains the field
        if self.provider_title is None and "provider_title" in self.model_fields_set:
            _dict['providerTitle'] = None

        # set to None if model_id (nullable) is None
        # and model_fields_set contains the field
        if self.model_id is None and "model_id" in self.model_fields_set:
            _dict['modelId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "providerId": obj.get("providerId"),
            "providerTitle": obj.get("providerTitle"),
            "modelId": obj.get("modelId"),
            "price": AiChatPrice.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "currency": CurrencyInfo.from_dict(obj["currency"]) if obj.get("currency") is not None else None
        })
        return _obj


