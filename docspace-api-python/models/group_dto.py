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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace-api-python.models.employee_full_dto import EmployeeFullDto
from typing import Optional, Set
from typing_extensions import Self

class GroupDto(BaseModel):
    """
    The group parameters.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The group name.")
    parent: Optional[StrictStr] = Field(default=None, description="The parent group ID.")
    category: Optional[StrictStr] = Field(default=None, description="The group category ID.")
    id: Optional[StrictStr] = Field(default=None, description="The group ID.")
    is_ldap: Optional[StrictBool] = Field(default=None, description="Specifies if the LDAP settings are enabled for the group or not.", alias="isLDAP")
    manager: Optional[EmployeeFullDto] = None
    members: Optional[List[EmployeeFullDto]] = Field(default=None, description="The list of group members.")
    shared: Optional[StrictBool] = Field(default=None, description="Specifies whether the group can be shared or not.")
    members_count: Optional[StrictInt] = Field(default=None, description="The number of group members.", alias="membersCount")
    __properties: ClassVar[List[str]] = ["name", "parent", "category", "id", "isLDAP", "manager", "members", "shared", "membersCount"]

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
        """Create an instance of GroupDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of manager
        if self.manager:
            _dict['manager'] = self.manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item_members in self.members:
                if _item_members:
                    _items.append(_item_members.to_dict())
            _dict['members'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if parent (nullable) is None
        # and model_fields_set contains the field
        if self.parent is None and "parent" in self.model_fields_set:
            _dict['parent'] = None

        # set to None if members (nullable) is None
        # and model_fields_set contains the field
        if self.members is None and "members" in self.model_fields_set:
            _dict['members'] = None

        # set to None if shared (nullable) is None
        # and model_fields_set contains the field
        if self.shared is None and "shared" in self.model_fields_set:
            _dict['shared'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GroupDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "parent": obj.get("parent"),
            "category": obj.get("category"),
            "id": obj.get("id"),
            "isLDAP": obj.get("isLDAP"),
            "manager": EmployeeFullDto.from_dict(obj["manager"]) if obj.get("manager") is not None else None,
            "members": [EmployeeFullDto.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None,
            "shared": obj.get("shared"),
            "membersCount": obj.get("membersCount")
        })
        return _obj


