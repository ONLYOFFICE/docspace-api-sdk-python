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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.ai_file_entry_base_dto import AiFileEntryBaseDto
from docspace_api_sdk.models.ai_folder_dto_integer import AiFolderDtoInteger
from typing import Optional, Set
from typing_extensions import Self

class AiFolderContentDtoInteger(BaseModel):
    """
    The folder content information.
    """ # noqa: E501
    files: Optional[List[AiFileEntryBaseDto]] = Field(default=None, description="The list of files in the folder.", json_schema_extra={"examples": [[{"id": 10, "title": "document.docx"}]]})
    folders: Optional[List[AiFileEntryBaseDto]] = Field(default=None, description="The list of folders in the folder.", json_schema_extra={"examples": [[{"id": 20, "title": "My Folder"}]]})
    current: Optional[AiFolderDtoInteger] = Field(default=None, description="The current folder information.")
    path_parts: Optional[Any] = Field(alias="pathParts")
    start_index: Optional[StrictInt] = Field(default=None, description="The folder start index.", alias="startIndex", json_schema_extra={"examples": [0]})
    count: Optional[StrictInt] = Field(default=None, description="The number of folder elements.", json_schema_extra={"examples": [4]})
    total: StrictInt = Field(description="The total number of elements in the folder.", json_schema_extra={"examples": [4]})
    new: Optional[StrictInt] = Field(default=None, description="The new element index in the folder.", json_schema_extra={"examples": [0]})
    __properties: ClassVar[List[str]] = ["files", "folders", "current", "pathParts", "startIndex", "count", "total", "new"]

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
        """Create an instance of AiFolderContentDtoInteger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item_files in self.files:
                if _item_files:
                    _items.append(_item_files.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in folders (list)
        _items = []
        if self.folders:
            for _item_folders in self.folders:
                if _item_folders:
                    _items.append(_item_folders.to_dict())
            _dict['folders'] = _items
        # override the default output from pydantic by calling `to_dict()` of current
        if self.current:
            _dict['current'] = self.current.to_dict()
        # set to None if files (nullable) is None
        # and model_fields_set contains the field
        if self.files is None and "files" in self.model_fields_set:
            _dict['files'] = None

        # set to None if folders (nullable) is None
        # and model_fields_set contains the field
        if self.folders is None and "folders" in self.model_fields_set:
            _dict['folders'] = None

        # set to None if path_parts (nullable) is None
        # and model_fields_set contains the field
        if self.path_parts is None and "path_parts" in self.model_fields_set:
            _dict['pathParts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiFolderContentDtoInteger from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "files": [AiFileEntryBaseDto.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None,
            "folders": [AiFileEntryBaseDto.from_dict(_item) for _item in obj["folders"]] if obj.get("folders") is not None else None,
            "current": AiFolderDtoInteger.from_dict(obj["current"]) if obj.get("current") is not None else None,
            "pathParts": obj.get("pathParts"),
            "startIndex": obj.get("startIndex"),
            "count": obj.get("count"),
            "total": obj.get("total"),
            "new": obj.get("new")
        })
        return _obj


