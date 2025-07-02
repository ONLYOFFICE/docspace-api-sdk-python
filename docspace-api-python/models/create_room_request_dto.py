# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from docspace-api-python.models.file_share_params import FileShareParams
from docspace-api-python.models.logo_request import LogoRequest
from docspace-api-python.models.room_data_lifetime_dto import RoomDataLifetimeDto
from docspace-api-python.models.room_type import RoomType
from docspace-api-python.models.watermark_request_dto import WatermarkRequestDto
from typing import Optional, Set
from typing_extensions import Self

class CreateRoomRequestDto(BaseModel):
    """
    The request parameters for creating a room.
    """ # noqa: E501
    title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=170)]] = Field(description="The room name.")
    quota: Optional[StrictInt] = Field(default=None, description="The room quota.")
    indexing: Optional[StrictBool] = Field(default=None, description="Specifies whether to create a room with indexing.")
    deny_download: Optional[StrictBool] = Field(default=None, description="Specifies whether to deny downloads from the room.", alias="denyDownload")
    lifetime: Optional[RoomDataLifetimeDto] = None
    watermark: Optional[WatermarkRequestDto] = None
    logo: Optional[LogoRequest] = None
    tags: Optional[List[StrictStr]] = Field(default=None, description="The list of tags.")
    color: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=6)]] = Field(default=None, description="The room color.")
    cover: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="The room cover.")
    room_type: RoomType = Field(alias="roomType")
    private: Optional[StrictBool] = Field(default=None, description="Specifies whether the room to be created is private or not.")
    share: Optional[List[FileShareParams]] = Field(default=None, description="The collection of sharing parameters.")
    __properties: ClassVar[List[str]] = ["title", "quota", "indexing", "denyDownload", "lifetime", "watermark", "logo", "tags", "color", "cover", "roomType", "private", "share"]

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
            "share": [FileShareParams.from_dict(_item) for _item in obj["share"]] if obj.get("share") is not None else None
        })
        return _obj


