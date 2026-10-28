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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.employee_full_dto import EmployeeFullDto
from docspace_api_sdk.models.file_share import FileShare
from docspace_api_sdk.models.file_share_link import FileShareLink
from docspace_api_sdk.models.group_summary_dto import GroupSummaryDto
from docspace_api_sdk.models.subject_type import SubjectType
from typing import Optional, Set
from typing_extensions import Self

class FileShareDto(BaseModel):
    """
    One access entry on a file, a folder or a room: who holds it, at which level, and what the caller may change about  it.
    """ # noqa: E501
    access: Optional[FileShare] = Field(default=None, description="The level the subject holds on the entry. On a link entry it is the level the link hands to whoever opens it,  and in a batch answer `Varies` means the subject holds different levels on the listed entries.")
    shared_to: Optional[Any] = Field(default=None, alias="sharedTo")
    shared_to_user: Optional[EmployeeFullDto] = Field(default=None, description="The account the entry belongs to. It is filled in only when `subjectType` says an account, and is null for a  group entry and for a link.", alias="sharedToUser")
    shared_to_group: Optional[GroupSummaryDto] = Field(default=None, description="The portal group the entry belongs to, which hands the level to everybody in it. It is filled in only for a  group entry, and is null otherwise.", alias="sharedToGroup")
    shared_link: Optional[FileShareLink] = Field(default=None, description="The sharing link the entry stands for, together with everything set on it. It is filled in only for a link  entry, and is null for an account or a group.", alias="sharedLink")
    is_locked: StrictBool = Field(description="Whether this entry is the caller's own, which is why they cannot change its level. Link entries never report  it.", alias="isLocked", json_schema_extra={"examples": [False]})
    is_owner: StrictBool = Field(description="Whether the subject created the entry the access is given on, and so cannot be removed from it.", alias="isOwner", json_schema_extra={"examples": [False]})
    can_edit_access: StrictBool = Field(description="Whether the caller may change the level of this entry. It is false on the caller's own entry, on every link,  and whenever the caller may not hand out access at all.", alias="canEditAccess", json_schema_extra={"examples": [True]})
    can_edit_internal: StrictBool = Field(description="Whether the caller may switch this link between being open to anybody and asking the visitor to sign in to the  portal first.", alias="canEditInternal", json_schema_extra={"examples": [True]})
    can_edit_deny_download: StrictBool = Field(description="Whether the caller may forbid downloading through this link. Only a link of a virtual data room reports true,  and only while the room itself still allows downloads.", alias="canEditDenyDownload", json_schema_extra={"examples": [True]})
    can_edit_expiration_date: StrictBool = Field(description="Whether the caller may move the moment this link stops working.", alias="canEditExpirationDate", json_schema_extra={"examples": [True]})
    can_revoke: StrictBool = Field(description="Whether the caller may take this entry away altogether, which for a link means deleting the link.", alias="canRevoke", json_schema_extra={"examples": [True]})
    subject_type: SubjectType = Field(description="What the entry was given to, which tells which of the three subject fields is filled in: an account, a group,  or one of the kinds of link.", alias="subjectType")
    __properties: ClassVar[List[str]] = ["access", "sharedTo", "sharedToUser", "sharedToGroup", "sharedLink", "isLocked", "isOwner", "canEditAccess", "canEditInternal", "canEditDenyDownload", "canEditExpirationDate", "canRevoke", "subjectType"]

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
        """Create an instance of FileShareDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shared_to_user
        if self.shared_to_user:
            _dict['sharedToUser'] = self.shared_to_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shared_to_group
        if self.shared_to_group:
            _dict['sharedToGroup'] = self.shared_to_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shared_link
        if self.shared_link:
            _dict['sharedLink'] = self.shared_link.to_dict()
        # set to None if shared_to (nullable) is None
        # and model_fields_set contains the field
        if self.shared_to is None and "shared_to" in self.model_fields_set:
            _dict['sharedTo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileShareDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "access": obj.get("access"),
            "sharedTo": obj.get("sharedTo"),
            "sharedToUser": EmployeeFullDto.from_dict(obj["sharedToUser"]) if obj.get("sharedToUser") is not None else None,
            "sharedToGroup": GroupSummaryDto.from_dict(obj["sharedToGroup"]) if obj.get("sharedToGroup") is not None else None,
            "sharedLink": FileShareLink.from_dict(obj["sharedLink"]) if obj.get("sharedLink") is not None else None,
            "isLocked": obj.get("isLocked"),
            "isOwner": obj.get("isOwner"),
            "canEditAccess": obj.get("canEditAccess"),
            "canEditInternal": obj.get("canEditInternal"),
            "canEditDenyDownload": obj.get("canEditDenyDownload"),
            "canEditExpirationDate": obj.get("canEditExpirationDate"),
            "canRevoke": obj.get("canRevoke"),
            "subjectType": obj.get("subjectType")
        })
        return _obj


