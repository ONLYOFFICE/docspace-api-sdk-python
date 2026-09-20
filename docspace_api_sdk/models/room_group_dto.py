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
from uuid import UUID
from docspace_api_sdk.models.file_entry_base_dto import FileEntryBaseDto
from docspace_api_sdk.models.multi_size_logo_cover import MultiSizeLogoCover
from typing import Optional, Set
from typing_extensions import Self

class RoomGroupDto(BaseModel):
    """
    A personal collection of rooms: the name and icon it was given, the account that owns it, and the rooms it gathers  at the moment it was read.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The identifier of the group, which addresses it in every other group operation and is kept for as long as the  group exists.", json_schema_extra={"examples": [42]})
    name: Optional[StrictStr] = Field(default=None, description="The name its owner gave the group, stored trimmed of surrounding spaces. Names are not unique, so two groups  of the same account can be told apart only by their identifier.", json_schema_extra={"examples": ["Client projects"]})
    icon: Optional[MultiSizeLogoCover] = Field(default=None, description="The built-in cover chosen for the group, carrying the cover identifier and its rendering in each available  size. Null when the group has no icon, either because it was never given one or because the icon was cleared  by setting it to an empty value.")
    user_id: Optional[UUID] = Field(default=None, description="The account that created the group and the only one able to read, change or delete it; for any other member of  the portal the group does not exist.", alias="userId", json_schema_extra={"examples": ["9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9"]})
    rooms: Optional[List[FileEntryBaseDto]] = Field(default=None, description="The rooms the group gathers, those stored in the portal first and those on connected third-party accounts  after them. Null when the group was asked for without its members, and an empty array when the group holds no  room the caller can still see. A room moved to the archive is left out until it is taken out of the archive.", json_schema_extra={"examples": [[{"title": "Client onboarding", "fileEntryType": 1}]]})
    total_rooms: Optional[StrictInt] = Field(default=None, description="How many rooms the group shows: the same rooms `rooms` lists, so archived ones are not counted either. It is  filled even when the rooms themselves were not asked for, which makes it the cheap way to tell an empty group  from a populated one.", alias="totalRooms", json_schema_extra={"examples": [2]})
    __properties: ClassVar[List[str]] = ["id", "name", "icon", "userId", "rooms", "totalRooms"]

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
        """Create an instance of RoomGroupDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of icon
        if self.icon:
            _dict['icon'] = self.icon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rooms (list)
        _items = []
        if self.rooms:
            for _item_rooms in self.rooms:
                if _item_rooms:
                    _items.append(_item_rooms.to_dict())
            _dict['rooms'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if rooms (nullable) is None
        # and model_fields_set contains the field
        if self.rooms is None and "rooms" in self.model_fields_set:
            _dict['rooms'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomGroupDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "icon": MultiSizeLogoCover.from_dict(obj["icon"]) if obj.get("icon") is not None else None,
            "userId": obj.get("userId"),
            "rooms": [FileEntryBaseDto.from_dict(_item) for _item in obj["rooms"]] if obj.get("rooms") is not None else None,
            "totalRooms": obj.get("totalRooms")
        })
        return _obj


