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
from docspace_api_sdk.models.file_dto import FileDto
from docspace_api_sdk.models.quota_scope import QuotaScope
from docspace_api_sdk.models.start_filling_mode import StartFillingMode
from typing import Optional, Set
from typing_extensions import Self

class ConfigurationDto(BaseModel):
    """
    Everything an editor client needs in order to open one document: the document itself, the editor setup for this  caller, and the signature that lets the editors trust both.
    """ # noqa: E501
    document: DocumentConfigDto = Field(description="The document as the editors address it: its revision key, title, type, download address and the permissions of  this caller on it.")
    document_type: Optional[StrictStr] = Field(description="The editor family the file opens in - `word`, `cell`, `slide`, `pdf` or `diagram`. It comes back empty for a  format no editor handles.", alias="documentType", json_schema_extra={"examples": ["word"]})
    editor_config: EditorConfigurationDto = Field(description="How the editor is set up for this opening: the mode, the language, the interface customization, the callback  the editors save through, and the account they attribute changes to.", alias="editorConfig")
    editor_type: EditorType = Field(description="The layout the configuration was actually built for. It echoes the requested one except where the room  overruled it, as the templates folder does by forcing the embedded viewer.", alias="editorType")
    editor_url: Optional[StrictStr] = Field(description="The address of the editor api script the client has to load, with the shard key of this document already  appended. Load it as it is given rather than assembling it by hand.", alias="editorUrl", json_schema_extra={"examples": ["https://portal.example.com/web-apps/apps/api/documents/api.js?shardkey=1_512_3"]})
    token: Optional[StrictStr] = Field(default=None, description="Signs this whole configuration so that the editors can trust it; anything a client changes in the  configuration invalidates it. It stays empty on a portal that has no signature secret configured for the  document service.", json_schema_extra={"examples": ["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."]})
    type: Optional[StrictStr] = Field(default=None, description="The layout spelled as a lowercase word - `desktop`, `mobile` or `embedded` - the same value the editor type  carries as a number.", json_schema_extra={"examples": ["desktop"]})
    file: FileDto = Field(description="The file the configuration was built for, in the same shape the file listings report it.")
    error_message: Optional[StrictStr] = Field(default=None, description="Filled in when the document could not be prepared for opening; the rest of the configuration should then not  be handed to the editors.", alias="errorMessage", json_schema_extra={"examples": ["The file is being converted"]})
    start_filling: Optional[StrictBool] = Field(default=None, description="Whether this caller may start a filling session on the form from inside the editor. It stays empty when the  file is not a form opened where starting is possible at all.", alias="startFilling", json_schema_extra={"examples": [False]})
    filling_status: Optional[StrictBool] = Field(default=None, description="True once the caller holds a role in the running filling session of this form. It stays empty outside a  virtual data room, where roles are the only place it is set.", alias="fillingStatus", json_schema_extra={"examples": [False]})
    start_filling_mode: Optional[StartFillingMode] = Field(default=None, description="Which filling button the editor offers: none at all, sharing the form out for others to fill, starting a  filling session, or starting one inside the form-filling room.", alias="startFillingMode")
    filling_session_id: Optional[StrictStr] = Field(default=None, description="Identifies the filling session this opening belongs to, and is empty when the document is not opened as part  of one. Submissions made in the editor are collected under it.", alias="fillingSessionId", json_schema_extra={"examples": ["a1b2c3d4-0000-0000-0000-000000000000"]})
    quota_exceeded_scope: Optional[QuotaScope] = Field(default=None, description="Names the quota that ran out - the user, the room or the portal - and is set only when the document had to be  opened read-only because of it.", alias="quotaExceededScope")
    generation_tool_call_state: Optional[EditorToolCallStateDto] = Field(default=None, description="The generation the editor should run as soon as the document opens. It is set only for a document an AI agent  produced and left waiting for its content, and is empty for every other file.", alias="generationToolCallState")
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
        """Create an instance of ConfigurationDto from a JSON string"""
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
        """Create an instance of ConfigurationDto from a dict"""
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
            "file": FileDto.from_dict(obj["file"]) if obj.get("file") is not None else None,
            "errorMessage": obj.get("errorMessage"),
            "startFilling": obj.get("startFilling"),
            "fillingStatus": obj.get("fillingStatus"),
            "startFillingMode": obj.get("startFillingMode"),
            "fillingSessionId": obj.get("fillingSessionId"),
            "quotaExceededScope": obj.get("quotaExceededScope"),
            "generationToolCallState": EditorToolCallStateDto.from_dict(obj["generationToolCallState"]) if obj.get("generationToolCallState") is not None else None
        })
        return _obj


