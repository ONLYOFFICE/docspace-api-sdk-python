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
from docspace_api_sdk.models.feature_used_dto import FeatureUsedDto
from typing import Optional, Set
from typing_extensions import Self

class TenantQuotaFeatureDto(BaseModel):
    """
    One feature a quota switches on, with the limit it grants and how much of that limit is used.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The stable key of the feature - `total_size`, `manager`, `room`, `backup` and so on. It is the value to  branch on, since `title` is prose in the portal language.", json_schema_extra={"examples": ["total_size"]})
    title: Optional[StrictStr] = Field(default=None, description="The feature described in the portal language, with its limit already substituted into the sentence, so it  can be printed as it is. It is empty when this build ships no wording for the feature.", json_schema_extra={"examples": ["Premium Storage"]})
    image: Optional[StrictStr] = Field(default=None, description="The feature's icon as SVG markup to render inline - not a URL to fetch. It is filled in only when the  quota comes from the catalogue, and left empty on the quota the portal is actually on, on a feature that  this quota switches off, and on a feature that ships no icon.", json_schema_extra={"examples": ["<svg viewBox=\"0 0 24 24\"><path d=\"...\"/></svg>"]})
    value: Optional[Any] = None
    type: Optional[StrictStr] = Field(default=None, description="How to read `value` and `used`: `size` for bytes, `count` for a number of things, `flag` for a feature  that is merely on or off.", json_schema_extra={"examples": ["size"]})
    used: Optional[FeatureUsedDto] = Field(default=None, description="How much of the limit is already used. It is present only on the quota the portal is actually on, and  only for a feature whose consumption is counted; a guest is shown none of these figures and a plain member  only the one for total size, so an absent value can mean the caller may not see it rather than that  nothing is used.")
    price_title: Optional[StrictStr] = Field(default=None, description="What the feature is charged as, in the portal language - for instance the per-unit price of an add-on. It  is filled in only for a feature that costs money on top of the plan.", alias="priceTitle", json_schema_extra={"examples": ["$9.99/month"]})
    __properties: ClassVar[List[str]] = ["id", "title", "image", "value", "type", "used", "priceTitle"]

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
        """Create an instance of TenantQuotaFeatureDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of used
        if self.used:
            _dict['used'] = self.used.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if price_title (nullable) is None
        # and model_fields_set contains the field
        if self.price_title is None and "price_title" in self.model_fields_set:
            _dict['priceTitle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TenantQuotaFeatureDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "image": obj.get("image"),
            "value": obj.get("value"),
            "type": obj.get("type"),
            "used": FeatureUsedDto.from_dict(obj["used"]) if obj.get("used") is not None else None,
            "priceTitle": obj.get("priceTitle")
        })
        return _obj


