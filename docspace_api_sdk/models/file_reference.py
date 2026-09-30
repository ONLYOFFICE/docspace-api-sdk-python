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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.file_reference_data import FileReferenceData
from typing import Optional, Set
from typing_extensions import Self

class FileReference(BaseModel):
    """
    The file reference parameters.
    """ # noqa: E501
    reference_data: Optional[FileReferenceData] = Field(default=None, description="How this document is named when another spreadsheet refers to it. Send it back as it stands to resolve the  reference again.", alias="referenceData")
    error: Optional[StrictStr] = Field(default=None, description="Filled in when the reference resolved to nothing; the rest of the descriptor is then empty and must not be  handed to the editors.", json_schema_extra={"examples": ["File not found"]})
    path: Optional[StrictStr] = Field(default=None, description="The title of the document the reference resolved to.", json_schema_extra={"examples": ["Budget 2026.xlsx"]})
    url: Optional[StrictStr] = Field(default=None, description="Where the content is fetched from. It is addressed to the host the document service can reach, which on a  deployment with a private editor network is not the address a browser should follow.", json_schema_extra={"examples": ["https://portal.example.com/filehandler.ashx?action=download&fileid=512"]})
    file_type: Optional[StrictStr] = Field(default=None, description="The format the content is in, without the leading dot.", alias="fileType", json_schema_extra={"examples": ["xlsx"]})
    key: Optional[StrictStr] = Field(default=None, description="Identifies the exact revision to the editors: two clients that receive the same key read the same co-editing  session, and the key changes as soon as the document is saved.", json_schema_extra={"examples": ["1_512_3"]})
    link: Optional[StrictStr] = Field(default=None, description="The address of the document in the portal web editor - the link to put in front of a person, unlike the  download address above.", json_schema_extra={"examples": ["https://portal.example.com/doceditor?fileid=512"]})
    token: Optional[StrictStr] = Field(default=None, description="Signs this descriptor so that the editors can trust it. It stays empty on a portal that has no signature  secret configured for the document service.", json_schema_extra={"examples": ["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."]})
    __properties: ClassVar[List[str]] = ["referenceData", "error", "path", "url", "fileType", "key", "link", "token"]

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
        """Create an instance of FileReference from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reference_data
        if self.reference_data:
            _dict['referenceData'] = self.reference_data.to_dict()
        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if file_type (nullable) is None
        # and model_fields_set contains the field
        if self.file_type is None and "file_type" in self.model_fields_set:
            _dict['fileType'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if token (nullable) is None
        # and model_fields_set contains the field
        if self.token is None and "token" in self.model_fields_set:
            _dict['token'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileReference from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "referenceData": FileReferenceData.from_dict(obj["referenceData"]) if obj.get("referenceData") is not None else None,
            "error": obj.get("error"),
            "path": obj.get("path"),
            "url": obj.get("url"),
            "fileType": obj.get("fileType"),
            "key": obj.get("key"),
            "link": obj.get("link"),
            "token": obj.get("token")
        })
        return _obj


