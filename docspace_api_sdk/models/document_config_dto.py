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
from docspace_api_sdk.models.file_reference_data import FileReferenceData
from docspace_api_sdk.models.info_config_dto import InfoConfigDto
from docspace_api_sdk.models.options import Options
from docspace_api_sdk.models.permissions_config import PermissionsConfig
from typing import Optional, Set
from typing_extensions import Self

class DocumentConfigDto(BaseModel):
    """
    The document itself as the editors address it: what to fetch, under which revision key, and what this caller may  do with it.
    """ # noqa: E501
    file_type: Optional[StrictStr] = Field(default=None, description="The format the editors treat the content as, without the leading dot. For a file that had to be converted this  is the format it was converted to, not the one it is stored under.", alias="fileType", json_schema_extra={"examples": ["docx"]})
    info: Optional[InfoConfigDto] = Field(default=None, description="The facts the editor information panel shows about the document.")
    is_linked_for_me: Optional[StrictBool] = Field(default=None, description="Whether the caller opened the original document rather than a link pointing at it, which matters only for  formats whose editing is restricted through links.", alias="isLinkedForMe", json_schema_extra={"examples": [False]})
    key: Optional[StrictStr] = Field(default=None, description="Identifies the exact revision to the editors: everyone who receives the same key joins the same co-editing  session, and the key changes as soon as the document is saved.", json_schema_extra={"examples": ["1_512_3"]})
    permissions: Optional[PermissionsConfig] = Field(default=None, description="What this caller may do inside the editor - edit, comment, review, fill, download, print, copy and chat.")
    shared_link_param: Optional[StrictStr] = Field(default=None, description="The name of the query parameter that carries the external share key. It is set only when the document was  opened through an external link.", alias="sharedLinkParam", json_schema_extra={"examples": ["share"]})
    shared_link_key: Optional[StrictStr] = Field(default=None, description="The external share key this opening runs under, empty when the caller opened the document as a portal member.  The editors pass it back on every request they make for the document.", alias="sharedLinkKey", json_schema_extra={"examples": ["HkQd9nT2"]})
    reference_data: Optional[FileReferenceData] = Field(default=None, description="How another spreadsheet names this document in a formula. Pass it to `POST api/2.0/files/file/referencedata`  to resolve such a reference.", alias="referenceData")
    title: Optional[StrictStr] = Field(default=None, description="The name the editors display. When a past version was opened, the moment that version was created is appended  to it in brackets.", json_schema_extra={"examples": ["Budget 2026.xlsx"]})
    url: Optional[StrictStr] = Field(default=None, description="Where the editors fetch the content. It is addressed to the host the document service can reach, which is not  necessarily the address a browser should follow.", json_schema_extra={"examples": ["https://portal.example.com/filehandler.ashx?action=download&fileid=512"]})
    is_form: Optional[StrictBool] = Field(default=None, description="Whether the document is a fillable PDF form. A PDF that the portal has never classified is inspected while the  configuration is built, so the answer is trustworthy even for a freshly uploaded file.", alias="isForm", json_schema_extra={"examples": [False]})
    options: Optional[Options] = Field(default=None, description="Extra instructions for the editors, currently the watermark to draw over the document. It is empty when the  room sets no watermark.")
    __properties: ClassVar[List[str]] = ["fileType", "info", "isLinkedForMe", "key", "permissions", "sharedLinkParam", "sharedLinkKey", "referenceData", "title", "url", "isForm", "options"]

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
        """Create an instance of DocumentConfigDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reference_data
        if self.reference_data:
            _dict['referenceData'] = self.reference_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        # set to None if file_type (nullable) is None
        # and model_fields_set contains the field
        if self.file_type is None and "file_type" in self.model_fields_set:
            _dict['fileType'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if shared_link_param (nullable) is None
        # and model_fields_set contains the field
        if self.shared_link_param is None and "shared_link_param" in self.model_fields_set:
            _dict['sharedLinkParam'] = None

        # set to None if shared_link_key (nullable) is None
        # and model_fields_set contains the field
        if self.shared_link_key is None and "shared_link_key" in self.model_fields_set:
            _dict['sharedLinkKey'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentConfigDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fileType": obj.get("fileType"),
            "info": InfoConfigDto.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "isLinkedForMe": obj.get("isLinkedForMe"),
            "key": obj.get("key"),
            "permissions": PermissionsConfig.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "sharedLinkParam": obj.get("sharedLinkParam"),
            "sharedLinkKey": obj.get("sharedLinkKey"),
            "referenceData": FileReferenceData.from_dict(obj["referenceData"]) if obj.get("referenceData") is not None else None,
            "title": obj.get("title"),
            "url": obj.get("url"),
            "isForm": obj.get("isForm"),
            "options": Options.from_dict(obj["options"]) if obj.get("options") is not None else None
        })
        return _obj


