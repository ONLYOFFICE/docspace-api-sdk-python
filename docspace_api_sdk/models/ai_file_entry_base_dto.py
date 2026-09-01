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
    The file entry information.
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The file entry title.", json_schema_extra={"examples": ["Some title.txt"]})
    access: Optional[AiFileShare] = Field(default=None, description="The access rights to the file entry.")
    shared_by: Optional[AiEmployeeDto] = Field(default=None, description="Provides information about the employee who shared the file or folder.", alias="sharedBy")
    owned_by: Optional[AiEmployeeDto] = Field(default=None, description="The information about the employee who owns the file entry.", alias="ownedBy")
    shared: Optional[StrictBool] = Field(default=None, description="Specifies if the file entry is shared via link or not.", json_schema_extra={"examples": [False]})
    shared_for_user: Optional[StrictBool] = Field(default=None, description="Specifies if the file entry is shared for user or not.", alias="sharedForUser", json_schema_extra={"examples": [False]})
    shared_external: Optional[StrictBool] = Field(default=None, description="Specifies if the file entry is shared via a public (non-internal) external link.", alias="sharedExternal", json_schema_extra={"examples": [False]})
    parent_shared: Optional[StrictBool] = Field(default=None, description="Indicates whether the parent entity is shared.", alias="parentShared", json_schema_extra={"examples": [False]})
    short_web_url: Optional[StrictStr] = Field(default=None, description="The short Web URL.", alias="shortWebUrl", json_schema_extra={"examples": ["http://localhost/s/abc123"]})
    created: Optional[AiApiDateTime] = Field(default=None, description="The creation date and time of the file entry.")
    created_by: Optional[AiEmployeeDto] = Field(default=None, description="The file entry author.", alias="createdBy")
    updated: Optional[AiApiDateTime] = Field(default=None, description="The last date and time when the file entry was updated.")
    auto_delete: Optional[AiApiDateTime] = Field(default=None, description="The date and time when the file entry will be automatically deleted.", alias="autoDelete")
    root_folder_type: Optional[AiFolderType] = Field(default=None, description="The root folder type of the file entry.", alias="rootFolderType")
    parent_room_type: Optional[AiFolderType] = Field(default=None, description="The parent room type of the file entry.", alias="parentRoomType")
    updated_by: Optional[AiEmployeeDto] = Field(default=None, description="The user who updated the file entry.", alias="updatedBy")
    provider_item: Optional[StrictBool] = Field(default=None, description="Specifies if the file entry provider is specified or not.", alias="providerItem", json_schema_extra={"examples": [False]})
    provider_key: Optional[StrictStr] = Field(default=None, description="The provider key of the file entry.", alias="providerKey", json_schema_extra={"examples": ["google-drive"]})
    provider_id: Optional[StrictInt] = Field(default=None, description="The provider ID of the file entry.", alias="providerId", json_schema_extra={"examples": [1]})
    order: Optional[StrictStr] = Field(default=None, description="The order of the file entry.", json_schema_extra={"examples": ["1"]})
    is_favorite: Optional[StrictBool] = Field(default=None, description="Specifies if the file is a favorite or not.", alias="isFavorite", json_schema_extra={"examples": [False]})
    file_entry_type: Optional[AiFileEntryType] = Field(default=None, description="The file entry type.", alias="fileEntryType")
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


