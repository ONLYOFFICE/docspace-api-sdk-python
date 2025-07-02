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
from docspace-api-python.models.backup_storage_type import BackupStorageType
from docspace-api-python.models.item_key_value_pair_object_object import ItemKeyValuePairObjectObject
from typing import Optional, Set
from typing_extensions import Self

class BackupRestoreDto(BaseModel):
    """
    The backup restoring parameters.
    """ # noqa: E501
    backup_id: Optional[StrictStr] = Field(default=None, description="The backup ID.", alias="backupId")
    storage_type: Optional[BackupStorageType] = Field(default=None, alias="storageType")
    storage_params: Optional[List[ItemKeyValuePairObjectObject]] = Field(default=None, description="The backup storage parameters.", alias="storageParams")
    notify: Optional[StrictBool] = Field(default=None, description="Notifies users about the portal restoring process or not.")
    dump: Optional[StrictBool] = Field(default=None, description="Specifies if a dump will be created or not.")
    __properties: ClassVar[List[str]] = ["backupId", "storageType", "storageParams", "notify", "dump"]

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
        """Create an instance of BackupRestoreDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in storage_params (list)
        _items = []
        if self.storage_params:
            for _item_storage_params in self.storage_params:
                if _item_storage_params:
                    _items.append(_item_storage_params.to_dict())
            _dict['storageParams'] = _items
        # set to None if backup_id (nullable) is None
        # and model_fields_set contains the field
        if self.backup_id is None and "backup_id" in self.model_fields_set:
            _dict['backupId'] = None

        # set to None if storage_params (nullable) is None
        # and model_fields_set contains the field
        if self.storage_params is None and "storage_params" in self.model_fields_set:
            _dict['storageParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BackupRestoreDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backupId": obj.get("backupId"),
            "storageType": obj.get("storageType"),
            "storageParams": [ItemKeyValuePairObjectObject.from_dict(_item) for _item in obj["storageParams"]] if obj.get("storageParams") is not None else None,
            "notify": obj.get("notify"),
            "dump": obj.get("dump")
        })
        return _obj


