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
from docspace-api-python.models.ace_short_wrapper import AceShortWrapper
from docspace-api-python.models.editor_type import EditorType
from typing import Optional, Set
from typing_extensions import Self

class InfoConfigDto(BaseModel):
    """
    The information config parameters.
    """ # noqa: E501
    favorite: Optional[StrictBool] = Field(default=None, description="Specifies if the file is favorite or not.")
    folder: Optional[StrictStr] = Field(default=None, description="The folder of the file.")
    owner: Optional[StrictStr] = Field(default=None, description="The file owner.")
    sharing_settings: Optional[List[AceShortWrapper]] = Field(default=None, description="The sharing settings of the file.", alias="sharingSettings")
    type: Optional[EditorType] = None
    uploaded: Optional[StrictStr] = Field(default=None, description="The uploaded file.")
    __properties: ClassVar[List[str]] = ["favorite", "folder", "owner", "sharingSettings", "type", "uploaded"]

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
        """Create an instance of InfoConfigDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sharing_settings (list)
        _items = []
        if self.sharing_settings:
            for _item_sharing_settings in self.sharing_settings:
                if _item_sharing_settings:
                    _items.append(_item_sharing_settings.to_dict())
            _dict['sharingSettings'] = _items
        # set to None if favorite (nullable) is None
        # and model_fields_set contains the field
        if self.favorite is None and "favorite" in self.model_fields_set:
            _dict['favorite'] = None

        # set to None if folder (nullable) is None
        # and model_fields_set contains the field
        if self.folder is None and "folder" in self.model_fields_set:
            _dict['folder'] = None

        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and "owner" in self.model_fields_set:
            _dict['owner'] = None

        # set to None if sharing_settings (nullable) is None
        # and model_fields_set contains the field
        if self.sharing_settings is None and "sharing_settings" in self.model_fields_set:
            _dict['sharingSettings'] = None

        # set to None if uploaded (nullable) is None
        # and model_fields_set contains the field
        if self.uploaded is None and "uploaded" in self.model_fields_set:
            _dict['uploaded'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InfoConfigDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "favorite": obj.get("favorite"),
            "folder": obj.get("folder"),
            "owner": obj.get("owner"),
            "sharingSettings": [AceShortWrapper.from_dict(_item) for _item in obj["sharingSettings"]] if obj.get("sharingSettings") is not None else None,
            "type": obj.get("type"),
            "uploaded": obj.get("uploaded")
        })
        return _obj


