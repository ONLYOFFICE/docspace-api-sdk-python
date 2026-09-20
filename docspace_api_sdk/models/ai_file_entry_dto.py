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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_api_date_time import AiApiDateTime
from docspace_api_sdk.models.ai_employee_dto import AiEmployeeDto
from docspace_api_sdk.models.ai_file_entry_dto_all_of_available_share_rights import AiFileEntryDtoAllOfAvailableShareRights
from docspace_api_sdk.models.ai_file_entry_dto_all_of_security import AiFileEntryDtoAllOfSecurity
from docspace_api_sdk.models.ai_file_entry_dto_all_of_share_settings import AiFileEntryDtoAllOfShareSettings
from docspace_api_sdk.models.ai_file_entry_type import AiFileEntryType
from docspace_api_sdk.models.ai_file_share import AiFileShare
from docspace_api_sdk.models.ai_folder_type import AiFolderType
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field
from docspace_api_sdk.models.ai_file_entry_base_dto import AiFileEntryBaseDto

class AiFileEntryDto(AiFileEntryBaseDto):
    """
    The part of a file or folder that depends on how the entry is identified: by a number on the portal, or by a  string on a connected third-party account.
    """

    id: Optional[StrictInt] = Field(default=None, description="The identifier to pass back to the other operations of this entry. It is a number for storage on the portal  and a string for a connected third-party account, and it is unique only within its own kind, so files and  folders may carry the same value.", json_schema_extra={"examples": [10]})
    root_folder_id: Optional[StrictInt] = Field(default=None, description="The section the entry ultimately lies in, as an identifier that can be listed like any other folder. For an  entry inside a room this is the rooms section, not the room.", alias="rootFolderId", json_schema_extra={"examples": [1]})
    origin_id: Optional[StrictInt] = Field(default=None, description="The folder the entry was deleted from, which is where restoring it puts it back. It is left out of the answer  unless the entry is in the trash.", alias="originId", json_schema_extra={"examples": [12]})
    origin_room_id: Optional[StrictInt] = Field(default=None, description="The room the entry was deleted from, left out of the answer for anything that was not deleted out of a room.", alias="originRoomId", json_schema_extra={"examples": [22]})
    origin_title: Optional[StrictStr] = Field(default=None, description="The name of the folder the entry was deleted from, for showing where it would be restored to. It is null for  an entry that is not in the trash.", alias="originTitle", json_schema_extra={"examples": ["Contracts"]})
    origin_room_title: Optional[StrictStr] = Field(default=None, description="The name of the room the entry was deleted from, null for anything that was not deleted out of a room.", alias="originRoomTitle", json_schema_extra={"examples": ["Legal team"]})
    can_share: Optional[StrictBool] = Field(default=None, description="Whether the calling account may change who has access to the entry, and so whether offering a sharing dialog  for it makes sense. It is false in rooms whose access is fixed by the room itself, such as a private one, even  for its manager.", alias="canShare", json_schema_extra={"examples": [True]})
    share_settings: Optional[AiFileEntryDtoAllOfShareSettings] = Field(default=None, alias="shareSettings")
    security: Optional[AiFileEntryDtoAllOfSecurity] = None
    available_share_rights: Optional[AiFileEntryDtoAllOfAvailableShareRights] = Field(default=None, alias="availableShareRights")
    request_token: Optional[StrictStr] = Field(default=None, description="The token of the link the entry is being read through, which is the value the external-share operations expect  and which also has to be carried by the download and preview addresses. It is null whenever the entry is not  being read through a link.", alias="requestToken", json_schema_extra={"examples": ["q7Ry8cQ1lZ0dP3sK2mXfA9tBnV6hJ4uE8wCz5oLg"]})
    external: Optional[StrictBool] = Field(default=None, description="Set when the link being used was made for this very entry, and false when the entry is reached through a link  to the room around it. It is null when no link is involved.", json_schema_extra={"examples": [False]})
    expiration_date: Optional[AiApiDateTime] = Field(default=None, description="When the link being used stops working, written with the offset of the portal's time zone. It is null for a  link that never expires and whenever no link is involved.", alias="expirationDate")
    is_link_expired: Optional[StrictBool] = Field(default=None, description="Set when the link being used has already passed its expiration date, which is why the entry cannot be opened  even though it is described here. It is null when no link is involved.", alias="isLinkExpired", json_schema_extra={"examples": [False]})

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
        """Create an instance of AiFileEntryDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shared_by
        if self.shared_by:
            _dict['sharedBy'] = self.shared_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owned_by
        if self.owned_by:
            _dict['ownedBy'] = self.owned_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_delete
        if self.auto_delete:
            _dict['autoDelete'] = self.auto_delete.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of share_settings
        if self.share_settings:
            _dict['shareSettings'] = self.share_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict['security'] = self.security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available_share_rights
        if self.available_share_rights:
            _dict['availableShareRights'] = self.available_share_rights.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration_date
        if self.expiration_date:
            _dict['expirationDate'] = self.expiration_date.to_dict()
        # set to None if origin_title (nullable) is None
        # and model_fields_set contains the field
        if self.origin_title is None and "origin_title" in self.model_fields_set:
            _dict['originTitle'] = None

        # set to None if origin_room_title (nullable) is None
        # and model_fields_set contains the field
        if self.origin_room_title is None and "origin_room_title" in self.model_fields_set:
            _dict['originRoomTitle'] = None

        # set to None if share_settings (nullable) is None
        # and model_fields_set contains the field
        if self.share_settings is None and "share_settings" in self.model_fields_set:
            _dict['shareSettings'] = None

        # set to None if security (nullable) is None
        # and model_fields_set contains the field
        if self.security is None and "security" in self.model_fields_set:
            _dict['security'] = None

        # set to None if available_share_rights (nullable) is None
        # and model_fields_set contains the field
        if self.available_share_rights is None and "available_share_rights" in self.model_fields_set:
            _dict['availableShareRights'] = None

        # set to None if request_token (nullable) is None
        # and model_fields_set contains the field
        if self.request_token is None and "request_token" in self.model_fields_set:
            _dict['requestToken'] = None

        # set to None if external (nullable) is None
        # and model_fields_set contains the field
        if self.external is None and "external" in self.model_fields_set:
            _dict['external'] = None

        # set to None if is_link_expired (nullable) is None
        # and model_fields_set contains the field
        if self.is_link_expired is None and "is_link_expired" in self.model_fields_set:
            _dict['isLinkExpired'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance from a dict"""
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        base_obj = super().from_dict(obj)
        base_dict = base_obj.model_dump() if hasattr(base_obj, "model_dump") else dict(base_obj or {})

        extra_fields = {
            "id": obj.get("id"),
            "rootFolderId": obj.get("rootFolderId"),
            "originId": obj.get("originId"),
            "originRoomId": obj.get("originRoomId"),
            "originTitle": obj.get("originTitle"),
            "originRoomTitle": obj.get("originRoomTitle"),
            "canShare": obj.get("canShare"),
            "shareSettings": AiFileEntryDtoAllOfShareSettings.from_dict(obj["shareSettings"]) if obj.get("shareSettings") is not None else None,
            "security": AiFileEntryDtoAllOfSecurity.from_dict(obj["security"]) if obj.get("security") is not None else None,
            "availableShareRights": AiFileEntryDtoAllOfAvailableShareRights.from_dict(obj["availableShareRights"]) if obj.get("availableShareRights") is not None else None,
            "requestToken": obj.get("requestToken"),
            "external": obj.get("external"),
            "expirationDate": AiApiDateTime.from_dict(obj["expirationDate"]) if obj.get("expirationDate") is not None else None,
            "isLinkExpired": obj.get("isLinkExpired")
        }
        all_fields = {**base_dict, **extra_fields}
        return cls.model_validate(all_fields)


