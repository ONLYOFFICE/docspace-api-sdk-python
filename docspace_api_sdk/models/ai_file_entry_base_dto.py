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
from docspace_api_sdk.models.ai_api_date_time import AiApiDateTime
from docspace_api_sdk.models.ai_employee_dto import AiEmployeeDto
from docspace_api_sdk.models.ai_file_entry_type import AiFileEntryType
from docspace_api_sdk.models.ai_file_share import AiFileShare
from docspace_api_sdk.models.ai_folder_type import AiFolderType
from typing import Optional, Set
from typing_extensions import Self

class AiFileEntryBaseDto(BaseModel):
    """
    What every file and folder in an answer has in common; the concrete shape is a file or a folder, told apart by the  entry type.
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The name shown for the entry. For a file it carries the extension, which is how the format is recognised, and  for a room it is the room name.", json_schema_extra={"examples": ["Some title.txt"]})
    access: Optional[AiFileShare] = Field(default=None, description="The level the calling account holds on this entry, resolved from its own rights, the groups it belongs to and  any link it came in through. It is the level itself, not what the account may do with it - the action flags  below answer that.")
    shared_by: Optional[AiEmployeeDto] = Field(default=None, description="Who gave the calling account the access it is using. It is filled in only while the entry is being read  through a share, and never for a caller without an account.", alias="sharedBy")
    owned_by: Optional[AiEmployeeDto] = Field(default=None, description="Who owns the place the entry is shared from - the creator of the room it lies in, or of the personal section  that holds it. It is filled in only while the entry is being read through a share, and never for a caller  without an account.", alias="ownedBy")
    shared: Optional[StrictBool] = Field(default=None, description="Whether at least one external link exists for the entry, whichever kind. It says nothing about accounts and  groups - those are counted by the flag for members below.", json_schema_extra={"examples": [False]})
    shared_for_user: Optional[StrictBool] = Field(default=None, description="Whether at least one account or group has been given rights on the entry directly, as opposed to reaching it  through a link or through the room around it.", alias="sharedForUser", json_schema_extra={"examples": [False]})
    shared_external: Optional[StrictBool] = Field(default=None, description="Whether one of the entry's links is open to people outside the portal, as opposed to a link that only its own  members can follow. This is the flag to watch when the concern is who can reach the content from outside.", alias="sharedExternal", json_schema_extra={"examples": [False]})
    parent_shared: Optional[StrictBool] = Field(default=None, description="Whether the entry is reachable because the room or folder around it is shared, rather than through rights of  its own. A copy or a move takes the entry out of that scope.", alias="parentShared", json_schema_extra={"examples": [False]})
    short_web_url: Optional[StrictStr] = Field(default=None, description="A shortened address that opens the entry through the link it is being read with. It is an empty string  whenever no link applies, which is the usual case for a member browsing their own rooms.", alias="shortWebUrl", json_schema_extra={"examples": ["http://localhost/s/abc123"]})
    created: Optional[AiApiDateTime] = Field(default=None, description="When the entry was created, written with the offset of the portal's time zone. For a file restored from an  older version this is still the moment the file first appeared.")
    created_by: Optional[AiEmployeeDto] = Field(default=None, description="Who created the entry. It is null for a caller without an account, who is told nothing about the portal's  members.", alias="createdBy")
    updated: Optional[AiApiDateTime] = Field(default=None, description="When the entry last changed, written with the offset of the portal's time zone. It is never reported as  earlier than the creation moment, so the two can be compared safely.")
    auto_delete: Optional[AiApiDateTime] = Field(default=None, description="When the entry will disappear on its own, written with the offset of the portal's time zone. It is filled in  only where a removal is actually scheduled - something in the trash while the portal cleans it up  automatically, or a guest's own documents - so a null means nothing is scheduled rather than that the entry is  permanent.", alias="autoDelete")
    root_folder_type: Optional[AiFolderType] = Field(default=None, description="The section the entry ultimately belongs to, which is what tells a personal document from one inside a room,  from a template and from something in the trash or the archive.", alias="rootFolderType")
    parent_room_type: Optional[AiFolderType] = Field(default=None, description="The kind of room the entry lies in, which decides what the room allows - filling forms, public links,  indexing. It is null for an entry that is not inside a room at all.", alias="parentRoomType")
    updated_by: Optional[AiEmployeeDto] = Field(default=None, description="Who changed the entry last. It is null for a caller without an account.", alias="updatedBy")
    provider_item: Optional[StrictBool] = Field(default=None, description="Set when the entry is stored on a connected third-party account rather than on the portal, and null when it is  stored on the portal. Such an entry is identified by a string rather than a number, and some operations skip  it.", alias="providerItem", json_schema_extra={"examples": [True]})
    provider_key: Optional[StrictStr] = Field(default=None, description="Which third-party service holds the entry, matching the keys accepted by the third-party operations. It is  null for an entry stored on the portal.", alias="providerKey", json_schema_extra={"examples": ["google-drive"]})
    provider_id: Optional[StrictInt] = Field(default=None, description="The connected account the entry comes from, for telling apart two connections to the same service. It is null  for an entry stored on the portal.", alias="providerId", json_schema_extra={"examples": [1]})
    order: Optional[StrictStr] = Field(default=None, description="The place of the entry in a room where the members arrange the content themselves, given as the position of  the entry preceded by the positions of the folders leading to it, separated by dots. It is empty when nothing  has been arranged.", json_schema_extra={"examples": ["1.3.2"]})
    is_favorite: Optional[StrictBool] = Field(default=None, description="Set when the calling account has marked the entry as a favorite, which is what puts it into the favorites  listing. For a file that is not marked it is null rather than false.", alias="isFavorite", json_schema_extra={"examples": [True]})
    file_entry_type: Optional[AiFileEntryType] = Field(default=None, description="Tells a folder from a file, and so which of the two shapes the rest of the object has. A room is reported as a  folder here.", alias="fileEntryType")
    __properties: ClassVar[List[str]] = ["title", "access", "sharedBy", "ownedBy", "shared", "sharedForUser", "sharedExternal", "parentShared", "shortWebUrl", "created", "createdBy", "updated", "autoDelete", "rootFolderType", "parentRoomType", "updatedBy", "providerItem", "providerKey", "providerId", "order", "isFavorite", "fileEntryType"]

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
        """Create an instance of AiFileEntryBaseDto from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if short_web_url (nullable) is None
        # and model_fields_set contains the field
        if self.short_web_url is None and "short_web_url" in self.model_fields_set:
            _dict['shortWebUrl'] = None

        # set to None if provider_item (nullable) is None
        # and model_fields_set contains the field
        if self.provider_item is None and "provider_item" in self.model_fields_set:
            _dict['providerItem'] = None

        # set to None if provider_key (nullable) is None
        # and model_fields_set contains the field
        if self.provider_key is None and "provider_key" in self.model_fields_set:
            _dict['providerKey'] = None

        # set to None if provider_id (nullable) is None
        # and model_fields_set contains the field
        if self.provider_id is None and "provider_id" in self.model_fields_set:
            _dict['providerId'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if is_favorite (nullable) is None
        # and model_fields_set contains the field
        if self.is_favorite is None and "is_favorite" in self.model_fields_set:
            _dict['isFavorite'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiFileEntryBaseDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "access": obj.get("access"),
            "sharedBy": AiEmployeeDto.from_dict(obj["sharedBy"]) if obj.get("sharedBy") is not None else None,
            "ownedBy": AiEmployeeDto.from_dict(obj["ownedBy"]) if obj.get("ownedBy") is not None else None,
            "shared": obj.get("shared"),
            "sharedForUser": obj.get("sharedForUser"),
            "sharedExternal": obj.get("sharedExternal"),
            "parentShared": obj.get("parentShared"),
            "shortWebUrl": obj.get("shortWebUrl"),
            "created": AiApiDateTime.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "createdBy": AiEmployeeDto.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "updated": AiApiDateTime.from_dict(obj["updated"]) if obj.get("updated") is not None else None,
            "autoDelete": AiApiDateTime.from_dict(obj["autoDelete"]) if obj.get("autoDelete") is not None else None,
            "rootFolderType": obj.get("rootFolderType"),
            "parentRoomType": obj.get("parentRoomType"),
            "updatedBy": AiEmployeeDto.from_dict(obj["updatedBy"]) if obj.get("updatedBy") is not None else None,
            "providerItem": obj.get("providerItem"),
            "providerKey": obj.get("providerKey"),
            "providerId": obj.get("providerId"),
            "order": obj.get("order"),
            "isFavorite": obj.get("isFavorite"),
            "fileEntryType": obj.get("fileEntryType")
        })
        return _obj


