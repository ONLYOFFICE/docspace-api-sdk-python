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
from docspace_api_sdk.models.document_config_dto import DocumentConfigDto
from docspace_api_sdk.models.editor_configuration_dto import EditorConfigurationDto
from docspace_api_sdk.models.editor_tool_call_state_dto import EditorToolCallStateDto
from docspace_api_sdk.models.editor_type import EditorType
from docspace_api_sdk.models.file_dto_integer import FileDtoInteger
from docspace_api_sdk.models.quota_scope import QuotaScope
from docspace_api_sdk.models.start_filling_mode import StartFillingMode
from typing import Optional, Set
from typing_extensions import Self

class ConfigurationDtoInteger(BaseModel):
    """
    The configuration parameters.
    """ # noqa: E501
    document: DocumentConfigDto = Field(description="The document configuration.")
    document_type: Optional[StrictStr] = Field(description="The document type.", alias="documentType", json_schema_extra={"examples": ["word"]})
    editor_config: EditorConfigurationDto = Field(description="The editor configuration.", alias="editorConfig")
    editor_type: EditorType = Field(description="The editor type.", alias="editorType")
    editor_url: Optional[StrictStr] = Field(description="The editor URL.", alias="editorUrl", json_schema_extra={"examples": ["http://localhost/editor"]})
    token: Optional[StrictStr] = Field(default=None, description="The token of the file configuration.", json_schema_extra={"examples": ["token-abc-123"]})
    type: Optional[StrictStr] = Field(default=None, description="The platform type.", json_schema_extra={"examples": ["desktop"]})
    file: FileDtoInteger = Field(description="The file parameters.")
    error_message: Optional[StrictStr] = Field(default=None, description="The error message.", alias="errorMessage", json_schema_extra={"examples": ["Configuration error"]})
    start_filling: Optional[StrictBool] = Field(default=None, description="Specifies if the file filling has started or not.", alias="startFilling", json_schema_extra={"examples": [False]})
    filling_status: Optional[StrictBool] = Field(default=None, description="The file filling status.", alias="fillingStatus", json_schema_extra={"examples": [False]})
    start_filling_mode: Optional[StartFillingMode] = Field(default=None, description="The start filling mode.", alias="startFillingMode")
    filling_session_id: Optional[StrictStr] = Field(default=None, description="The file filling session ID.", alias="fillingSessionId", json_schema_extra={"examples": ["session-123-456"]})
    quota_exceeded_scope: Optional[QuotaScope] = Field(default=None, description="Indicates which quota scope has been exceeded.", alias="quotaExceededScope")
    generation_tool_call_state: Optional[EditorToolCallStateDto] = Field(default=None, description="The generation tool call state. Used to run the agent flow in the editor.", alias="generationToolCallState")
    __properties: ClassVar[List[str]] = ["document", "documentType", "editorConfig", "editorType", "editorUrl", "token", "type", "file", "errorMessage", "startFilling", "fillingStatus", "startFillingMode", "fillingSessionId", "quotaExceededScope", "generationToolCallState"]

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
        # override the default output from pydantic by calling `to_dict()` of generation_tool_call_state
        if self.generation_tool_call_state:
            _dict['generationToolCallState'] = self.generation_tool_call_state.to_dict()
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
            "fillingSessionId": obj.get("fillingSessionId"),
            "quotaExceededScope": obj.get("quotaExceededScope"),
            "generationToolCallState": EditorToolCallStateDto.from_dict(obj["generationToolCallState"]) if obj.get("generationToolCallState") is not None else None
        })
        return _obj


