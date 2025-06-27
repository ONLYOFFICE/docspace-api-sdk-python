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
from docspace.models.copy_as_json_element_dest_folder_id import CopyAsJsonElementDestFolderId
from typing import Optional, Set
from typing_extensions import Self

class CopyAsJsonElement(BaseModel):
    """
    The parameters for copying a file.
    """ # noqa: E501
    dest_title: Optional[StrictStr] = Field(description="The copied file name.", alias="destTitle")
    dest_folder_id: CopyAsJsonElementDestFolderId = Field(alias="destFolderId")
    enable_external_ext: Optional[StrictBool] = Field(default=None, description="Specifies whether to allow creating the copied file of an external extension or not.", alias="enableExternalExt")
    password: Optional[StrictStr] = Field(default=None, description="The copied file password.")
    to_form: Optional[StrictBool] = Field(default=None, description="Specifies whether to convert the file to form or not.", alias="toForm")
    __properties: ClassVar[List[str]] = ["destTitle", "destFolderId", "enableExternalExt", "password", "toForm"]

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
        """Create an instance of CopyAsJsonElement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dest_folder_id
        if self.dest_folder_id:
            _dict['destFolderId'] = self.dest_folder_id.to_dict()
        # set to None if dest_title (nullable) is None
        # and model_fields_set contains the field
        if self.dest_title is None and "dest_title" in self.model_fields_set:
            _dict['destTitle'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CopyAsJsonElement from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destTitle": obj.get("destTitle"),
            "destFolderId": CopyAsJsonElementDestFolderId.from_dict(obj["destFolderId"]) if obj.get("destFolderId") is not None else None,
            "enableExternalExt": obj.get("enableExternalExt"),
            "password": obj.get("password"),
            "toForm": obj.get("toForm")
        })
        return _obj


