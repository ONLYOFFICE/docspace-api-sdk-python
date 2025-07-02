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
from docspace-api-python.models.document_config_dto import DocumentConfigDto
from docspace-api-python.models.editor_configuration_dto import EditorConfigurationDto
from docspace-api-python.models.editor_type import EditorType
from docspace-api-python.models.file_dto_integer import FileDtoInteger
from docspace-api-python.models.start_filling_mode import StartFillingMode
from typing import Optional, Set
from typing_extensions import Self

class ConfigurationDtoInteger(BaseModel):
    """
    The configuration parameters.
    """ # noqa: E501
    document: Optional[DocumentConfigDto] = None
    document_type: Optional[StrictStr] = Field(default=None, description="The document type.", alias="documentType")
    editor_config: Optional[EditorConfigurationDto] = Field(default=None, alias="editorConfig")
    editor_type: Optional[EditorType] = Field(default=None, alias="editorType")
    editor_url: Optional[StrictStr] = Field(default=None, description="The editor URL.", alias="editorUrl")
    token: Optional[StrictStr] = Field(default=None, description="The token of the file configuration.")
    type: Optional[StrictStr] = Field(default=None, description="The platform type.")
    file: Optional[FileDtoInteger] = None
    error_message: Optional[StrictStr] = Field(default=None, description="The error message.", alias="errorMessage")
    start_filling: Optional[StrictBool] = Field(default=None, description="Specifies if the file filling has started or not.", alias="startFilling")
    filling_status: Optional[StrictBool] = Field(default=None, description="The file filling status.", alias="fillingStatus")
    start_filling_mode: Optional[StartFillingMode] = Field(default=None, alias="startFillingMode")
    filling_session_id: Optional[StrictStr] = Field(default=None, description="The file filling session ID.", alias="fillingSessionId")
    __properties: ClassVar[List[str]] = ["document", "documentType", "editorConfig", "editorType", "editorUrl", "token", "type", "file", "errorMessage", "startFilling", "fillingStatus", "startFillingMode", "fillingSessionId"]

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
        """Create an instance of ConfigurationDtoInteger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict['document'] = self.document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of editor_config
        if self.editor_config:
            _dict['editorConfig'] = self.editor_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # set to None if document_type (nullable) is None
        # and model_fields_set contains the field
        if self.document_type is None and "document_type" in self.model_fields_set:
            _dict['documentType'] = None

        # set to None if editor_url (nullable) is None
        # and model_fields_set contains the field
        if self.editor_url is None and "editor_url" in self.model_fields_set:
            _dict['editorUrl'] = None

        # set to None if token (nullable) is None
        # and model_fields_set contains the field
        if self.token is None and "token" in self.model_fields_set:
            _dict['token'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        # set to None if start_filling (nullable) is None
        # and model_fields_set contains the field
        if self.start_filling is None and "start_filling" in self.model_fields_set:
            _dict['startFilling'] = None

        # set to None if filling_status (nullable) is None
        # and model_fields_set contains the field
        if self.filling_status is None and "filling_status" in self.model_fields_set:
            _dict['fillingStatus'] = None

        # set to None if filling_session_id (nullable) is None
        # and model_fields_set contains the field
        if self.filling_session_id is None and "filling_session_id" in self.model_fields_set:
            _dict['fillingSessionId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationDtoInteger from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "document": DocumentConfigDto.from_dict(obj["document"]) if obj.get("document") is not None else None,
            "documentType": obj.get("documentType"),
            "editorConfig": EditorConfigurationDto.from_dict(obj["editorConfig"]) if obj.get("editorConfig") is not None else None,
            "editorType": obj.get("editorType"),
            "editorUrl": obj.get("editorUrl"),
            "token": obj.get("token"),
            "type": obj.get("type"),
            "file": FileDtoInteger.from_dict(obj["file"]) if obj.get("file") is not None else None,
            "errorMessage": obj.get("errorMessage"),
            "startFilling": obj.get("startFilling"),
            "fillingStatus": obj.get("fillingStatus"),
            "startFillingMode": obj.get("startFillingMode"),
            "fillingSessionId": obj.get("fillingSessionId")
        })
        return _obj


