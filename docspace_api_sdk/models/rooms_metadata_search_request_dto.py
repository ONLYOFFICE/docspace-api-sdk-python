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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from docspace_api_sdk.models.metadata_filter_condition_request import MetadataFilterConditionRequest
from docspace_api_sdk.models.room_type import RoomType
from docspace_api_sdk.models.search_area import SearchArea
from docspace_api_sdk.models.sort_order import SortOrder
from typing import Optional, Set
from typing_extensions import Self

class RoomsMetadataSearchRequestDto(BaseModel):
    """
    The typed form of the metadata search of the rooms: the same filter the rooms listing takes in the metadataTemplateId  and metadataFilters query parameters, with the conditions as objects instead of a JSON string.
    """ # noqa: E501
    metadata_template_id: Optional[StrictInt] = Field(default=None, description="The ID of the metadata template the rooms must be assigned to. On its own it narrows the listing to the rooms  carrying the template; together with the conditions it also pins the template the filtered fields belong to.", alias="metadataTemplateId", json_schema_extra={"examples": [1]})
    metadata_filters: Optional[List[MetadataFilterConditionRequest]] = Field(default=None, description="The metadata filter conditions, combined with AND. A custom field is addressed by its name instead of the field ID.", alias="metadataFilters", json_schema_extra={"examples": [[{"fieldId": 1, "op": "eq", "value": "ACME"}, {"name": "Client", "op": "eq", "value": "ACME"}]]})
    include_hidden_metadata: Optional[StrictBool] = Field(default=None, description="Whether the text search, and the metadataMatches it reports, also look at the values of the hidden metadata  templates (created with visible false for the metadata a service keeps for itself, which the web client never  shows). False, the default, leaves them out, so an entry is not found by such a value; true takes them in.  metadataTemplateId and metadataFilters are not concerned: a hidden template or field named there is searched  either way.", alias="includeHiddenMetadata", json_schema_extra={"examples": [False]})
    filter_value: Optional[StrictStr] = Field(default=None, description="The text to search for in the room titles and in the string metadata values of the rooms, the custom fields and  the template fields alike; a room found by its metadata says where in metadataMatches.", alias="filterValue", json_schema_extra={"examples": ["ACME"]})
    search_area: Optional[SearchArea] = Field(default=None, description="The section to search in: the active rooms (the default), the archive or the templates.", alias="searchArea")
    type: Optional[List[RoomType]] = Field(default=None, description="The room types to search among.", json_schema_extra={"examples": [[5]]})
    count: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = Field(default=None, description="The number of rooms to return, from 1 to 100.", json_schema_extra={"examples": [25]})
    start_index: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(default=None, description="The zero-based index of the first room to return.", alias="startIndex", json_schema_extra={"examples": [0]})
    sort_by: Optional[StrictStr] = Field(default=None, description="The field to sort by, a name of the SortedByType values.", alias="sortBy", json_schema_extra={"examples": ["DateAndTime"]})
    sort_order: Optional[SortOrder] = Field(default=None, description="The sort order.", alias="sortOrder")
    __properties: ClassVar[List[str]] = ["metadataTemplateId", "metadataFilters", "includeHiddenMetadata", "filterValue", "searchArea", "type", "count", "startIndex", "sortBy", "sortOrder"]

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
        """Create an instance of RoomsMetadataSearchRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metadata_filters (list)
        _items = []
        if self.metadata_filters:
            for _item_metadata_filters in self.metadata_filters:
                if _item_metadata_filters:
                    _items.append(_item_metadata_filters.to_dict())
            _dict['metadataFilters'] = _items
        # set to None if metadata_template_id (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_template_id is None and "metadata_template_id" in self.model_fields_set:
            _dict['metadataTemplateId'] = None

        # set to None if metadata_filters (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_filters is None and "metadata_filters" in self.model_fields_set:
            _dict['metadataFilters'] = None

        # set to None if include_hidden_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.include_hidden_metadata is None and "include_hidden_metadata" in self.model_fields_set:
            _dict['includeHiddenMetadata'] = None

        # set to None if filter_value (nullable) is None
        # and model_fields_set contains the field
        if self.filter_value is None and "filter_value" in self.model_fields_set:
            _dict['filterValue'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if sort_by (nullable) is None
        # and model_fields_set contains the field
        if self.sort_by is None and "sort_by" in self.model_fields_set:
            _dict['sortBy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomsMetadataSearchRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadataTemplateId": obj.get("metadataTemplateId"),
            "metadataFilters": [MetadataFilterConditionRequest.from_dict(_item) for _item in obj["metadataFilters"]] if obj.get("metadataFilters") is not None else None,
            "includeHiddenMetadata": obj.get("includeHiddenMetadata"),
            "filterValue": obj.get("filterValue"),
            "searchArea": obj.get("searchArea"),
            "type": obj.get("type"),
            "count": obj.get("count"),
            "startIndex": obj.get("startIndex"),
            "sortBy": obj.get("sortBy"),
            "sortOrder": obj.get("sortOrder")
        })
        return _obj


