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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DefaultTemplateItemDto(BaseModel):
    """
    Default template setting
    """ # noqa: E501
    selected_file: Optional[StrictInt] = Field(default=None, description="File id to use as a default template", alias="selectedFile", json_schema_extra={"examples": [123]})
    file_extension: Optional[StrictStr] = Field(description="Extension of a default template", alias="fileExtension", json_schema_extra={"examples": [".docx"]})
    file_title: Optional[StrictStr] = Field(default=None, description="Title of a default template", alias="fileTitle", json_schema_extra={"examples": ["Default Template"]})
    last_modified: Optional[datetime] = Field(default=None, description="Last modified date of a default template", alias="lastModified", json_schema_extra={"examples": ["2025-01-01T00:00:00"]})
    file_size: Optional[StrictInt] = Field(default=None, description="Filesize (in bytes) of a default template", alias="fileSize", json_schema_extra={"examples": [1024]})
    view_url: Optional[StrictStr] = Field(default=None, description="View url of a default template", alias="viewUrl", json_schema_extra={"examples": ["http://localhost/template/view"]})
    __properties: ClassVar[List[str]] = ["selectedFile", "fileExtension", "fileTitle", "lastModified", "fileSize", "viewUrl"]

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
        """Create an instance of DefaultTemplateItemDto from a JSON string"""
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
        # set to None if selected_file (nullable) is None
        # and model_fields_set contains the field
        if self.selected_file is None and "selected_file" in self.model_fields_set:
            _dict['selectedFile'] = None

        # set to None if file_extension (nullable) is None
        # and model_fields_set contains the field
        if self.file_extension is None and "file_extension" in self.model_fields_set:
            _dict['fileExtension'] = None

        # set to None if file_title (nullable) is None
        # and model_fields_set contains the field
        if self.file_title is None and "file_title" in self.model_fields_set:
            _dict['fileTitle'] = None

        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and "last_modified" in self.model_fields_set:
            _dict['lastModified'] = None

        # set to None if file_size (nullable) is None
        # and model_fields_set contains the field
        if self.file_size is None and "file_size" in self.model_fields_set:
            _dict['fileSize'] = None

        # set to None if view_url (nullable) is None
        # and model_fields_set contains the field
        if self.view_url is None and "view_url" in self.model_fields_set:
            _dict['viewUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DefaultTemplateItemDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "selectedFile": obj.get("selectedFile"),
            "fileExtension": obj.get("fileExtension"),
            "fileTitle": obj.get("fileTitle"),
            "lastModified": obj.get("lastModified"),
            "fileSize": obj.get("fileSize"),
            "viewUrl": obj.get("viewUrl")
        })
        return _obj


