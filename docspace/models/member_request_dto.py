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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from docspace.models.api_date_time import ApiDateTime
from docspace.models.contact import Contact
from docspace.models.employee_type import EmployeeType
from docspace.models.sex_enum import SexEnum
from typing import Optional, Set
from typing_extensions import Self

class MemberRequestDto(BaseModel):
    """
    The user request parameters.
    """ # noqa: E501
    password: Optional[StrictStr] = Field(default=None, description="The user password.")
    password_hash: Optional[StrictStr] = Field(default=None, description="The user password hash.", alias="passwordHash")
    email: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The user email address.")
    type: Optional[EmployeeType] = None
    is_user: Optional[StrictBool] = Field(default=None, description="Specifies if this is a guest or a user.", alias="isUser")
    first_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The user first name.", alias="firstName")
    last_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The user last name.", alias="lastName")
    department: Optional[List[StrictStr]] = Field(default=None, description="The list of the user departments IDs.")
    title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The user title.")
    location: Optional[StrictStr] = Field(default=None, description="The user location.")
    sex: Optional[SexEnum] = None
    birthday: Optional[ApiDateTime] = None
    worksfrom: Optional[ApiDateTime] = None
    comment: Optional[StrictStr] = Field(default=None, description="The user comment.")
    contacts: Optional[List[Contact]] = Field(default=None, description="The list of the user contacts.")
    files: Optional[StrictStr] = Field(default=None, description="The avatar photo URL.")
    from_invite_link: Optional[StrictBool] = Field(default=None, description="Specifies if the user is added via the invitation link or not.", alias="fromInviteLink")
    key: Optional[StrictStr] = Field(default=None, description="The user key.")
    culture_name: Optional[StrictStr] = Field(default=None, description="The user culture code.", alias="cultureName")
    target: Optional[StrictStr] = Field(default=None, description="The user target ID.")
    spam: Optional[StrictBool] = Field(default=None, description="Specifies if tips, updates and offers are allowed to be sent to the user or not.")
    __properties: ClassVar[List[str]] = ["password", "passwordHash", "email", "type", "isUser", "firstName", "lastName", "department", "title", "location", "sex", "birthday", "worksfrom", "comment", "contacts", "files", "fromInviteLink", "key", "cultureName", "target", "spam"]

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
        """Create an instance of MemberRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of birthday
        if self.birthday:
            _dict['birthday'] = self.birthday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of worksfrom
        if self.worksfrom:
            _dict['worksfrom'] = self.worksfrom.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in contacts (list)
        _items = []
        if self.contacts:
            for _item_contacts in self.contacts:
                if _item_contacts:
                    _items.append(_item_contacts.to_dict())
            _dict['contacts'] = _items
        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if password_hash (nullable) is None
        # and model_fields_set contains the field
        if self.password_hash is None and "password_hash" in self.model_fields_set:
            _dict['passwordHash'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if is_user (nullable) is None
        # and model_fields_set contains the field
        if self.is_user is None and "is_user" in self.model_fields_set:
            _dict['isUser'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if department (nullable) is None
        # and model_fields_set contains the field
        if self.department is None and "department" in self.model_fields_set:
            _dict['department'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if contacts (nullable) is None
        # and model_fields_set contains the field
        if self.contacts is None and "contacts" in self.model_fields_set:
            _dict['contacts'] = None

        # set to None if files (nullable) is None
        # and model_fields_set contains the field
        if self.files is None and "files" in self.model_fields_set:
            _dict['files'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if culture_name (nullable) is None
        # and model_fields_set contains the field
        if self.culture_name is None and "culture_name" in self.model_fields_set:
            _dict['cultureName'] = None

        # set to None if spam (nullable) is None
        # and model_fields_set contains the field
        if self.spam is None and "spam" in self.model_fields_set:
            _dict['spam'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MemberRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "password": obj.get("password"),
            "passwordHash": obj.get("passwordHash"),
            "email": obj.get("email"),
            "type": obj.get("type"),
            "isUser": obj.get("isUser"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "department": obj.get("department"),
            "title": obj.get("title"),
            "location": obj.get("location"),
            "sex": obj.get("sex"),
            "birthday": ApiDateTime.from_dict(obj["birthday"]) if obj.get("birthday") is not None else None,
            "worksfrom": ApiDateTime.from_dict(obj["worksfrom"]) if obj.get("worksfrom") is not None else None,
            "comment": obj.get("comment"),
            "contacts": [Contact.from_dict(_item) for _item in obj["contacts"]] if obj.get("contacts") is not None else None,
            "files": obj.get("files"),
            "fromInviteLink": obj.get("fromInviteLink"),
            "key": obj.get("key"),
            "cultureName": obj.get("cultureName"),
            "target": obj.get("target"),
            "spam": obj.get("spam")
        })
        return _obj


