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
from docspace_api_sdk.models.service_limit_dto import ServiceLimitDto
from typing import Optional, Set
from typing_extensions import Self

class ServiceLimitReportDto(BaseModel):
    """
    A page of the spending limits in force for the portal users.
    """ # noqa: E501
    collection: Optional[List[ServiceLimitDto]] = Field(default=None, description="The limits of this page, one per user; empty when no limit applies to any user or the page is past the end.", json_schema_extra={"examples": [[{"id": 42, "serviceGroupName": "ai-services", "customerAccountNumber": 12345, "scope": "Custom", "userId": "3f2504e0-4f89-11d3-9a0c-0305e82c3301", "amountValue": 40, "currency": "USD", "period": "Day", "periodEnd": "2026-10-18T23:59:59Z", "enabled": True, "created": "2026-09-01T10:30:00Z", "modified": "2026-09-15T08:00:00Z", "usage": {"periodStart": "2026-10-18T00:00:00Z", "periodEnd": "2026-10-18T23:59:59Z", "amountConsumed": 12.5, "amountAvailable": 27.5, "quantityConsumed": 0}}]]})
    offset: Optional[StrictInt] = Field(default=None, description="The number of limits skipped before this page.", json_schema_extra={"examples": [0]})
    limit: Optional[StrictInt] = Field(default=None, description="The page size the page was read with.", json_schema_extra={"examples": [25]})
    total_page: Optional[StrictInt] = Field(default=None, description="The number of pages the whole list takes at this page size.", alias="totalPage", json_schema_extra={"examples": [3]})
    current_page: Optional[StrictInt] = Field(default=None, description="The number of this page, starting from 1.", alias="currentPage", json_schema_extra={"examples": [1]})
    total_quantity: Optional[StrictInt] = Field(default=None, description="The number of users with a limit in force across all pages.", alias="totalQuantity", json_schema_extra={"examples": [60]})
    __properties: ClassVar[List[str]] = ["collection", "offset", "limit", "totalPage", "currentPage", "totalQuantity"]

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
        """Create an instance of ServiceLimitReportDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in collection (list)
        _items = []
        if self.collection:
            for _item_collection in self.collection:
                if _item_collection:
                    _items.append(_item_collection.to_dict())
            _dict['collection'] = _items
        # set to None if collection (nullable) is None
        # and model_fields_set contains the field
        if self.collection is None and "collection" in self.model_fields_set:
            _dict['collection'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ServiceLimitReportDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "collection": [ServiceLimitDto.from_dict(_item) for _item in obj["collection"]] if obj.get("collection") is not None else None,
            "offset": obj.get("offset"),
            "limit": obj.get("limit"),
            "totalPage": obj.get("totalPage"),
            "currentPage": obj.get("currentPage"),
            "totalQuantity": obj.get("totalQuantity")
        })
        return _obj


