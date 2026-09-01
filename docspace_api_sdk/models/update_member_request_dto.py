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
    user_id: Optional[StrictStr] = Field(default=None, description="The user ID.", alias="userId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    disable: Optional[StrictBool] = Field(default=None, description="Specifies whether to disable a user or not.", json_schema_extra={"examples": [False]})
    email: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The user email address.", json_schema_extra={"examples": ["john.doe@example.com"]})
    is_user: Optional[StrictBool] = Field(default=None, description="Specifies if this is a guest or a user.", alias="isUser", json_schema_extra={"examples": [True]})
    first_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The user first name.", alias="firstName", json_schema_extra={"examples": ["John"]})
    last_name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = Field(default=None, description="The user last name.", alias="lastName", json_schema_extra={"examples": ["Doe"]})
    department: Optional[List[UUID]] = Field(default=None, description="The list of the user departments.", json_schema_extra={"examples": [["00000000-0000-0000-0000-000000000000"]]})
    location: Optional[StrictStr] = Field(default=None, description="The user location.", json_schema_extra={"examples": ["New York"]})
    comment: Optional[StrictStr] = Field(default=None, description="The user comment.", json_schema_extra={"examples": ["User comment"]})
    contacts: Optional[List[Contact]] = Field(default=None, description="The list of the user contacts.", json_schema_extra={"examples": [[{"type": "email", "value": "john.doe@example.com"}]]})
    files: Optional[StrictStr] = Field(default=None, description="The user avatar photo URL.", json_schema_extra={"examples": ["https://example.com/avatar.jpg"]})
    spam: Optional[StrictBool] = Field(default=None, description="Specifies if tips, updates and offers are allowed to be sent to the user or not.", json_schema_extra={"examples": [False]})
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


