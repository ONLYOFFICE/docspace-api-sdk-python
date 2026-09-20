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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AiEntryPricingDtoDecimal(BaseModel):
    """
    One AI model or service on the price list: how to name it, who provides it, and what it costs.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(description="The model identifier to send to the AI operations. It is the value to branch on, while `alias` is for display  only.", json_schema_extra={"examples": ["gpt-4o"]})
    alias: Optional[StrictStr] = Field(description="The model name as the vendor writes it, meant to be shown to a person rather than matched on.", json_schema_extra={"examples": ["GPT-4o"]})
    provider: Optional[StrictStr] = Field(description="Who runs the model. Two entries can share a provider, and one provider's models can be priced quite  differently, so the price always belongs to the entry and never to the provider.", json_schema_extra={"examples": ["openai"]})
    image: Optional[StrictStr] = Field(description="The absolute URL of the provider's icon, for rendering next to the entry.", json_schema_extra={"examples": ["https://cdn.example.com/providers/openai.png"]})
    price: Union[StrictFloat, StrictInt] = Field(description="What the entry costs, in the currency the answer names. Amounts per token are normalised per million  tokens, so they are not the price of a single call.", json_schema_extra={"examples": [{"prompt": 5.0, "completion": 15.0}]})
    link: Optional[StrictStr] = Field(description="The provider's own page for the model, for a person to read the model's terms. It is empty when the  provider publishes none.", json_schema_extra={"examples": ["https://openai.com/pricing"]})
    __properties: ClassVar[List[str]] = ["id", "alias", "provider", "image", "price", "link"]

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
        """Create an instance of AiEntryPricingDtoDecimal from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if alias (nullable) is None
        # and model_fields_set contains the field
        if self.alias is None and "alias" in self.model_fields_set:
            _dict['alias'] = None

        # set to None if provider (nullable) is None
        # and model_fields_set contains the field
        if self.provider is None and "provider" in self.model_fields_set:
            _dict['provider'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiEntryPricingDtoDecimal from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "alias": obj.get("alias"),
            "provider": obj.get("provider"),
            "image": obj.get("image"),
            "price": obj.get("price"),
            "link": obj.get("link")
        })
        return _obj


