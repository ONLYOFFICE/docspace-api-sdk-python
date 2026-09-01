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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.encryption_key_dto import EncryptionKeyDto
from docspace_api_sdk.models.file_keys import FileKeys
from typing import Optional, Set
from typing_extensions import Self

class FileEncryptionInfoDto(BaseModel):
    """
    The encryption information of a file: the user key pairs and the per-user file keys.
    """ # noqa: E501
    user_keys: Optional[List[EncryptionKeyDto]] = Field(default=None, description="The key pairs of the users who have access to the file.", alias="userKeys")
    file_keys: Optional[List[FileKeys]] = Field(default=None, description="The file keys issued to those users.", alias="fileKeys")
    __properties: ClassVar[List[str]] = ["userKeys", "fileKeys"]

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
        """Create an instance of FileEncryptionInfoDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in user_keys (list)
        _items = []
        if self.user_keys:
            for _item_user_keys in self.user_keys:
                if _item_user_keys:
                    _items.append(_item_user_keys.to_dict())
            _dict['userKeys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in file_keys (list)
        _items = []
        if self.file_keys:
            for _item_file_keys in self.file_keys:
                if _item_file_keys:
                    _items.append(_item_file_keys.to_dict())
            _dict['fileKeys'] = _items
        # set to None if user_keys (nullable) is None
        # and model_fields_set contains the field
        if self.user_keys is None and "user_keys" in self.model_fields_set:
            _dict['userKeys'] = None

        # set to None if file_keys (nullable) is None
        # and model_fields_set contains the field
        if self.file_keys is None and "file_keys" in self.model_fields_set:
            _dict['fileKeys'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileEncryptionInfoDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "userKeys": [EncryptionKeyDto.from_dict(_item) for _item in obj["userKeys"]] if obj.get("userKeys") is not None else None,
            "fileKeys": [FileKeys.from_dict(_item) for _item in obj["fileKeys"]] if obj.get("fileKeys") is not None else None
        })
        return _obj


