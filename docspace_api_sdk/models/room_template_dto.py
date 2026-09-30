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
from uuid import UUID
from docspace_api_sdk.models.logo_request import LogoRequest
from typing import Optional, Set
from typing_extensions import Self

class RoomTemplateDto(BaseModel):
    """
    The parameters of a room template built from an existing room.
    """ # noqa: E501
    room_id: StrictInt = Field(description="The identifier of the room the template is built from. Take it from the room listing of  `GET api/2.0/files/rooms`; a folder identifier is not accepted.", alias="roomId", json_schema_extra={"examples": [1234]})
    title: Annotated[str, Field(min_length=0, strict=True, max_length=400)] = Field(description="The title the template is saved under in the Templates section. Characters that a folder name cannot contain  are replaced with an underscore on save, and two templates may share a title.", json_schema_extra={"examples": ["Sales agreement room"]})
    logo: Optional[LogoRequest] = Field(default=None, description="A picture of the caller's own for the template, cropped out of an image already placed in the temporary  storage.")
    copy_logo: Optional[StrictBool] = Field(default=None, description="Whether the template takes over the picture already set on the source room. When false the template gets no  picture from that room.", alias="copyLogo", json_schema_extra={"examples": [True]})
    share: Optional[List[StrictStr]] = Field(default=None, description="The email addresses of the portal members who are granted read access to the finished template.", json_schema_extra={"examples": [["user1@example.com", "user2@example.com"]]})
    groups: Optional[List[UUID]] = Field(default=None, description="The identifiers of the portal groups whose members are granted read access to the finished template.", json_schema_extra={"examples": [["9924256a-739c-462b-af15-e652a3b1b6eb"]]})
    public: Optional[StrictBool] = Field(default=None, description="Whether the finished template is shared with everyone allowed to create rooms. When false it stays reachable  only for the recipients named for it.", json_schema_extra={"examples": [True]})
    tags: Optional[List[StrictStr]] = Field(default=None, description="The labels attached to the template and shown next to it in listings.", json_schema_extra={"examples": [["Contracts", "Sales"]]})
    color: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=6)]] = Field(default=None, description="The accent colour of the generated cover, written as six hexadecimal digits with no leading hash sign. When it  is left empty a colour is picked at random.", json_schema_extra={"examples": ["FF5733"]})
    cover: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="The identifier of a built-in cover picture, as listed by `GET api/2.0/files/rooms/covers`. When it is left  empty the template gets no cover.", json_schema_extra={"examples": ["bookmark"]})
    quota: Optional[StrictInt] = Field(default=None, description="The storage limit assigned to the template, in bytes. When it is not set the template keeps the limit of the  source room.", json_schema_extra={"examples": [10485760]})
    __properties: ClassVar[List[str]] = ["roomId", "title", "logo", "copyLogo", "share", "groups", "public", "tags", "color", "cover", "quota"]

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
        """Create an instance of RoomTemplateDto from a JSON string"""
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
        # set to None if share (nullable) is None
        # and model_fields_set contains the field
        if self.share is None and "share" in self.model_fields_set:
            _dict['share'] = None

        # set to None if groups (nullable) is None
        # and model_fields_set contains the field
        if self.groups is None and "groups" in self.model_fields_set:
            _dict['groups'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if color (nullable) is None
        # and model_fields_set contains the field
        if self.color is None and "color" in self.model_fields_set:
            _dict['color'] = None

        # set to None if cover (nullable) is None
        # and model_fields_set contains the field
        if self.cover is None and "cover" in self.model_fields_set:
            _dict['cover'] = None

        # set to None if quota (nullable) is None
        # and model_fields_set contains the field
        if self.quota is None and "quota" in self.model_fields_set:
            _dict['quota'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomTemplateDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "roomId": obj.get("roomId"),
            "title": obj.get("title"),
            "logo": LogoRequest.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "copyLogo": obj.get("copyLogo"),
            "share": obj.get("share"),
            "groups": obj.get("groups"),
            "public": obj.get("public"),
            "tags": obj.get("tags"),
            "color": obj.get("color"),
            "cover": obj.get("cover"),
            "quota": obj.get("quota")
        })
        return _obj


