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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.logo_request import LogoRequest
from docspace_api_sdk.models.room_type import RoomType
from typing import Optional, Set
from typing_extensions import Self

class CreateThirdPartyRoom(BaseModel):
    """
    The room to be created out of a folder of a connected third-party storage account.
    """ # noqa: E501
    create_as_new_folder: Optional[StrictBool] = Field(default=None, description="Creates a new folder named after `title` inside the folder named in the path and turns that subfolder into the  room, leaving the named folder itself untouched. When omitted, the named folder becomes the room and keeps  everything it already holds.", alias="createAsNewFolder", json_schema_extra={"examples": [False]})
    title: Optional[StrictStr] = Field(description="The name the room is shown under. It is stored on the connected account, so it does not have to match the name  of the folder in the storage; with `createAsNewFolder` it is also the name given to the created subfolder.", json_schema_extra={"examples": ["Third-party project room"]})
    room_type: RoomType = Field(description="The kind of room the folder becomes, which decides the default access rules of its members and cannot be  changed afterwards.", alias="roomType")
    private: Optional[StrictBool] = Field(default=None, description="Restricts the room to the members explicitly invited into it. The flag is kept on the connected storage  account rather than on the folder, so every folder read through that account reports the same value.", json_schema_extra={"examples": [False]})
    indexing: Optional[StrictBool] = Field(default=None, description="Keeps the contents of the room in an explicit numbered order, the one reported as `order` on every entry,  instead of leaving the order to the reader.", json_schema_extra={"examples": [True]})
    deny_download: Optional[StrictBool] = Field(default=None, description="Forbids downloading and printing the contents of the room, which leaves the members with viewing and editing  in the editor only.", alias="denyDownload", json_schema_extra={"examples": [False]})
    color: Optional[StrictStr] = Field(default=None, description="The background colour drawn behind the cover of the room, as six hexadecimal digits without a leading number  sign. An empty value restores the colour the portal picks by default.", json_schema_extra={"examples": ["FF5733"]})
    cover: Optional[StrictStr] = Field(default=None, description="The drawing shown on the room tile, named by one of the built-in cover identifiers returned by  `GET api/2.0/files/rooms/covers`. An empty value leaves the room without a cover, and any other unknown value  is rejected as an invalid request.", json_schema_extra={"examples": ["bookmark"]})
    tags: Optional[List[StrictStr]] = Field(default=None, description="The tags to attach to the room, named by their text. A name that is not in the portal tag catalogue yet is  added to it, and `GET api/2.0/files/tags` lists the names already there.", json_schema_extra={"examples": [["Marketing", "Q3"]]})
    logo: Optional[LogoRequest] = Field(default=None, description="The picture to use as the room logo, which has to be uploaded with `POST api/2.0/files/logos` first; leaving  it out keeps the room on its cover and colour.")
    __properties: ClassVar[List[str]] = ["createAsNewFolder", "title", "roomType", "private", "indexing", "denyDownload", "color", "cover", "tags", "logo"]

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
        """Create an instance of CreateThirdPartyRoom from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if color (nullable) is None
        # and model_fields_set contains the field
        if self.color is None and "color" in self.model_fields_set:
            _dict['color'] = None

        # set to None if cover (nullable) is None
        # and model_fields_set contains the field
        if self.cover is None and "cover" in self.model_fields_set:
            _dict['cover'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateThirdPartyRoom from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createAsNewFolder": obj.get("createAsNewFolder"),
            "title": obj.get("title"),
            "roomType": obj.get("roomType"),
            "private": obj.get("private"),
            "indexing": obj.get("indexing"),
            "denyDownload": obj.get("denyDownload"),
            "color": obj.get("color"),
            "cover": obj.get("cover"),
            "tags": obj.get("tags"),
            "logo": LogoRequest.from_dict(obj["logo"]) if obj.get("logo") is not None else None
        })
        return _obj


