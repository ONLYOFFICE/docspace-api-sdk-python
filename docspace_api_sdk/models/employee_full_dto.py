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
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from uuid import UUID
from docspace_api_sdk.models.contact import Contact
from docspace_api_sdk.models.dark_theme_settings_type import DarkThemeSettingsType
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_dto import EmployeeDto
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.group_summary_dto import GroupSummaryDto
from docspace_api_sdk.models.mobile_phone_activation_status import MobilePhoneActivationStatus
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field
from docspace_api_sdk.models.employee_dto import EmployeeDto

class EmployeeFullDto(EmployeeDto):
    """
    The full list of user parameters.
    """

    first_name: Optional[StrictStr] = Field(default=None, description="The user first name.", alias="firstName", json_schema_extra={"examples": ["Mike"]})
    last_name: Optional[StrictStr] = Field(default=None, description="The user last name.", alias="lastName", json_schema_extra={"examples": ["Zanyatski"]})
    user_name: Optional[StrictStr] = Field(default=None, description="The user username.", alias="userName", json_schema_extra={"examples": ["Mike.Zanyatski"]})
    email: Optional[StrictStr] = Field(default=None, description="The user email.", json_schema_extra={"examples": ["my@gmail.com"]})
    contacts: Optional[List[Contact]] = Field(default=None, description="The list of user contacts.", json_schema_extra={"examples": [[{"type": "email", "value": "user@example.com"}]]})
    status: Optional[EmployeeStatus] = Field(default=None, description="The user status.")
    activation_status: Optional[EmployeeActivationStatus] = Field(default=None, description="The user activation status.", alias="activationStatus")
    terminated: Optional[datetime] = Field(default=None, description="The date when the user account was terminated.", json_schema_extra={"examples": ["2025-06-01T00:00:00.0000000Z"]})
    department: Optional[StrictStr] = Field(default=None, description="The user department.", json_schema_extra={"examples": ["Marketing"]})
    groups: Optional[List[GroupSummaryDto]] = Field(default=None, description="The list of user groups.", json_schema_extra={"examples": [[{"id": "00000000-0000-0000-0000-000000000000", "name": "Marketing"}]]})
    location: Optional[StrictStr] = Field(default=None, description="The user location.", json_schema_extra={"examples": ["Palo Alto"]})
    notes: Optional[StrictStr] = Field(default=None, description="The user notes.", json_schema_extra={"examples": ["Notes to worker"]})
    is_admin: Optional[StrictBool] = Field(default=None, description="Specifies if the user is an administrator or not.", alias="isAdmin", json_schema_extra={"examples": [False]})
    is_room_admin: Optional[StrictBool] = Field(default=None, description="Specifies if the user is a room administrator or not.", alias="isRoomAdmin", json_schema_extra={"examples": [False]})
    is_ldap: Optional[StrictBool] = Field(default=None, description="Specifies if the LDAP settings are enabled for the user or not.", alias="isLDAP", json_schema_extra={"examples": [False]})
    list_admin_modules: Optional[List[StrictStr]] = Field(default=None, description="The list of the administrator modules.", alias="listAdminModules", json_schema_extra={"examples": [["projects", "crm"]]})
    is_owner: Optional[StrictBool] = Field(default=None, description="Specifies if the user is a portal owner or not.", alias="isOwner", json_schema_extra={"examples": [False]})
    is_visitor: Optional[StrictBool] = Field(default=None, description="Specifies if the user is a portal visitor or not.", alias="isVisitor", json_schema_extra={"examples": [False]})
    is_collaborator: Optional[StrictBool] = Field(default=None, description="Specifies if the user is a portal collaborator or not.", alias="isCollaborator", json_schema_extra={"examples": [False]})
    culture_name: Optional[StrictStr] = Field(default=None, description="The user culture code.", alias="cultureName", json_schema_extra={"examples": ["en-EN"]})
    mobile_phone: Optional[StrictStr] = Field(default=None, description="The user mobile phone number.", alias="mobilePhone", json_schema_extra={"examples": ["+1 (555) 123-4567"]})
    mobile_phone_activation_status: Optional[MobilePhoneActivationStatus] = Field(default=None, description="The mobile phone activation status.", alias="mobilePhoneActivationStatus")
    is_sso: Optional[StrictBool] = Field(default=None, description="Specifies if the SSO settings are enabled for the user or not.", alias="isSSO", json_schema_extra={"examples": [False]})
    theme: Optional[DarkThemeSettingsType] = Field(default=None, description="The user theme settings.")
    quota_limit: Optional[StrictInt] = Field(default=None, description="The user quota limit.", alias="quotaLimit", json_schema_extra={"examples": [1073741824]})
    used_space: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The portal used space of the user.", alias="usedSpace", json_schema_extra={"examples": [12345]})
    shared: Optional[StrictBool] = Field(default=None, description="Specifies if the user has access rights.", json_schema_extra={"examples": [False]})
    is_custom_quota: Optional[StrictBool] = Field(default=None, description="Specifies if the user has a custom quota or not.", alias="isCustomQuota", json_schema_extra={"examples": [False]})
    login_event_id: Optional[StrictInt] = Field(default=None, description="The current login event ID.", alias="loginEventId", json_schema_extra={"examples": [123]})
    auth_cookie_lifetime: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The auth cookie lifetime in seconds.", alias="authCookieLifetime", json_schema_extra={"examples": [3600]})
    created_by: Optional[EmployeeDto] = Field(default=None, description="The user who created the current user.", alias="createdBy")
    registration_date: Optional[datetime] = Field(default=None, description="The user registration date.", alias="registrationDate", json_schema_extra={"examples": ["2020-01-01T00:00:00.0000000Z"]})
    has_personal_folder: Optional[StrictBool] = Field(default=None, description="Specifies if the user has a personal folder or not.", alias="hasPersonalFolder", json_schema_extra={"examples": [True]})
    tfa_app_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the user has enabled two-factor authentication (TFA) using an authentication app.", alias="tfaAppEnabled", json_schema_extra={"examples": [False]})

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

        # set to None if terminated (nullable) is None
        # and model_fields_set contains the field
        if self.terminated is None and "terminated" in self.model_fields_set:
            _dict['terminated'] = None

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

        # set to None if auth_cookie_lifetime (nullable) is None
        # and model_fields_set contains the field
        if self.auth_cookie_lifetime is None and "auth_cookie_lifetime" in self.model_fields_set:
            _dict['authCookieLifetime'] = None

        # set to None if registration_date (nullable) is None
        # and model_fields_set contains the field
        if self.registration_date is None and "registration_date" in self.model_fields_set:
            _dict['registrationDate'] = None

        # set to None if has_personal_folder (nullable) is None
        # and model_fields_set contains the field
        if self.has_personal_folder is None and "has_personal_folder" in self.model_fields_set:
            _dict['hasPersonalFolder'] = None

        # set to None if tfa_app_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.tfa_app_enabled is None and "tfa_app_enabled" in self.model_fields_set:
            _dict['tfaAppEnabled'] = None

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
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "userName": obj.get("userName"),
            "email": obj.get("email"),
            "contacts": [Contact.from_dict(_item) for _item in obj["contacts"]] if obj.get("contacts") is not None else None,
            "status": obj.get("status"),
            "activationStatus": obj.get("activationStatus"),
            "terminated": obj.get("terminated"),
            "department": obj.get("department"),
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
            "authCookieLifetime": obj.get("authCookieLifetime"),
            "createdBy": EmployeeDto.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "registrationDate": obj.get("registrationDate"),
            "hasPersonalFolder": obj.get("hasPersonalFolder"),
            "tfaAppEnabled": obj.get("tfaAppEnabled")
        }
        all_fields = {**base_dict, **extra_fields}
        return cls.model_validate(all_fields)


