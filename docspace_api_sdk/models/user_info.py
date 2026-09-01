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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.mobile_phone_activation_status import MobilePhoneActivationStatus
from typing import Optional, Set
from typing_extensions import Self

class UserInfo(BaseModel):
    """
    The user information.
    """ # noqa: E501
    id: Optional[UUID] = Field(default=None, description="The user ID.", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    first_name: Optional[StrictStr] = Field(default=None, description="The user's first name.", alias="firstName", json_schema_extra={"examples": ["John"]})
    last_name: Optional[StrictStr] = Field(default=None, description="The user's last name.", alias="lastName", json_schema_extra={"examples": ["Doe"]})
    user_name: Optional[StrictStr] = Field(default=None, description="The user username.", alias="userName", json_schema_extra={"examples": ["johndoe"]})
    birth_date: Optional[datetime] = Field(default=None, description="The user birthday.", alias="birthDate", json_schema_extra={"examples": ["1990-01-01T00:00:00Z"]})
    sex: Optional[StrictBool] = Field(default=None, description="The user sex (male or female).", json_schema_extra={"examples": [True]})
    status: Optional[EmployeeStatus] = Field(default=None, description="The user status.")
    activation_status: Optional[EmployeeActivationStatus] = Field(default=None, description="The user activation status.", alias="activationStatus")
    terminated_date: Optional[datetime] = Field(default=None, description="The date and time when the user account was terminated.", alias="terminatedDate", json_schema_extra={"examples": ["2025-12-31T23:59:59Z"]})
    title: Optional[StrictStr] = Field(default=None, description="The user title.", json_schema_extra={"examples": ["Manager"]})
    work_from_date: Optional[datetime] = Field(default=None, description="The user registration date.", alias="workFromDate", json_schema_extra={"examples": ["2020-01-15T00:00:00Z"]})
    email: Optional[StrictStr] = Field(default=None, description="The user email address.", json_schema_extra={"examples": ["john.doe@example.com"]})
    contacts: Optional[StrictStr] = Field(default=None, description="The list of user contacts in the string format.", json_schema_extra={"examples": ["skype:johndoe|telegram:@johndoe"]})
    contacts_list: Optional[List[StrictStr]] = Field(default=None, description="The list of user contacts.", alias="contactsList", json_schema_extra={"examples": [["skype:johndoe", "telegram:@johndoe"]]})
    location: Optional[StrictStr] = Field(default=None, description="The user location.", json_schema_extra={"examples": ["New York, USA"]})
    notes: Optional[StrictStr] = Field(default=None, description="The user notes.", json_schema_extra={"examples": ["Additional information about the user"]})
    removed: Optional[StrictBool] = Field(default=None, description="Specifies if the user account was removed or not.", json_schema_extra={"examples": [False]})
    last_modified: Optional[datetime] = Field(default=None, description="The date and time when the user account was last modified.", alias="lastModified", json_schema_extra={"examples": ["2025-02-08T10:30:00Z"]})
    tenant_id: Optional[StrictInt] = Field(default=None, description="The tenant ID.", alias="tenantId", json_schema_extra={"examples": [1]})
    is_active: Optional[StrictBool] = Field(default=None, description="Specifies if the user is active or not.", alias="isActive", json_schema_extra={"examples": [True]})
    culture_name: Optional[StrictStr] = Field(default=None, description="The user culture code.", alias="cultureName", json_schema_extra={"examples": ["en-US"]})
    mobile_phone: Optional[StrictStr] = Field(default=None, description="The user mobile phone.", alias="mobilePhone", json_schema_extra={"examples": ["+1234567890"]})
    mobile_phone_activation_status: Optional[MobilePhoneActivationStatus] = Field(default=None, description="The user mobile phone activation status.", alias="mobilePhoneActivationStatus")
    sid: Optional[StrictStr] = Field(default=None, description="The LDAP user identifier.", json_schema_extra={"examples": ["S-1-5-21-3623811015-3361044348-30300820-1013"]})
    ldap_qouta: Optional[StrictInt] = Field(default=None, description="The LDAP user quota attribute.", alias="ldapQouta", json_schema_extra={"examples": [1073741824]})
    sso_name_id: Optional[StrictStr] = Field(default=None, description="The SSO SAML user identifier.", alias="ssoNameId", json_schema_extra={"examples": ["johndoe@example.com"]})
    sso_session_id: Optional[StrictStr] = Field(default=None, description="The SSO SAML user session identifier.", alias="ssoSessionId", json_schema_extra={"examples": ["_1a2b3c4d5e6f7g8h9i0j"]})
    create_date: Optional[datetime] = Field(default=None, description="The date and time when the user account was created.", alias="createDate", json_schema_extra={"examples": ["2020-01-15T00:00:00Z"]})
    created_by: Optional[UUID] = Field(default=None, description="The ID of the user who created the current user account.", alias="createdBy", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    spam: Optional[StrictBool] = Field(default=None, description="Specifies if tips, updates and offers are allowed to be sent to the user or not.", json_schema_extra={"examples": [False]})
    check_activation: Optional[StrictBool] = Field(default=None, description="Indicates whether the activation status of the employee or recipient is unchecked or inactive.  Depending on the context, this property evaluates the activation or eligibility status accordingly.", alias="checkActivation", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["id", "firstName", "lastName", "userName", "birthDate", "sex", "status", "activationStatus", "terminatedDate", "title", "workFromDate", "email", "contacts", "contactsList", "location", "notes", "removed", "lastModified", "tenantId", "isActive", "cultureName", "mobilePhone", "mobilePhoneActivationStatus", "sid", "ldapQouta", "ssoNameId", "ssoSessionId", "createDate", "createdBy", "spam", "checkActivation"]

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
        """Create an instance of UserInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "is_active",
            "check_activation",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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

        # set to None if birth_date (nullable) is None
        # and model_fields_set contains the field
        if self.birth_date is None and "birth_date" in self.model_fields_set:
            _dict['birthDate'] = None

        # set to None if sex (nullable) is None
        # and model_fields_set contains the field
        if self.sex is None and "sex" in self.model_fields_set:
            _dict['sex'] = None

        # set to None if terminated_date (nullable) is None
        # and model_fields_set contains the field
        if self.terminated_date is None and "terminated_date" in self.model_fields_set:
            _dict['terminatedDate'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if work_from_date (nullable) is None
        # and model_fields_set contains the field
        if self.work_from_date is None and "work_from_date" in self.model_fields_set:
            _dict['workFromDate'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if contacts (nullable) is None
        # and model_fields_set contains the field
        if self.contacts is None and "contacts" in self.model_fields_set:
            _dict['contacts'] = None

        # set to None if contacts_list (nullable) is None
        # and model_fields_set contains the field
        if self.contacts_list is None and "contacts_list" in self.model_fields_set:
            _dict['contactsList'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        # set to None if culture_name (nullable) is None
        # and model_fields_set contains the field
        if self.culture_name is None and "culture_name" in self.model_fields_set:
            _dict['cultureName'] = None

        # set to None if mobile_phone (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_phone is None and "mobile_phone" in self.model_fields_set:
            _dict['mobilePhone'] = None

        # set to None if sid (nullable) is None
        # and model_fields_set contains the field
        if self.sid is None and "sid" in self.model_fields_set:
            _dict['sid'] = None

        # set to None if sso_name_id (nullable) is None
        # and model_fields_set contains the field
        if self.sso_name_id is None and "sso_name_id" in self.model_fields_set:
            _dict['ssoNameId'] = None

        # set to None if sso_session_id (nullable) is None
        # and model_fields_set contains the field
        if self.sso_session_id is None and "sso_session_id" in self.model_fields_set:
            _dict['ssoSessionId'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['createdBy'] = None

        # set to None if spam (nullable) is None
        # and model_fields_set contains the field
        if self.spam is None and "spam" in self.model_fields_set:
            _dict['spam'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserInfo from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "userName": obj.get("userName"),
            "birthDate": obj.get("birthDate"),
            "sex": obj.get("sex"),
            "status": obj.get("status"),
            "activationStatus": obj.get("activationStatus"),
            "terminatedDate": obj.get("terminatedDate"),
            "title": obj.get("title"),
            "workFromDate": obj.get("workFromDate"),
            "email": obj.get("email"),
            "contacts": obj.get("contacts"),
            "contactsList": obj.get("contactsList"),
            "location": obj.get("location"),
            "notes": obj.get("notes"),
            "removed": obj.get("removed"),
            "lastModified": obj.get("lastModified"),
            "tenantId": obj.get("tenantId"),
            "isActive": obj.get("isActive"),
            "cultureName": obj.get("cultureName"),
            "mobilePhone": obj.get("mobilePhone"),
            "mobilePhoneActivationStatus": obj.get("mobilePhoneActivationStatus"),
            "sid": obj.get("sid"),
            "ldapQouta": obj.get("ldapQouta"),
            "ssoNameId": obj.get("ssoNameId"),
            "ssoSessionId": obj.get("ssoSessionId"),
            "createDate": obj.get("createDate"),
            "createdBy": obj.get("createdBy"),
            "spam": obj.get("spam"),
            "checkActivation": obj.get("checkActivation")
        })
        return _obj


