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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from docspace.models.api_date_time import ApiDateTime
from docspace.models.contact import Contact
from docspace.models.dark_theme_settings_type import DarkThemeSettingsType
from docspace.models.employee_activation_status import EmployeeActivationStatus
from docspace.models.employee_dto import EmployeeDto
from docspace.models.employee_status import EmployeeStatus
from docspace.models.group_summary_dto import GroupSummaryDto
from docspace.models.mobile_phone_activation_status import MobilePhoneActivationStatus
from typing import Optional, Set
from typing_extensions import Self

class EmployeeFullDto(BaseModel):
    """
    The full list of user parameters.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The user ID.")
    display_name: Optional[StrictStr] = Field(default=None, description="The user display name.", alias="displayName")
    title: Optional[StrictStr] = Field(default=None, description="The user title.")
    avatar: Optional[StrictStr] = Field(default=None, description="The user avatar.")
    avatar_original: Optional[StrictStr] = Field(default=None, description="The user original size avatar.", alias="avatarOriginal")
    avatar_max: Optional[StrictStr] = Field(default=None, description="The user maximum size avatar.", alias="avatarMax")
    avatar_medium: Optional[StrictStr] = Field(default=None, description="The user medium size avatar.", alias="avatarMedium")
    avatar_small: Optional[StrictStr] = Field(default=None, description="The user small size avatar.", alias="avatarSmall")
    profile_url: Optional[StrictStr] = Field(default=None, description="The user profile URL.", alias="profileUrl")
    has_avatar: Optional[StrictBool] = Field(default=None, description="Specifies if the user has an avatar or not.", alias="hasAvatar")
    is_anonim: Optional[StrictBool] = Field(default=None, description="Specifies if the user is anonymous or not.", alias="isAnonim")
    first_name: Optional[StrictStr] = Field(default=None, description="The user first name.", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="The user last name.", alias="lastName")
    user_name: Optional[StrictStr] = Field(default=None, description="The user username.", alias="userName")
    email: Optional[StrictStr] = Field(default=None, description="The user email.")
    contacts: Optional[List[Contact]] = Field(default=None, description="The list of user contacts.")
    birthday: Optional[ApiDateTime] = None
    sex: Optional[StrictStr] = Field(default=None, description="The user sex.")
    status: Optional[EmployeeStatus] = None
    activation_status: Optional[EmployeeActivationStatus] = Field(default=None, alias="activationStatus")
    terminated: Optional[ApiDateTime] = None
    department: Optional[StrictStr] = Field(default=None, description="The user department.")
    work_from: Optional[ApiDateTime] = Field(default=None, alias="workFrom")
    groups: Optional[List[GroupSummaryDto]] = Field(default=None, description="The list of user groups.")
    location: Optional[StrictStr] = Field(default=None, description="The user location.")
    notes: Optional[StrictStr] = Field(default=None, description="The user notes.")
    is_admin: Optional[StrictBool] = Field(default=None, description="Specifies if the user is an administrator or not.", alias="isAdmin")
    is_room_admin: Optional[StrictBool] = Field(default=None, description="Specifies if the user is a room administrator or not.", alias="isRoomAdmin")
    is_ldap: Optional[StrictBool] = Field(default=None, description="Specifies if the LDAP settings are enabled for the user or not.", alias="isLDAP")
    list_admin_modules: Optional[List[StrictStr]] = Field(default=None, description="The list of the administrator modules.", alias="listAdminModules")
    is_owner: Optional[StrictBool] = Field(default=None, description="Specifies if the user is a portal owner or not.", alias="isOwner")
    is_visitor: Optional[StrictBool] = Field(default=None, description="Specifies if the user is a portal visitor or not.", alias="isVisitor")
    is_collaborator: Optional[StrictBool] = Field(default=None, description="Specifies if the user is a portal collaborator or not.", alias="isCollaborator")
    culture_name: Optional[StrictStr] = Field(default=None, description="The user culture code.", alias="cultureName")
    mobile_phone: Optional[StrictStr] = Field(default=None, description="The user mobile phone number.", alias="mobilePhone")
    mobile_phone_activation_status: Optional[MobilePhoneActivationStatus] = Field(default=None, alias="mobilePhoneActivationStatus")
    is_sso: Optional[StrictBool] = Field(default=None, description="Specifies if the SSO settings are enabled for the user or not.", alias="isSSO")
    theme: Optional[DarkThemeSettingsType] = None
    quota_limit: Optional[StrictInt] = Field(default=None, description="The user quota limit.", alias="quotaLimit")
    used_space: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The portal used space of the user.", alias="usedSpace")
    shared: Optional[StrictBool] = Field(default=None, description="Specifies if the user has access rights.")
    is_custom_quota: Optional[StrictBool] = Field(default=None, description="Specifies if the user has a custom quota or not.", alias="isCustomQuota")
    login_event_id: Optional[StrictInt] = Field(default=None, description="The current login event ID.", alias="loginEventId")
    created_by: Optional[EmployeeDto] = Field(default=None, alias="createdBy")
    registration_date: Optional[ApiDateTime] = Field(default=None, alias="registrationDate")
    has_personal_folder: Optional[StrictBool] = Field(default=None, description="Specifies if the user has a personal folder or not.", alias="hasPersonalFolder")
    tfa_app_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the user has enabled two-factor authentication (TFA) using an authentication app.", alias="tfaAppEnabled")
    __properties: ClassVar[List[str]] = ["id", "displayName", "title", "avatar", "avatarOriginal", "avatarMax", "avatarMedium", "avatarSmall", "profileUrl", "hasAvatar", "isAnonim", "firstName", "lastName", "userName", "email", "contacts", "birthday", "sex", "status", "activationStatus", "terminated", "department", "workFrom", "groups", "location", "notes", "isAdmin", "isRoomAdmin", "isLDAP", "listAdminModules", "isOwner", "isVisitor", "isCollaborator", "cultureName", "mobilePhone", "mobilePhoneActivationStatus", "isSSO", "theme", "quotaLimit", "usedSpace", "shared", "isCustomQuota", "loginEventId", "createdBy", "registrationDate", "hasPersonalFolder", "tfaAppEnabled"]

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
        """Create an instance of EmployeeFullDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in contacts (list)
        _items = []
        if self.contacts:
            for _item_contacts in self.contacts:
                if _item_contacts:
                    _items.append(_item_contacts.to_dict())
            _dict['contacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of birthday
        if self.birthday:
            _dict['birthday'] = self.birthday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terminated
        if self.terminated:
            _dict['terminated'] = self.terminated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_from
        if self.work_from:
            _dict['workFrom'] = self.work_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of registration_date
        if self.registration_date:
            _dict['registrationDate'] = self.registration_date.to_dict()
        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['displayName'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if avatar_original (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_original is None and "avatar_original" in self.model_fields_set:
            _dict['avatarOriginal'] = None

        # set to None if avatar_max (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_max is None and "avatar_max" in self.model_fields_set:
            _dict['avatarMax'] = None

        # set to None if avatar_medium (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_medium is None and "avatar_medium" in self.model_fields_set:
            _dict['avatarMedium'] = None

        # set to None if avatar_small (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_small is None and "avatar_small" in self.model_fields_set:
            _dict['avatarSmall'] = None

        # set to None if profile_url (nullable) is None
        # and model_fields_set contains the field
        if self.profile_url is None and "profile_url" in self.model_fields_set:
            _dict['profileUrl'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if user_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_name is None and "user_name" in self.model_fields_set:
            _dict['userName'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if contacts (nullable) is None
        # and model_fields_set contains the field
        if self.contacts is None and "contacts" in self.model_fields_set:
            _dict['contacts'] = None

        # set to None if sex (nullable) is None
        # and model_fields_set contains the field
        if self.sex is None and "sex" in self.model_fields_set:
            _dict['sex'] = None

        # set to None if department (nullable) is None
        # and model_fields_set contains the field
        if self.department is None and "department" in self.model_fields_set:
            _dict['department'] = None

        # set to None if groups (nullable) is None
        # and model_fields_set contains the field
        if self.groups is None and "groups" in self.model_fields_set:
            _dict['groups'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if list_admin_modules (nullable) is None
        # and model_fields_set contains the field
        if self.list_admin_modules is None and "list_admin_modules" in self.model_fields_set:
            _dict['listAdminModules'] = None

        # set to None if culture_name (nullable) is None
        # and model_fields_set contains the field
        if self.culture_name is None and "culture_name" in self.model_fields_set:
            _dict['cultureName'] = None

        # set to None if mobile_phone (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_phone is None and "mobile_phone" in self.model_fields_set:
            _dict['mobilePhone'] = None

        # set to None if quota_limit (nullable) is None
        # and model_fields_set contains the field
        if self.quota_limit is None and "quota_limit" in self.model_fields_set:
            _dict['quotaLimit'] = None

        # set to None if used_space (nullable) is None
        # and model_fields_set contains the field
        if self.used_space is None and "used_space" in self.model_fields_set:
            _dict['usedSpace'] = None

        # set to None if shared (nullable) is None
        # and model_fields_set contains the field
        if self.shared is None and "shared" in self.model_fields_set:
            _dict['shared'] = None

        # set to None if is_custom_quota (nullable) is None
        # and model_fields_set contains the field
        if self.is_custom_quota is None and "is_custom_quota" in self.model_fields_set:
            _dict['isCustomQuota'] = None

        # set to None if login_event_id (nullable) is None
        # and model_fields_set contains the field
        if self.login_event_id is None and "login_event_id" in self.model_fields_set:
            _dict['loginEventId'] = None

        # set to None if tfa_app_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.tfa_app_enabled is None and "tfa_app_enabled" in self.model_fields_set:
            _dict['tfaAppEnabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EmployeeFullDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "displayName": obj.get("displayName"),
            "title": obj.get("title"),
            "avatar": obj.get("avatar"),
            "avatarOriginal": obj.get("avatarOriginal"),
            "avatarMax": obj.get("avatarMax"),
            "avatarMedium": obj.get("avatarMedium"),
            "avatarSmall": obj.get("avatarSmall"),
            "profileUrl": obj.get("profileUrl"),
            "hasAvatar": obj.get("hasAvatar"),
            "isAnonim": obj.get("isAnonim"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "userName": obj.get("userName"),
            "email": obj.get("email"),
            "contacts": [Contact.from_dict(_item) for _item in obj["contacts"]] if obj.get("contacts") is not None else None,
            "birthday": ApiDateTime.from_dict(obj["birthday"]) if obj.get("birthday") is not None else None,
            "sex": obj.get("sex"),
            "status": obj.get("status"),
            "activationStatus": obj.get("activationStatus"),
            "terminated": ApiDateTime.from_dict(obj["terminated"]) if obj.get("terminated") is not None else None,
            "department": obj.get("department"),
            "workFrom": ApiDateTime.from_dict(obj["workFrom"]) if obj.get("workFrom") is not None else None,
            "groups": [GroupSummaryDto.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "location": obj.get("location"),
            "notes": obj.get("notes"),
            "isAdmin": obj.get("isAdmin"),
            "isRoomAdmin": obj.get("isRoomAdmin"),
            "isLDAP": obj.get("isLDAP"),
            "listAdminModules": obj.get("listAdminModules"),
            "isOwner": obj.get("isOwner"),
            "isVisitor": obj.get("isVisitor"),
            "isCollaborator": obj.get("isCollaborator"),
            "cultureName": obj.get("cultureName"),
            "mobilePhone": obj.get("mobilePhone"),
            "mobilePhoneActivationStatus": obj.get("mobilePhoneActivationStatus"),
            "isSSO": obj.get("isSSO"),
            "theme": obj.get("theme"),
            "quotaLimit": obj.get("quotaLimit"),
            "usedSpace": obj.get("usedSpace"),
            "shared": obj.get("shared"),
            "isCustomQuota": obj.get("isCustomQuota"),
            "loginEventId": obj.get("loginEventId"),
            "createdBy": EmployeeDto.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "registrationDate": ApiDateTime.from_dict(obj["registrationDate"]) if obj.get("registrationDate") is not None else None,
            "hasPersonalFolder": obj.get("hasPersonalFolder"),
            "tfaAppEnabled": obj.get("tfaAppEnabled")
        })
        return _obj


