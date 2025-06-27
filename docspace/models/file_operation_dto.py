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
from docspace.models.file_entry_dto import FileEntryDto
from docspace.models.file_operation_type import FileOperationType
from typing import Optional, Set
from typing_extensions import Self

class FileOperationDto(BaseModel):
    """
    The file operation information.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The file operation ID.")
    operation: Optional[FileOperationType] = Field(default=None, alias="Operation")
    progress: Optional[StrictInt] = Field(default=None, description="The file operation progress in percentage.")
    error: Optional[StrictStr] = Field(default=None, description="The file operation error message.")
    processed: Optional[StrictStr] = Field(default=None, description="The file operation processing status.")
    finished: Optional[StrictBool] = Field(default=None, description="Specifies if the file operation is finished or not.")
    url: Optional[StrictStr] = Field(default=None, description="The file operation URL.")
    files: Optional[List[FileEntryDto]] = Field(default=None, description="The list of files of the file operation.")
    folders: Optional[List[FileEntryDto]] = Field(default=None, description="The list of folders of the file operation.")
    __properties: ClassVar[List[str]] = ["id", "Operation", "progress", "error", "processed", "finished", "url", "files", "folders"]

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
        """Create an instance of FileOperationDto from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if processed (nullable) is None
        # and model_fields_set contains the field
        if self.processed is None and "processed" in self.model_fields_set:
            _dict['processed'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if files (nullable) is None
        # and model_fields_set contains the field
        if self.files is None and "files" in self.model_fields_set:
            _dict['files'] = None

        # set to None if folders (nullable) is None
        # and model_fields_set contains the field
        if self.folders is None and "folders" in self.model_fields_set:
            _dict['folders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileOperationDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "Operation": obj.get("Operation"),
            "progress": obj.get("progress"),
            "error": obj.get("error"),
            "processed": obj.get("processed"),
            "finished": obj.get("finished"),
            "url": obj.get("url"),
            "files": [FileEntryDto.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None,
            "folders": [FileEntryDto.from_dict(_item) for _item in obj["folders"]] if obj.get("folders") is not None else None
        })
        return _obj


