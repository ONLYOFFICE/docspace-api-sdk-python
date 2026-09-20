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
from docspace_api_sdk.models.backup_storage_type import BackupStorageType
from docspace_api_sdk.models.item_key_value_pair_object_object import ItemKeyValuePairObjectObject
from typing import Optional, Set
from typing_extensions import Self

class BackupRestoreDto(BaseModel):
    """
    The request parameters for restoring a portal from a backup.
    """ # noqa: E501
    backup_id: Optional[StrictStr] = Field(description="The ID of the backup to restore from, as listed by `GET api/2.0/backup/getbackuphistory`. Send  anything that is not a GUID to restore from a file given by `storageParams` instead; an all-zero GUID  selects neither, because it parses as a GUID and then matches no record.", alias="backupId", json_schema_extra={"examples": ["11111111-1111-1111-1111-111111111111"]})
    storage_type: Optional[BackupStorageType] = Field(default=None, description="The storage the archive is read from. It defaults to `Documents` and is only used when `backupId` is  not a GUID, because a known backup carries the storage of its own record.", alias="storageType")
    storage_params: Optional[List[ItemKeyValuePairObjectObject]] = Field(default=None, description="The location of the archive, as an array of key and value pairs. The key read here is `filePath` -  not the `folderId` a backup is started with - and it holds a file ID for `Documents`, a  provider-specific file ID for `ThridpartyDocuments` and a path on the server for `Local`. It is only  used when `backupId` is not a GUID.", alias="storageParams", json_schema_extra={"examples": [[{"key": "filePath", "value": "1234"}]]})
    notify: Optional[StrictBool] = Field(default=None, description="Chooses who is emailed when the restoring starts and when it finishes: every active user of the  portal when true, and its owner alone when false. Mail goes only to accounts that have been  activated, so this decides the audience rather than whether anybody is notified at all.", json_schema_extra={"examples": [True]})
    dump: Optional[StrictBool] = Field(default=None, description="Restores the whole server rather than this one portal. It requires the space access permission.", json_schema_extra={"examples": [False]})
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


