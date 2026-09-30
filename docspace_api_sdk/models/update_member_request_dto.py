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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from docspace_api_sdk.models.contact import Contact
from typing import Optional, Set
from typing_extensions import Self

class UpdateMemberRequestDto(BaseModel):
    """
    The request parameters for updating the user information.
    """ # noqa: E501
    user_id: Optional[StrictStr] = Field(default=None, description="The account the change applies to. It is read from this body by `POST api/2.0/people/email`, while  `PUT api/2.0/people/{userid}` takes the account from the route and ignores this field.", alias="userId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    disable: Optional[StrictBool] = Field(default=None, description="Set it to true to give the account the `Terminated` status and end every session it has, and to false to  bring it back. It is applied only when the caller edits somebody else, and omitting it keeps the current  status.", json_schema_extra={"examples": [False]})
    email: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The new email address, up to 255 characters. It is read only by `POST api/2.0/people/email`, which either  mails a confirmation letter or, for an administrator acting on somebody else, applies the address at once;  `PUT api/2.0/people/{userid}` ignores it.", json_schema_extra={"examples": ["john.doe@example.com"]})
    is_user: Optional[StrictBool] = Field(default=None, description="Set it to true to turn the account into a guest and to false to turn it back into a member. Either direction  takes a seat and can answer 402, it is applied only when the caller edits somebody else, and a request to  make the portal owner, a DocSpace administrator or a module administrator a guest is ignored.", alias="isUser", json_schema_extra={"examples": [True]})
    first_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The new first name, up to 255 characters. It is applied only to the caller's own profile, is left alone on an  LDAP or SSO account, and a pair the portal does not accept as a name answers 400.", alias="firstName", json_schema_extra={"examples": ["John"]})
    last_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The new last name, up to 255 characters. It is applied only to the caller's own profile, is left alone on an  LDAP or SSO account, and a pair the portal does not accept as a name answers 400.", alias="lastName", json_schema_extra={"examples": ["Doe"]})
    department: Optional[List[UUID]] = Field(default=None, description="The groups the profile should belong to, by group ID, replacing the current ones. It is applied only to the  caller's own profile.", json_schema_extra={"examples": [["00000000-0000-0000-0000-000000000000"]]})
    location: Optional[StrictStr] = Field(default=None, description="The new free-text location shown on the profile. It is applied only to the caller's own profile and is left  alone on an LDAP or SSO account.", json_schema_extra={"examples": ["New York"]})
    comment: Optional[StrictStr] = Field(default=None, description="The new free-text note kept with the profile. It is applied only to the caller's own profile.", json_schema_extra={"examples": ["User comment"]})
    contacts: Optional[List[Contact]] = Field(default=None, description="The additional ways to reach the person, replacing the current ones. Each entry is a free-text type such as  `email`, `phone`, `skype` or `telegram` and its value, an entry with an empty value is dropped, and the field  is applied only to the caller's own profile.", json_schema_extra={"examples": [[{"type": "email", "value": "john.doe@example.com"}]]})
    files: Optional[StrictStr] = Field(default=None, description="The address the portal downloads the new avatar from. It is applied only to the caller's own profile, has to  use HTTPS unless the request itself came over HTTP, and passing the address the profile already uses  downloads nothing.", json_schema_extra={"examples": ["https://example.com/avatar.jpg"]})
    spam: Optional[StrictBool] = Field(default=None, description="Whether the account agrees to receive tips, updates and offers. It is applied only to the caller's own  profile, and omitting it on such a request stores false rather than keeping the current value.", json_schema_extra={"examples": [False]})
    __properties: ClassVar[List[str]] = ["userId", "disable", "email", "isUser", "firstName", "lastName", "department", "location", "comment", "contacts", "files", "spam"]

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
        """Create an instance of UpdateMemberRequestDto from a JSON string"""
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
        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['userId'] = None

        # set to None if disable (nullable) is None
        # and model_fields_set contains the field
        if self.disable is None and "disable" in self.model_fields_set:
            _dict['disable'] = None

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

        # set to None if spam (nullable) is None
        # and model_fields_set contains the field
        if self.spam is None and "spam" in self.model_fields_set:
            _dict['spam'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateMemberRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "userId": obj.get("userId"),
            "disable": obj.get("disable"),
            "email": obj.get("email"),
            "isUser": obj.get("isUser"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "department": obj.get("department"),
            "location": obj.get("location"),
            "comment": obj.get("comment"),
            "contacts": [Contact.from_dict(_item) for _item in obj["contacts"]] if obj.get("contacts") is not None else None,
            "files": obj.get("files"),
            "spam": obj.get("spam")
        })
        return _obj


