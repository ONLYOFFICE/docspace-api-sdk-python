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
    The request parameters for creating a room.
    """ # noqa: E501
    title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=170)]] = Field(description="The room name.", json_schema_extra={"examples": ["My Room"]})
    quota: Optional[StrictInt] = Field(default=None, description="The room quota.", json_schema_extra={"examples": [1073741824]})
    indexing: Optional[StrictBool] = Field(default=None, description="Specifies whether to create a room with indexing.", json_schema_extra={"examples": [True]})
    deny_download: Optional[StrictBool] = Field(default=None, description="Specifies whether to deny downloads from the room.", alias="denyDownload", json_schema_extra={"examples": [False]})
    lifetime: Optional[RoomDataLifetimeDto] = Field(default=None, description="The room data lifetime information.")
    watermark: Optional[WatermarkRequestDto] = Field(default=None, description="The request parameters for adding watermarks.")
    logo: Optional[LogoRequest] = Field(default=None, description="The logo request parameters.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="The list of tags.", json_schema_extra={"examples": [["tag1", "tag2", "tag3"]]})
    color: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The room color, as a six-digit hexadecimal value without a leading '#'.", json_schema_extra={"examples": ["FF0000"]})
    cover: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="The room cover.", json_schema_extra={"examples": ["cover1.jpg"]})
    room_type: RoomType = Field(description="The room type.", alias="roomType")
    private: Optional[StrictBool] = Field(default=None, description="Specifies whether the room to be created is private or not.", json_schema_extra={"examples": [False]})
    share: Optional[List[FileShareParams]] = Field(default=None, description="The collection of sharing parameters.", json_schema_extra={"examples": [[{"access": 1, "shareTo": "00000000-0000-0000-0000-000000000000"}]]})
    chat_settings: Optional[ChatSettings] = Field(default=None, description="The chat settings.", alias="chatSettings")
    send_form_to_external_db: Optional[StrictBool] = Field(default=None, description="Specifies whether to send form data to external database.", alias="sendFormToExternalDB", json_schema_extra={"examples": [False]})
    save_form_as_xlsx: Optional[StrictBool] = Field(default=None, description="Specifies whether to save form data as XLSX file.", alias="saveFormAsXLSX", json_schema_extra={"examples": [False]})
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


