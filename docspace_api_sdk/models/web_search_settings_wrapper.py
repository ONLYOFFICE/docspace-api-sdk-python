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
from docspace_api_sdk.models.get_portal_prices200_response_links_inner import GetPortalPrices200ResponseLinksInner
from docspace_api_sdk.models.web_search_settings_dto import WebSearchSettingsDto
from typing import Optional, Set
from typing_extensions import Self

class WebSearchSettingsWrapper(BaseModel):
    """
    WebSearchSettingsWrapper
    """ # noqa: E501
    response: Optional[WebSearchSettingsDto] = None
    count: Optional[StrictInt] = Field(default=None, description="The total number of items in the response")
    links: Optional[List[GetPortalPrices200ResponseLinksInner]] = Field(default=None, description="List of links related to the response")
    status: Optional[StrictInt] = Field(default=None, description="HTTP status code of the response")
    status_code: Optional[StrictInt] = Field(default=None, description="HTTP status code of the response (duplicate of status)", alias="statusCode")
    __properties: ClassVar[List[str]] = ["response", "count", "links", "status", "statusCode"]

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
        """Create an instance of WebSearchSettingsWrapper from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of response
        if self.response:
            _dict['response'] = self.response.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebSearchSettingsWrapper from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "response": WebSearchSettingsDto.from_dict(obj["response"]) if obj.get("response") is not None else None,
            "count": obj.get("count"),
            "links": [GetPortalPrices200ResponseLinksInner.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "status": obj.get("status"),
            "statusCode": obj.get("statusCode")
        })
        return _obj


