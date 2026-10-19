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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.convert_document_layout_request import ConvertDocumentLayoutRequest
from docspace_api_sdk.models.convert_document_renderer_request import ConvertDocumentRendererRequest
from docspace_api_sdk.models.convert_pdf_request import ConvertPdfRequest
from docspace_api_sdk.models.convert_spreadsheet_layout_request import ConvertSpreadsheetLayoutRequest
from docspace_api_sdk.models.convert_thumbnail_request import ConvertThumbnailRequest
from typing import Optional, Set
from typing_extensions import Self

class ConvertFileRequestDto(BaseModel):
    """
    What to convert, where to keep the result, and the parameters the document service is handed. Everything below the  first two fields is the contract of the document service itself, named and shaped exactly as it names it, so that  the portal passes the request on rather than translating it. What the portal can read off the file - its format,  its name and the key of its revision - is not asked for and cannot be overridden.
    """ # noqa: E501
    file_id: StrictInt = Field(description="The id of the portal file to convert, as reported by a folder listing such as `GET api/2.0/files/{folderId}`.", alias="fileId", json_schema_extra={"examples": [1234]})
    folder_id: Optional[StrictInt] = Field(default=None, description="The id of the folder to save the converted file in, as reported by a folder listing such as  `GET api/2.0/files/{folderId}`.", alias="folderId", json_schema_extra={"examples": [5678]})
    code_page: Optional[StrictInt] = Field(default=None, description="The encoding of a csv or txt source, as a code page number: 1251 for Cyrillic, 65001 for UTF-8, and so on.  Leaving it out lets the document service guess, which garbles non-latin text.", alias="codePage", json_schema_extra={"examples": [65001]})
    delimiter: Optional[StrictInt] = Field(default=None, description="The character separating the values of a csv source: 0 - none, 1 - tab, 2 - semicolon, 3 - colon, 4 - comma,  5 - space.", json_schema_extra={"examples": [4]})
    document_layout: Optional[ConvertDocumentLayoutRequest] = Field(default=None, description="The layout of forms printed as pdf documents or images.", alias="documentLayout")
    document_renderer: Optional[ConvertDocumentRendererRequest] = Field(default=None, description="How the text of a pdf, xps or oxps source is read back.", alias="documentRenderer")
    outputtype: Optional[StrictStr] = Field(description="The extension of the format to convert to, without the dot. The formats a source can become are listed under  `extsConvertible` in `GET api/2.0/files/settings`, keyed by the source extension, both with a leading dot there.", json_schema_extra={"examples": ["pdf"]})
    password: Optional[StrictStr] = Field(default=None, description="The password of the source document, for a document that is protected with one.", json_schema_extra={"examples": ["qwerty"]})
    region: Optional[StrictStr] = Field(default=None, description="The culture code whose currency, date and time formats a spreadsheet converted to PDF is shown in.", json_schema_extra={"examples": ["en-US"]})
    thumbnail: Optional[ConvertThumbnailRequest] = Field(default=None, description="How a thumbnail is fitted, when the target format is an image.")
    spreadsheet_layout: Optional[ConvertSpreadsheetLayoutRequest] = Field(default=None, description="How a spreadsheet is laid out on the page, when it is converted to PDF.", alias="spreadsheetLayout")
    pdf: Optional[ConvertPdfRequest] = Field(default=None, description="The PDF settings, used when the target format is PDF.")
    __properties: ClassVar[List[str]] = ["fileId", "folderId", "codePage", "delimiter", "documentLayout", "documentRenderer", "outputtype", "password", "region", "thumbnail", "spreadsheetLayout", "pdf"]

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
        """Create an instance of ConvertFileRequestDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of document_layout
        if self.document_layout:
            _dict['documentLayout'] = self.document_layout.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_renderer
        if self.document_renderer:
            _dict['documentRenderer'] = self.document_renderer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of thumbnail
        if self.thumbnail:
            _dict['thumbnail'] = self.thumbnail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spreadsheet_layout
        if self.spreadsheet_layout:
            _dict['spreadsheetLayout'] = self.spreadsheet_layout.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pdf
        if self.pdf:
            _dict['pdf'] = self.pdf.to_dict()
        # set to None if folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.folder_id is None and "folder_id" in self.model_fields_set:
            _dict['folderId'] = None

        # set to None if code_page (nullable) is None
        # and model_fields_set contains the field
        if self.code_page is None and "code_page" in self.model_fields_set:
            _dict['codePage'] = None

        # set to None if delimiter (nullable) is None
        # and model_fields_set contains the field
        if self.delimiter is None and "delimiter" in self.model_fields_set:
            _dict['delimiter'] = None

        # set to None if outputtype (nullable) is None
        # and model_fields_set contains the field
        if self.outputtype is None and "outputtype" in self.model_fields_set:
            _dict['outputtype'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConvertFileRequestDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fileId": obj.get("fileId"),
            "folderId": obj.get("folderId"),
            "codePage": obj.get("codePage"),
            "delimiter": obj.get("delimiter"),
            "documentLayout": ConvertDocumentLayoutRequest.from_dict(obj["documentLayout"]) if obj.get("documentLayout") is not None else None,
            "documentRenderer": ConvertDocumentRendererRequest.from_dict(obj["documentRenderer"]) if obj.get("documentRenderer") is not None else None,
            "outputtype": obj.get("outputtype"),
            "password": obj.get("password"),
            "region": obj.get("region"),
            "thumbnail": ConvertThumbnailRequest.from_dict(obj["thumbnail"]) if obj.get("thumbnail") is not None else None,
            "spreadsheetLayout": ConvertSpreadsheetLayoutRequest.from_dict(obj["spreadsheetLayout"]) if obj.get("spreadsheetLayout") is not None else None,
            "pdf": ConvertPdfRequest.from_dict(obj["pdf"]) if obj.get("pdf") is not None else None
        })
        return _obj


