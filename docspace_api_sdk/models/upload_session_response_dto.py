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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.file_dto import FileDto
from typing import Optional, Set
from typing_extensions import Self

class UploadSessionResponseDto(BaseModel):
    """
    How far a chunked upload has got, and the file it produced once the last byte has arrived.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The file the parts are being written into. An upload that took over a file of the same title carries it from  the start, while an upload that creates a new file has nothing to name yet and reports 0 until the answer that  sets `uploaded` to true.", json_schema_extra={"examples": [1234]})
    folder_id: Optional[StrictInt] = Field(default=None, description="The folder receiving the file. It is the folder the upload was reserved against, or the sub-folder created for  it when the reservation declared a relative path.", alias="folderId", json_schema_extra={"examples": [10]})
    version: Optional[StrictInt] = Field(default=None, description="The revision the content is being written as: 1 for a file that did not exist, the next number when the upload  took over a file of the same title, and the unchanged current number for an upload opened over an existing  file, which replaces its content in place.", json_schema_extra={"examples": [1]})
    title: Optional[StrictStr] = Field(default=None, description="The title the file is stored under, after characters a title cannot hold were replaced and, where a second  copy was asked for, a numeric suffix was added - so it can differ from the name that was sent.", json_schema_extra={"examples": ["Quarterly report.docx"]})
    provider_key: Optional[StrictStr] = Field(default=None, description="The third-party service holding the destination, such as `GoogleDrive` or `OneDrive`, and null for a folder  stored on the portal itself.", alias="providerKey", json_schema_extra={"examples": ["GoogleDrive"]})
    uploaded: Optional[StrictBool] = Field(default=None, description="False while bytes are still missing, when the answer only reports progress; true in the answer that reports  the stored file, which is also the answer that arrives with 201.", json_schema_extra={"examples": [False]})
    file: Optional[FileDto] = Field(default=None, description="The file as it stands. It is filled in both answers, but while `uploaded` is false it describes a file that  has not been written yet, so its identifier, size and links are only worth reading once that flag turns true.")
    __properties: ClassVar[List[str]] = ["id", "folderId", "version", "title", "providerKey", "uploaded", "file"]

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
        """Create an instance of UploadSessionResponseDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if provider_key (nullable) is None
        # and model_fields_set contains the field
        if self.provider_key is None and "provider_key" in self.model_fields_set:
            _dict['providerKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UploadSessionResponseDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "folderId": obj.get("folderId"),
            "version": obj.get("version"),
            "title": obj.get("title"),
            "providerKey": obj.get("providerKey"),
            "uploaded": obj.get("uploaded"),
            "file": FileDto.from_dict(obj["file"]) if obj.get("file") is not None else None
        })
        return _obj


