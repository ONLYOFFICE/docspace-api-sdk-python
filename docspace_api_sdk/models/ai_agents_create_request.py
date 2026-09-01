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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AiAgentsCreateRequest(BaseModel):
    """
    AiAgentsCreateRequest
    """ # noqa: E501
    profile_id: StrictStr = Field(description="Profile id bound to the agent.", alias="profileId")
    prompt: StrictStr = Field(description="Agent system prompt; stored as the room's `chatSettings.prompt`.")
    private: Optional[StrictBool] = Field(default=None, description="Whether the agent room is private.")
    share: Optional[List[Dict[str, Any]]] = Field(default=None, description="Initial share entries (`FileShareParams`).")
    attach_default_tools: Optional[StrictBool] = Field(default=None, description="Whether to attach the default DocSpace MCP tool server.", alias="attachDefaultTools")
    title: Optional[StrictStr] = Field(default=None, description="Agent (room) title.")
    quota: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Room quota in bytes.")
    indexing: Optional[StrictBool] = Field(default=None, description="Whether room content is indexed for search.")
    deny_download: Optional[StrictBool] = Field(default=None, description="Whether downloading room content is denied.", alias="denyDownload")
    lifetime: Optional[Dict[str, Any]] = Field(default=None, description="Room data lifetime policy (`RoomDataLifetimeDto`).")
    watermark: Optional[Dict[str, Any]] = Field(default=None, description="Watermark settings (`WatermarkRequestDto`).")
    logo: Optional[Dict[str, Any]] = Field(default=None, description="Room logo (`LogoRequest`).")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Room tags.")
    color: Optional[StrictStr] = Field(default=None, description="Room accent color.")
    cover: Optional[StrictStr] = Field(default=None, description="Room cover image id.")
    __properties: ClassVar[List[str]] = ["profileId", "prompt", "private", "share", "attachDefaultTools", "title", "quota", "indexing", "denyDownload", "lifetime", "watermark", "logo", "tags", "color", "cover"]

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
        """Create an instance of AiAgentsCreateRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiAgentsCreateRequest from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "profileId": obj.get("profileId"),
            "prompt": obj.get("prompt"),
            "private": obj.get("private"),
            "share": obj.get("share"),
            "attachDefaultTools": obj.get("attachDefaultTools"),
            "title": obj.get("title"),
            "quota": obj.get("quota"),
            "indexing": obj.get("indexing"),
            "denyDownload": obj.get("denyDownload"),
            "lifetime": obj.get("lifetime"),
            "watermark": obj.get("watermark"),
            "logo": obj.get("logo"),
            "tags": obj.get("tags"),
            "color": obj.get("color"),
            "cover": obj.get("cover")
        })
        return _obj


