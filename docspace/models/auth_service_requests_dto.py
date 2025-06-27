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
from docspace.models.auth_key import AuthKey
from typing import Optional, Set
from typing_extensions import Self

class AuthServiceRequestsDto(BaseModel):
    """
    The request parameters for handling the authorization service.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the authentication service.")
    title: Optional[StrictStr] = Field(default=None, description="The user-friendly display title of the authentication service.")
    description: Optional[StrictStr] = Field(default=None, description="The brief description of the authentication service.")
    instruction: Optional[StrictStr] = Field(default=None, description="The detailed instructions for configuring or using the authentication service.")
    can_set: Optional[StrictBool] = Field(default=None, description="Specifies whether the authentication service can be configured by the user.", alias="canSet")
    props: Optional[List[AuthKey]] = Field(default=None, description="The collection of authorization keys associated with the authentication service.")
    __properties: ClassVar[List[str]] = ["name", "title", "description", "instruction", "canSet", "props"]

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
        """Create an instance of AuthServiceRequestsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in props (list)
        _items = []
        if self.props:
            for _item_props in self.props:
                if _item_props:
                    _items.append(_item_props.to_dict())
            _dict['props'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if instruction (nullable) is None
        # and model_fields_set contains the field
        if self.instruction is None and "instruction" in self.model_fields_set:
            _dict['instruction'] = None

        # set to None if props (nullable) is None
        # and model_fields_set contains the field
        if self.props is None and "props" in self.model_fields_set:
            _dict['props'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthServiceRequestsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "instruction": obj.get("instruction"),
            "canSet": obj.get("canSet"),
            "props": [AuthKey.from_dict(_item) for _item in obj["props"]] if obj.get("props") is not None else None
        })
        return _obj


