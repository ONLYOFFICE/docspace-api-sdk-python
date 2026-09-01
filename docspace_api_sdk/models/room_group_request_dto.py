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
from typing_extensions import Annotated
from docspace_api_sdk.models.duplicate_request_dto_all_of_file_ids import DuplicateRequestDtoAllOfFileIds
from typing import Optional, Set
from typing_extensions import Self

class RoomGroupRequestDto(BaseModel):
    """
    The request parameters for creating a room group
    """ # noqa: E501
    name: Annotated[str, Field(min_length=0, strict=True, max_length=128)] = Field(description="Group name", json_schema_extra={"examples": ["My Group"]})
    icon: Annotated[str, Field(min_length=0, strict=True, max_length=50)] = Field(description="Group icon", json_schema_extra={"examples": ["cover1"]})
    rooms: List[DuplicateRequestDtoAllOfFileIds] = Field(description="The list of room IDs.", json_schema_extra={"examples": [[1, 2, 3]]})
    __properties: ClassVar[List[str]] = ["name", "icon", "rooms"]

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
        """Create an instance of RoomGroupRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rooms (list)
        _items = []
        if self.rooms:
            for _item_rooms in self.rooms:
                if _item_rooms:
                    _items.append(_item_rooms.to_dict())
            _dict['rooms'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomGroupRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "icon": obj.get("icon"),
            "rooms": [DuplicateRequestDtoAllOfFileIds.from_dict(_item) for _item in obj["rooms"]] if obj.get("rooms") is not None else None
        })
        return _obj


