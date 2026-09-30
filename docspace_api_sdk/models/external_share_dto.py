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
from uuid import UUID
from docspace_api_sdk.models.file_entry_type import FileEntryType
from docspace_api_sdk.models.status import Status
from typing import Optional, Set
from typing_extensions import Self

class ExternalShareDto(BaseModel):
    """
    The outcome of validating an external share link and the entry it points at.
    """ # noqa: E501
    status: Status = Field(description="How validating the link went. It is the first field to read: a refused link is reported here with the answer  still arriving as a success. A link that resolved describes both the entry and the link, one that is waiting  for its password describes only the entry, and one that failed outright leaves the rest of the object empty.")
    id: Optional[StrictStr] = Field(default=None, description="The identifier of the room, folder or file the link points at, always rendered as a string even where the  portal stores it as a number. It is null when the link could not be resolved.", json_schema_extra={"examples": ["42"]})
    title: Optional[StrictStr] = Field(default=None, description="The title of the entry the link points at, suitable for showing to the visitor before they are let in. It is  null when the link could not be resolved.", json_schema_extra={"examples": ["Project documents"]})
    type: Optional[FileEntryType] = Field(default=None, description="Whether the link points at a folder - a room counts as one - or at a single file. It is null when the link  could not be resolved.")
    tenant_id: StrictInt = Field(description="The portal the link belongs to, which matters for a client that works with more than one. It stays 0 for a  link that did not resolve.", alias="tenantId", json_schema_extra={"examples": [1]})
    entity_id: Optional[StrictStr] = Field(default=None, description="The identifier of the entry that was asked about through the request's file or folder parameter, echoed back  once it was found under the link's target. It is null when nothing was asked about, or when the entry lies  outside what the link opens.", alias="entityId", json_schema_extra={"examples": ["9"]})
    entity_title: Optional[StrictStr] = Field(default=None, description="The title of that entry, null under the same conditions as its identifier.", alias="entityTitle", json_schema_extra={"examples": ["Contract.docx"]})
    entity_type: Optional[FileEntryType] = Field(default=None, description="Whether that entry is a folder or a file, null under the same conditions as its identifier.", alias="entityType")
    is_room: Optional[StrictBool] = Field(default=None, description="True when the link opens a whole room rather than one entry inside it. It is null for a link to a file and for  a link that did not resolve.", alias="isRoom", json_schema_extra={"examples": [True]})
    shared: StrictBool = Field(description="True when the entry now sits in the calling account's own lists - it was already shared with that account, or  resolving the link has just put it there. It stays false for a visitor browsing without an account, who  reaches the entry through the link alone.", json_schema_extra={"examples": [True]})
    link_id: UUID = Field(description="The link the token belongs to, which is also the subject under which the link appears among the sharing rights  of the entry. It is an empty identifier when the link did not resolve.", alias="linkId", json_schema_extra={"examples": ["b3a1f0c7-5d2e-4a19-9f38-71c6e0d4b852"]})
    is_authenticated: StrictBool = Field(description="Whether the request carried a signed-in account. It says nothing about that account's rights on the entry, so  it must not be read as permission - it is false for every anonymous visitor and true for any member, even one  who is a stranger to the room.", alias="isAuthenticated", json_schema_extra={"examples": [True]})
    is_room_member: Optional[StrictBool] = Field(default=None, description="Whether the signed-in caller already has rights of their own on the room that holds the entry, as opposed to  reaching it through this link. It is false for an anonymous visitor and for a member who has never been  invited.", alias="isRoomMember", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["status", "id", "title", "type", "tenantId", "entityId", "entityTitle", "entityType", "isRoom", "shared", "linkId", "isAuthenticated", "isRoomMember"]

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
        """Create an instance of ExternalShareDto from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if entity_id (nullable) is None
        # and model_fields_set contains the field
        if self.entity_id is None and "entity_id" in self.model_fields_set:
            _dict['entityId'] = None

        # set to None if entity_title (nullable) is None
        # and model_fields_set contains the field
        if self.entity_title is None and "entity_title" in self.model_fields_set:
            _dict['entityTitle'] = None

        # set to None if is_room (nullable) is None
        # and model_fields_set contains the field
        if self.is_room is None and "is_room" in self.model_fields_set:
            _dict['isRoom'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalShareDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "id": obj.get("id"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "tenantId": obj.get("tenantId"),
            "entityId": obj.get("entityId"),
            "entityTitle": obj.get("entityTitle"),
            "entityType": obj.get("entityType"),
            "isRoom": obj.get("isRoom"),
            "shared": obj.get("shared"),
            "linkId": obj.get("linkId"),
            "isAuthenticated": obj.get("isAuthenticated"),
            "isRoomMember": obj.get("isRoomMember")
        })
        return _obj


