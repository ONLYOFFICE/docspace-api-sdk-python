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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from docspace_api_sdk.models.chat_settings import ChatSettings
from docspace_api_sdk.models.file_share_params import FileShareParams
from docspace_api_sdk.models.logo_request import LogoRequest
from docspace_api_sdk.models.room_data_lifetime_dto import RoomDataLifetimeDto
from docspace_api_sdk.models.room_type import RoomType
from docspace_api_sdk.models.watermark_request_dto import WatermarkRequestDto
from typing import Optional, Set
from typing_extensions import Self

class CreateRoomRequestDto(BaseModel):
    """
    The parameters of a new room in the Rooms section.
    """ # noqa: E501
    title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=170)]] = Field(description="The name of the room. It is trimmed, characters that a folder name cannot hold are replaced with underscores  and the rest is truncated, so the stored title can differ from the one sent; a blank title is rejected. Titles  are not unique, and rooms are told apart by their id.", json_schema_extra={"examples": ["Project Alpha"]})
    quota: Optional[StrictInt] = Field(default=None, description="The storage the room may take, in bytes. It is accepted only while the per-room quota feature is on for the  portal and must stay inside the portal own limit; leaving it out lets the room follow the portal default.", json_schema_extra={"examples": [1073741824]})
    indexing: Optional[StrictBool] = Field(default=None, description="Whether the room keeps a manual order of its contents. With it on every file and folder carries a position  that listings follow and that `PUT api/2.0/files/rooms/{id}/reorder` compacts; with it off the contents are  ordered by the sorting of the request.", json_schema_extra={"examples": [True]})
    deny_download: Optional[StrictBool] = Field(default=None, description="Whether members without editing rights are stopped from downloading and printing the contents of the room.  They can still open the documents in the editor.", alias="denyDownload", json_schema_extra={"examples": [False]})
    lifetime: Optional[RoomDataLifetimeDto] = Field(default=None, description="How long files may stay in the room before they are deleted automatically. The countdown starts when the  setting is saved, and leaving the field out keeps the files forever.")
    watermark: Optional[WatermarkRequestDto] = Field(default=None, description="The watermark drawn over documents opened in the room. Leaving the field out adds no watermark, and sending it  with the switch turned off removes the one the room has.")
    logo: Optional[LogoRequest] = Field(default=None, description="The picture to use as the room logo, named by the path that `POST api/2.0/files/logos` returned for an image  uploaded beforehand, plus the crop to take from it. Leaving the field out keeps the room on its cover and  colour.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="The labels to attach to the room, by name. Names the portal tag catalogue does not hold yet are added to it,  and `GET api/2.0/files/tags` lists what already exists.", json_schema_extra={"examples": [["Finance", "2026"]]})
    color: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The background colour the room is drawn with while it has no logo, as six hexadecimal digits with no leading  number sign. An empty value restores the default colour of the room type.", json_schema_extra={"examples": ["FF5733"]})
    cover: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="The picture drawn on the room while it has no logo, named by an identifier from  `GET api/2.0/files/rooms/covers`. Any other value is rejected, and an empty value leaves the room without a  cover.", json_schema_extra={"examples": ["bookmark"]})
    room_type: RoomType = Field(description="What the room is for. It decides which sharing links, roles and form features the room offers, and it cannot  be changed once the room exists, so a room of the wrong kind has to be recreated.", alias="roomType")
    private: Optional[StrictBool] = Field(default=None, description="Whether the room is end-to-end encrypted. Its files can then be opened only in the desktop application by  members whose encryption keys are set up, and the flag cannot be changed after the room is created.", json_schema_extra={"examples": [False]})
    share: Optional[List[FileShareParams]] = Field(default=None, description="Not implemented on room creation: any non-empty value is rejected, and members are invited afterwards with  `PUT api/2.0/files/rooms/{id}/share`.", json_schema_extra={"examples": [[]]})
    chat_settings: Optional[ChatSettings] = Field(default=None, description="The model and the prompt an AI room answers with. It belongs to AI rooms only and is rejected for a room of  any other kind.", alias="chatSettings")
    send_form_to_external_db: Optional[StrictBool] = Field(default=None, description="For a form filling room, whether the data of every completed submission is also pushed to the external  database configured for the portal. It is what `POST api/2.0/files/rooms/{id}/externaldbsync` re-runs for the  forms already collected.", alias="sendFormToExternalDB", json_schema_extra={"examples": [False]})
    save_form_as_xlsx: Optional[StrictBool] = Field(default=None, description="For a form filling room, whether the collected submissions are also gathered into a spreadsheet stored next to  the completed forms. With it off the submissions are kept only as the filled documents themselves.", alias="saveFormAsXLSX", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["title", "quota", "indexing", "denyDownload", "lifetime", "watermark", "logo", "tags", "color", "cover", "roomType", "private", "share", "chatSettings", "sendFormToExternalDB", "saveFormAsXLSX"]

    @field_validator('color')
    def color_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-fA-F]{6}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-fA-F]{6}$/")
        return value

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
        """Create an instance of CreateRoomRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of lifetime
        if self.lifetime:
            _dict['lifetime'] = self.lifetime.to_dict()
        # override the default output from pydantic by calling `to_dict()` of watermark
        if self.watermark:
            _dict['watermark'] = self.watermark.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in share (list)
        _items = []
        if self.share:
            for _item_share in self.share:
                if _item_share:
                    _items.append(_item_share.to_dict())
            _dict['share'] = _items
        # override the default output from pydantic by calling `to_dict()` of chat_settings
        if self.chat_settings:
            _dict['chatSettings'] = self.chat_settings.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if quota (nullable) is None
        # and model_fields_set contains the field
        if self.quota is None and "quota" in self.model_fields_set:
            _dict['quota'] = None

        # set to None if indexing (nullable) is None
        # and model_fields_set contains the field
        if self.indexing is None and "indexing" in self.model_fields_set:
            _dict['indexing'] = None

        # set to None if deny_download (nullable) is None
        # and model_fields_set contains the field
        if self.deny_download is None and "deny_download" in self.model_fields_set:
            _dict['denyDownload'] = None

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

        # set to None if share (nullable) is None
        # and model_fields_set contains the field
        if self.share is None and "share" in self.model_fields_set:
            _dict['share'] = None

        # set to None if send_form_to_external_db (nullable) is None
        # and model_fields_set contains the field
        if self.send_form_to_external_db is None and "send_form_to_external_db" in self.model_fields_set:
            _dict['sendFormToExternalDB'] = None

        # set to None if save_form_as_xlsx (nullable) is None
        # and model_fields_set contains the field
        if self.save_form_as_xlsx is None and "save_form_as_xlsx" in self.model_fields_set:
            _dict['saveFormAsXLSX'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateRoomRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "quota": obj.get("quota"),
            "indexing": obj.get("indexing"),
            "denyDownload": obj.get("denyDownload"),
            "lifetime": RoomDataLifetimeDto.from_dict(obj["lifetime"]) if obj.get("lifetime") is not None else None,
            "watermark": WatermarkRequestDto.from_dict(obj["watermark"]) if obj.get("watermark") is not None else None,
            "logo": LogoRequest.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "tags": obj.get("tags"),
            "color": obj.get("color"),
            "cover": obj.get("cover"),
            "roomType": obj.get("roomType"),
            "private": obj.get("private"),
            "share": [FileShareParams.from_dict(_item) for _item in obj["share"]] if obj.get("share") is not None else None,
            "chatSettings": ChatSettings.from_dict(obj["chatSettings"]) if obj.get("chatSettings") is not None else None,
            "sendFormToExternalDB": obj.get("sendFormToExternalDB"),
            "saveFormAsXLSX": obj.get("saveFormAsXLSX")
        })
        return _obj


