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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.draft_location_integer import DraftLocationInteger
from docspace_api_sdk.models.employee_dto import EmployeeDto
from docspace_api_sdk.models.file_dto_integer_all_of_view_accessibility import FileDtoIntegerAllOfViewAccessibility
from docspace_api_sdk.models.file_entry_dto_integer_all_of_available_share_rights import FileEntryDtoIntegerAllOfAvailableShareRights
from docspace_api_sdk.models.file_entry_dto_integer_all_of_security import FileEntryDtoIntegerAllOfSecurity
from docspace_api_sdk.models.file_entry_dto_integer_all_of_share_settings import FileEntryDtoIntegerAllOfShareSettings
from docspace_api_sdk.models.file_entry_type import FileEntryType
from docspace_api_sdk.models.file_share import FileShare
from docspace_api_sdk.models.file_status import FileStatus
from docspace_api_sdk.models.file_type import FileType
from docspace_api_sdk.models.folder_type import FolderType
from docspace_api_sdk.models.form_filling_status import FormFillingStatus
from docspace_api_sdk.models.size import Size
from docspace_api_sdk.models.thumbnail import Thumbnail
from docspace_api_sdk.models.vectorization_status import VectorizationStatus
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field
from docspace_api_sdk.models.file_entry_dto_integer import FileEntryDtoInteger

class FileDtoInteger(FileEntryDtoInteger):
    """
    The file parameters.
    """

    folder_id: Optional[StrictInt] = Field(default=None, description="The folder ID where the file is located.", alias="folderId", json_schema_extra={"examples": [10]})
    version: Optional[StrictInt] = Field(default=None, description="The file version.", json_schema_extra={"examples": [3]})
    version_group: Optional[StrictInt] = Field(default=None, description="The version group of the file.", alias="versionGroup", json_schema_extra={"examples": [1]})
    content_length: Optional[StrictStr] = Field(default=None, description="The content length of the file.", alias="contentLength", json_schema_extra={"examples": ["12345"]})
    pure_content_length: Optional[StrictInt] = Field(default=None, description="The pure content length of the file.", alias="pureContentLength", json_schema_extra={"examples": [12345]})
    file_status: Optional[FileStatus] = Field(default=None, description="The current status of the file.", alias="fileStatus")
    editing_by: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="The list of users editing the file.", alias="editingBy", json_schema_extra={"examples": [{"00000000-0000-0000-0000-000000000000": "John Doe"}]})
    mute: Optional[StrictBool] = Field(default=None, description="Specifies if the file is muted or not.", json_schema_extra={"examples": [False]})
    view_url: Optional[StrictStr] = Field(default=None, description="The URL link to view the file.", alias="viewUrl", json_schema_extra={"examples": ["https://www.onlyoffice.com/viewfile?fileid=2221"]})
    web_url: Optional[StrictStr] = Field(default=None, description="The Web URL link to the file.", alias="webUrl", json_schema_extra={"examples": ["http://localhost/files/document.docx"]})
    file_type: Optional[FileType] = Field(default=None, description="The file type.", alias="fileType")
    file_exst: Optional[StrictStr] = Field(default=None, description="The file extension.", alias="fileExst", json_schema_extra={"examples": [".txt"]})
    comment: Optional[StrictStr] = Field(default=None, description="The comment to the file.", json_schema_extra={"examples": ["This is a comment"]})
    encrypted: Optional[StrictBool] = Field(default=None, description="Specifies if the file is encrypted or not.", json_schema_extra={"examples": [False]})
    thumbnail_url: Optional[StrictStr] = Field(default=None, description="The thumbnail URL of the file.", alias="thumbnailUrl", json_schema_extra={"examples": ["http://localhost/thumbnails/file.png"]})
    thumbnail_status: Optional[Thumbnail] = Field(default=None, description="The current thumbnail status of the file.", alias="thumbnailStatus")
    locked: Optional[StrictBool] = Field(default=None, description="Specifies if the file is locked or not.", json_schema_extra={"examples": [False]})
    locked_by: Optional[StrictStr] = Field(default=None, description="The user ID of the person who locked the file.", alias="lockedBy", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    has_draft: Optional[StrictBool] = Field(default=None, description="Specifies if the file has a draft or not.", alias="hasDraft", json_schema_extra={"examples": [False]})
    form_filling_status: Optional[FormFillingStatus] = Field(default=None, description="The status of the form filling process.", alias="formFillingStatus")
    is_form: Optional[StrictBool] = Field(default=None, description="Specifies if the file is a form or not.", alias="isForm", json_schema_extra={"examples": [False]})
    custom_filter_enabled: Optional[StrictBool] = Field(default=None, description="Specifies if the Custom Filter editing mode is enabled for a file or not.", alias="customFilterEnabled", json_schema_extra={"examples": [False]})
    custom_filter_enabled_by: Optional[StrictStr] = Field(default=None, description="The name of the user who enabled a Custom Filter editing mode for a file.", alias="customFilterEnabledBy", json_schema_extra={"examples": ["John Doe"]})
    start_filling: Optional[StrictBool] = Field(default=None, description="Specifies if the filling has started or not.", alias="startFilling", json_schema_extra={"examples": [False]})
    is_filling_preparing: Optional[StrictBool] = Field(default=None, description="Specifies if the form filling has started but the file is still being saved by the document editor. Filling and editing are not allowed.", alias="isFillingPreparing", json_schema_extra={"examples": [False]})
    in_process_folder_id: Optional[StrictInt] = Field(default=None, description="The InProcess folder ID of the file.", alias="inProcessFolderId", json_schema_extra={"examples": [10]})
    in_process_folder_title: Optional[StrictStr] = Field(default=None, description="The InProcess folder title of the file.", alias="inProcessFolderTitle", json_schema_extra={"examples": ["In Process"]})
    results_folder_id: Optional[StrictInt] = Field(default=None, description="The ID of the FormFillingFolderDone folder that corresponds to this original form.", alias="resultsFolderId", json_schema_extra={"examples": [55]})
    draft_location: Optional[DraftLocationInteger] = Field(default=None, description="The file draft information with its location.", alias="draftLocation")
    view_accessibility: Optional[FileDtoIntegerAllOfViewAccessibility] = Field(default=None, alias="viewAccessibility")
    last_opened: Optional[datetime] = Field(default=None, description="The time when the file was last opened.", alias="lastOpened", json_schema_extra={"examples": ["2021-01-01T00:00:00Z"]})
    expired: Optional[datetime] = Field(default=None, description="The date when the file will be expired.", json_schema_extra={"examples": ["2025-12-31T23:59:59Z"]})
    vectorization_status: Optional[VectorizationStatus] = Field(default=None, description="The vectorization status of the file.", alias="vectorizationStatus")
    external_db_table_name: Optional[StrictStr] = Field(default=None, description="The name of the table in the external database that corresponds to this form.", alias="externalDbTableName", json_schema_extra={"examples": ["form_123_v1"]})
    dimensions: Optional[Size] = Field(default=None, description="The dimensions (width and height) of the image file in pixels.  This property is populated only for image files that can be viewed (supported formats like PNG, JPEG, GIF, BMP, etc.).  For non-image files, this property remains null.")

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
        """Create an instance of FileDtoInteger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shared_by
        if self.shared_by:
            _dict['sharedBy'] = self.shared_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owned_by
        if self.owned_by:
            _dict['ownedBy'] = self.owned_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of share_settings
        if self.share_settings:
            _dict['shareSettings'] = self.share_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict['security'] = self.security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available_share_rights
        if self.available_share_rights:
            _dict['availableShareRights'] = self.available_share_rights.to_dict()
        # override the default output from pydantic by calling `to_dict()` of draft_location
        if self.draft_location:
            _dict['draftLocation'] = self.draft_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of view_accessibility
        if self.view_accessibility:
            _dict['viewAccessibility'] = self.view_accessibility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dimensions
        if self.dimensions:
            _dict['dimensions'] = self.dimensions.to_dict()
        # set to None if share_settings (nullable) is None
        # and model_fields_set contains the field
        if self.share_settings is None and "share_settings" in self.model_fields_set:
            _dict['shareSettings'] = None

        # set to None if security (nullable) is None
        # and model_fields_set contains the field
        if self.security is None and "security" in self.model_fields_set:
            _dict['security'] = None

        # set to None if available_share_rights (nullable) is None
        # and model_fields_set contains the field
        if self.available_share_rights is None and "available_share_rights" in self.model_fields_set:
            _dict['availableShareRights'] = None

        # set to None if content_length (nullable) is None
        # and model_fields_set contains the field
        if self.content_length is None and "content_length" in self.model_fields_set:
            _dict['contentLength'] = None

        # set to None if pure_content_length (nullable) is None
        # and model_fields_set contains the field
        if self.pure_content_length is None and "pure_content_length" in self.model_fields_set:
            _dict['pureContentLength'] = None

        # set to None if view_url (nullable) is None
        # and model_fields_set contains the field
        if self.view_url is None and "view_url" in self.model_fields_set:
            _dict['viewUrl'] = None

        # set to None if web_url (nullable) is None
        # and model_fields_set contains the field
        if self.web_url is None and "web_url" in self.model_fields_set:
            _dict['webUrl'] = None

        # set to None if file_exst (nullable) is None
        # and model_fields_set contains the field
        if self.file_exst is None and "file_exst" in self.model_fields_set:
            _dict['fileExst'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if encrypted (nullable) is None
        # and model_fields_set contains the field
        if self.encrypted is None and "encrypted" in self.model_fields_set:
            _dict['encrypted'] = None

        # set to None if thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail_url is None and "thumbnail_url" in self.model_fields_set:
            _dict['thumbnailUrl'] = None

        # set to None if locked (nullable) is None
        # and model_fields_set contains the field
        if self.locked is None and "locked" in self.model_fields_set:
            _dict['locked'] = None

        # set to None if locked_by (nullable) is None
        # and model_fields_set contains the field
        if self.locked_by is None and "locked_by" in self.model_fields_set:
            _dict['lockedBy'] = None

        # set to None if has_draft (nullable) is None
        # and model_fields_set contains the field
        if self.has_draft is None and "has_draft" in self.model_fields_set:
            _dict['hasDraft'] = None

        # set to None if is_form (nullable) is None
        # and model_fields_set contains the field
        if self.is_form is None and "is_form" in self.model_fields_set:
            _dict['isForm'] = None

        # set to None if custom_filter_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.custom_filter_enabled is None and "custom_filter_enabled" in self.model_fields_set:
            _dict['customFilterEnabled'] = None

        # set to None if custom_filter_enabled_by (nullable) is None
        # and model_fields_set contains the field
        if self.custom_filter_enabled_by is None and "custom_filter_enabled_by" in self.model_fields_set:
            _dict['customFilterEnabledBy'] = None

        # set to None if start_filling (nullable) is None
        # and model_fields_set contains the field
        if self.start_filling is None and "start_filling" in self.model_fields_set:
            _dict['startFilling'] = None

        # set to None if is_filling_preparing (nullable) is None
        # and model_fields_set contains the field
        if self.is_filling_preparing is None and "is_filling_preparing" in self.model_fields_set:
            _dict['isFillingPreparing'] = None

        # set to None if in_process_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.in_process_folder_id is None and "in_process_folder_id" in self.model_fields_set:
            _dict['inProcessFolderId'] = None

        # set to None if in_process_folder_title (nullable) is None
        # and model_fields_set contains the field
        if self.in_process_folder_title is None and "in_process_folder_title" in self.model_fields_set:
            _dict['inProcessFolderTitle'] = None

        # set to None if results_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.results_folder_id is None and "results_folder_id" in self.model_fields_set:
            _dict['resultsFolderId'] = None

        # set to None if view_accessibility (nullable) is None
        # and model_fields_set contains the field
        if self.view_accessibility is None and "view_accessibility" in self.model_fields_set:
            _dict['viewAccessibility'] = None

        # set to None if last_opened (nullable) is None
        # and model_fields_set contains the field
        if self.last_opened is None and "last_opened" in self.model_fields_set:
            _dict['lastOpened'] = None

        # set to None if expired (nullable) is None
        # and model_fields_set contains the field
        if self.expired is None and "expired" in self.model_fields_set:
            _dict['expired'] = None

        # set to None if external_db_table_name (nullable) is None
        # and model_fields_set contains the field
        if self.external_db_table_name is None and "external_db_table_name" in self.model_fields_set:
            _dict['externalDbTableName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance from a dict"""
        if obj is None:
            return None
        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        base_obj = super().from_dict(obj)
        base_dict = base_obj.model_dump() if hasattr(base_obj, "model_dump") else dict(base_obj or {})

        extra_fields = {
            "folderId": obj.get("folderId"),
            "version": obj.get("version"),
            "versionGroup": obj.get("versionGroup"),
            "contentLength": obj.get("contentLength"),
            "pureContentLength": obj.get("pureContentLength"),
            "fileStatus": obj.get("fileStatus"),
            "editingBy": obj.get("editingBy"),
            "mute": obj.get("mute"),
            "viewUrl": obj.get("viewUrl"),
            "webUrl": obj.get("webUrl"),
            "fileType": obj.get("fileType"),
            "fileExst": obj.get("fileExst"),
            "comment": obj.get("comment"),
            "encrypted": obj.get("encrypted"),
            "thumbnailUrl": obj.get("thumbnailUrl"),
            "thumbnailStatus": obj.get("thumbnailStatus"),
            "locked": obj.get("locked"),
            "lockedBy": obj.get("lockedBy"),
            "hasDraft": obj.get("hasDraft"),
            "formFillingStatus": obj.get("formFillingStatus"),
            "isForm": obj.get("isForm"),
            "customFilterEnabled": obj.get("customFilterEnabled"),
            "customFilterEnabledBy": obj.get("customFilterEnabledBy"),
            "startFilling": obj.get("startFilling"),
            "isFillingPreparing": obj.get("isFillingPreparing"),
            "inProcessFolderId": obj.get("inProcessFolderId"),
            "inProcessFolderTitle": obj.get("inProcessFolderTitle"),
            "resultsFolderId": obj.get("resultsFolderId"),
            "draftLocation": DraftLocationInteger.from_dict(obj["draftLocation"]) if obj.get("draftLocation") is not None else None,
            "viewAccessibility": FileDtoIntegerAllOfViewAccessibility.from_dict(obj["viewAccessibility"]) if obj.get("viewAccessibility") is not None else None,
            "lastOpened": obj.get("lastOpened"),
            "expired": obj.get("expired"),
            "vectorizationStatus": obj.get("vectorizationStatus"),
            "externalDbTableName": obj.get("externalDbTableName"),
            "dimensions": Size.from_dict(obj["dimensions"]) if obj.get("dimensions") is not None else None
        }
        all_fields = {**base_dict, **extra_fields}
        return cls.model_validate(all_fields)


