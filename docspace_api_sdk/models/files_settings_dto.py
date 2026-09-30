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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from docspace_api_sdk.models.auto_clean_up_data import AutoCleanUpData
from docspace_api_sdk.models.files_settings_dto_internal_formats import FilesSettingsDtoInternalFormats
from docspace_api_sdk.models.order_by import OrderBy
from typing import Optional, Set
from typing_extensions import Self

class FilesSettingsDto(BaseModel):
    """
    Everything a client needs to work with documents in this portal: the format tables, the address templates, the  upload limits, the portal-wide switches and the preferences of the calling account.
    """ # noqa: E501
    exts_image_previewed: Optional[List[StrictStr]] = Field(default=None, description="Images the portal can show in its own viewer. Anything outside the list has to be downloaded to be seen.", alias="extsImagePreviewed", json_schema_extra={"examples": [[".bmp", ".gif", ".jpeg", ".jpg", ".png", ".svg"]]})
    exts_media_previewed: Optional[List[StrictStr]] = Field(default=None, description="Audio and video the portal can play in its own player.", alias="extsMediaPreviewed", json_schema_extra={"examples": [[".mp4", ".webm", ".mp3", ".ogg"]]})
    exts_web_previewed: Optional[List[StrictStr]] = Field(default=None, description="Documents the editor can open read-only. A format that is here but not in the edited list can be viewed and  not changed.", alias="extsWebPreviewed", json_schema_extra={"examples": [[".docx", ".xlsx", ".pptx", ".pdf"]]})
    exts_web_edited: Optional[List[StrictStr]] = Field(default=None, description="Documents the editor can open for editing. Uploading a format outside this list and outside the convertible  list leaves a file that can only be downloaded.", alias="extsWebEdited", json_schema_extra={"examples": [[".docx", ".xlsx", ".pptx"]]})
    exts_web_encrypt: Optional[List[StrictStr]] = Field(default=None, description="Documents that can be edited inside a private room, where the content is encrypted on the client.", alias="extsWebEncrypt", json_schema_extra={"examples": [[".docx", ".xlsx", ".pptx"]]})
    exts_web_reviewed: Optional[List[StrictStr]] = Field(default=None, description="Documents that support the reviewing mode, so that granting review access to them is meaningful.", alias="extsWebReviewed", json_schema_extra={"examples": [[".docx"]]})
    exts_web_custom_filter_editing: Optional[List[StrictStr]] = Field(default=None, description="Spreadsheets that support the custom filter mode, where a filter applied by one editor does not disturb the  others.", alias="extsWebCustomFilterEditing", json_schema_extra={"examples": [[".xlsx"]]})
    exts_web_restricted_editing: Optional[List[StrictStr]] = Field(default=None, description="Documents that can only be filled in or commented on rather than edited freely, whatever access the caller  holds.", alias="extsWebRestrictedEditing", json_schema_extra={"examples": [[".pdf"]]})
    exts_web_commented: Optional[List[StrictStr]] = Field(default=None, description="Documents that support comments, so that granting comment access to them is meaningful.", alias="extsWebCommented", json_schema_extra={"examples": [[".docx"]]})
    exts_web_template: Optional[List[StrictStr]] = Field(default=None, description="Documents the portal treats as templates to create new files from.", alias="extsWebTemplate", json_schema_extra={"examples": [[".docx", ".xlsx", ".pptx"]]})
    exts_must_convert: Optional[List[StrictStr]] = Field(default=None, description="Formats that cannot be edited as they are and are converted on upload or on first opening. Which target each  one has is in the convertible table below.", alias="extsMustConvert", json_schema_extra={"examples": [[".doc", ".xls", ".ppt"]]})
    exts_convertible: Optional[Dict[str, Optional[List[StrictStr]]]] = Field(default=None, description="The conversion map of the portal: for each source extension, the extensions it can be converted into. Use it  to fill the target format of a conversion request instead of guessing one.", alias="extsConvertible", json_schema_extra={"examples": [{".doc": [".docx", ".pdf"], ".xls": [".xlsx", ".pdf"]}]})
    exts_uploadable: Optional[List[StrictStr]] = Field(default=None, description="Formats the portal offers to create and upload as documents. It is not an upload filter: files of other  formats are stored as they are.", alias="extsUploadable", json_schema_extra={"examples": [[".docx", ".xlsx", ".pdf"]]})
    exts_archive: Optional[List[StrictStr]] = Field(default=None, description="Formats recognised as archives, which is what decides the archive icon and the offer to unpack.", alias="extsArchive", json_schema_extra={"examples": [[".zip", ".rar", ".7z"]]})
    exts_video: Optional[List[StrictStr]] = Field(default=None, description="Formats classified as video. The classification lists drive icons and the media filters of the listing  operations, and are wider than what the built-in player can show.", alias="extsVideo", json_schema_extra={"examples": [[".mp4", ".webm", ".avi"]]})
    exts_audio: Optional[List[StrictStr]] = Field(default=None, description="Formats classified as audio.", alias="extsAudio", json_schema_extra={"examples": [[".mp3", ".ogg", ".wav"]]})
    exts_image: Optional[List[StrictStr]] = Field(default=None, description="Formats classified as images.", alias="extsImage", json_schema_extra={"examples": [[".png", ".jpg", ".gif"]]})
    exts_spreadsheet: Optional[List[StrictStr]] = Field(default=None, description="Formats classified as spreadsheets.", alias="extsSpreadsheet", json_schema_extra={"examples": [[".xlsx", ".xls", ".ods"]]})
    exts_presentation: Optional[List[StrictStr]] = Field(default=None, description="Formats classified as presentations.", alias="extsPresentation", json_schema_extra={"examples": [[".pptx", ".ppt", ".odp"]]})
    exts_document: Optional[List[StrictStr]] = Field(default=None, description="Formats classified as text documents.", alias="extsDocument", json_schema_extra={"examples": [[".docx", ".doc", ".odt"]]})
    exts_diagram: Optional[List[StrictStr]] = Field(default=None, description="Formats classified as diagrams.", alias="extsDiagram", json_schema_extra={"examples": [[".vsdx"]]})
    internal_formats: Optional[FilesSettingsDtoInternalFormats] = Field(default=None, alias="internalFormats")
    master_form_extension: Optional[StrictStr] = Field(default=None, description="The extension of a fillable form template in this portal. It is configurable, so read it rather than assuming  the product default.", alias="masterFormExtension", json_schema_extra={"examples": [".pdf"]})
    param_version: Optional[StrictStr] = Field(default=None, description="The name of the query parameter that pins a document address to one version. Append it to the addresses below  instead of composing a version address by hand.", alias="paramVersion", json_schema_extra={"examples": ["version"]})
    param_out_type: Optional[StrictStr] = Field(default=None, description="The name of the query parameter that asks a download address for a converted copy in another format.", alias="paramOutType", json_schema_extra={"examples": ["outputtype"]})
    file_download_url_string: Optional[StrictStr] = Field(default=None, description="The template of the address a file is downloaded from: substitute the file identifier for the `{0}`  placeholder. Add the version and output-type parameters named above for a particular version or format.", alias="fileDownloadUrlString", json_schema_extra={"examples": ["https://example.com/filehandler.ashx?action=download&fileid={0}"]})
    file_web_viewer_url_string: Optional[StrictStr] = Field(default=None, description="The template of the address that opens a file in the viewer inside the portal, with `{0}` for the file  identifier. It is a portal-relative address, meant to be opened in a browser rather than called as an API.", alias="fileWebViewerUrlString", json_schema_extra={"examples": ["/products/files/doceditor?fileid={0}&action=view"]})
    file_web_viewer_external_url_string: Optional[StrictStr] = Field(default=None, description="The same viewer address as an absolute one, for a message or a page outside the portal.", alias="fileWebViewerExternalUrlString", json_schema_extra={"examples": ["https://example.com/products/files/doceditor?fileid={0}&action=view"]})
    file_web_editor_url_string: Optional[StrictStr] = Field(default=None, description="The template of the address that opens a file for editing inside the portal, with `{0}` for the file  identifier. Whether the session really becomes editable still depends on the access the caller holds.", alias="fileWebEditorUrlString", json_schema_extra={"examples": ["/products/files/doceditor?fileid={0}&action=edit"]})
    file_web_editor_external_url_string: Optional[StrictStr] = Field(default=None, description="The same editing address as an absolute one, for use outside the portal.", alias="fileWebEditorExternalUrlString", json_schema_extra={"examples": ["https://example.com/products/files/doceditor?fileid={0}&action=edit"]})
    file_redirect_preview_url_string: Optional[StrictStr] = Field(default=None, description="The template of the address that sends the browser on to whichever viewer or editor suits the file, with `{0}`  for the file identifier. Use it when the kind of the file is not known in advance.", alias="fileRedirectPreviewUrlString", json_schema_extra={"examples": ["https://example.com/products/files/{0}"]})
    file_thumbnail_url_string: Optional[StrictStr] = Field(default=None, description="The template of the address a file thumbnail is fetched from, with `{0}` for the file identifier. A thumbnail  is built in the background, so the address can answer with nothing for a while after the file appears.", alias="fileThumbnailUrlString", json_schema_extra={"examples": ["https://example.com/filehandler.ashx?action=thumb&fileid={0}"]})
    confirm_delete: Optional[StrictBool] = Field(default=None, description="Whether the caller asked to be prompted before a deletion. Written by `PUT api/2.0/files/changedeleteconfrim`.", alias="confirmDelete", json_schema_extra={"examples": [True]})
    enable_third_party: Optional[StrictBool] = Field(default=None, description="Whether this portal allows third-party storages to be connected at all. It is set portal-wide by an  administrator, so a member sees it as read-only.", alias="enableThirdParty", json_schema_extra={"examples": [True]})
    external_share: Optional[StrictBool] = Field(default=None, description="Whether links that open an entry without a portal account may be created in this portal. Set portal-wide by an  administrator.", alias="externalShare", json_schema_extra={"examples": [True]})
    external_share_social_media: Optional[StrictBool] = Field(default=None, description="Whether the share-to-network buttons are offered next to an external link. It is reported as false whenever  external sharing itself is off.", alias="externalShareSocialMedia", json_schema_extra={"examples": [True]})
    store_original_files: Optional[StrictBool] = Field(default=None, description="Whether the caller's uploads keep the original file when the portal converts them. With false the conversion  replaces the uploaded file with a new version of it.", alias="storeOriginalFiles", json_schema_extra={"examples": [True]})
    keep_new_file_name: Optional[StrictBool] = Field(default=None, description="Whether the caller asked for new documents to be created with the default name instead of being prompted for  one.", alias="keepNewFileName", json_schema_extra={"examples": [False]})
    display_file_extension: Optional[StrictBool] = Field(default=None, description="Whether the caller asked to see extensions in file titles. Stored titles always carry the extension whatever  this says.", alias="displayFileExtension", json_schema_extra={"examples": [True]})
    show_quick_actions: Optional[StrictBool] = Field(default=None, description="Specifies whether to display the quick action buttons.", alias="showQuickActions", json_schema_extra={"examples": [True]})
    convert_notify: Optional[StrictBool] = Field(default=None, description="Whether the caller is told about the result of a conversion. There is no operation in this document that  writes it.", alias="convertNotify", json_schema_extra={"examples": [True]})
    hide_confirm_cancel_operation: Optional[StrictBool] = Field(default=None, description="Whether the prompt shown before a running operation is abandoned is hidden for the caller.", alias="hideConfirmCancelOperation", json_schema_extra={"examples": [False]})
    hide_confirm_convert_save: Optional[StrictBool] = Field(default=None, description="Whether the prompt that offers to keep a copy in the original format on conversion is hidden for the caller.  Once true it cannot be turned back through the API.", alias="hideConfirmConvertSave", json_schema_extra={"examples": [False]})
    hide_confirm_convert_open: Optional[StrictBool] = Field(default=None, description="Whether the prompt that offers to open the conversion result is hidden for the caller. Once true it cannot be  turned back through the API.", alias="hideConfirmConvertOpen", json_schema_extra={"examples": [False]})
    hide_confirm_room_lifetime: Optional[StrictBool] = Field(default=None, description="Whether the warning shown before the lifetime settings of a room are changed is hidden for the caller.", alias="hideConfirmRoomLifetime", json_schema_extra={"examples": [False]})
    default_order: Optional[OrderBy] = Field(default=None, description="The ordering the listing operations fall back to when a request names none. It follows the last order the  caller asked a listing for, so it changes on its own as the account is used.", alias="defaultOrder")
    forcesave: Optional[StrictBool] = Field(default=None, description="Whether the editor writes a document back to storage while the session is still open. It is on for every  portal and cannot be switched off.", json_schema_extra={"examples": [True]})
    store_forcesave: Optional[StrictBool] = Field(default=None, description="Whether those intermediate saves are kept as separate versions. They are not, in any portal: they update the  current version instead.", alias="storeForcesave", json_schema_extra={"examples": [False]})
    recent_section: Optional[StrictBool] = Field(default=None, description="Whether the Recent section is offered to the caller among the section roots.", alias="recentSection", json_schema_extra={"examples": [True]})
    favorites_section: Optional[StrictBool] = Field(default=None, description="Whether the Favorites section is offered to the caller among the section roots.", alias="favoritesSection", json_schema_extra={"examples": [True]})
    templates_section: Optional[StrictBool] = Field(default=None, description="Whether the Templates section is offered to the caller among the section roots.", alias="templatesSection", json_schema_extra={"examples": [True]})
    download_tar_gz: Optional[StrictBool] = Field(default=None, description="The archive format the caller's multi-item downloads are packed into: true for `.tar.gz`, false for `.zip`.", alias="downloadTarGz", json_schema_extra={"examples": [True]})
    automatically_clean_up: Optional[AutoCleanUpData] = Field(default=None, description="The trash auto-clearing setting of the caller, the same pair `GET api/2.0/files/settings/autocleanup` returns.", alias="automaticallyCleanUp")
    can_search_by_content: Optional[StrictBool] = Field(default=None, description="Whether documents in this portal can be searched by what is inside them and not only by title. It depends on  the full-text search service being configured and having indexed the portal.", alias="canSearchByContent", json_schema_extra={"examples": [True]})
    default_sharing_access_rights: Optional[List[StrictInt]] = Field(default=None, description="The access rights the sharing dialog offers the caller by default. The portal normalises the set it stores, so  this can be shorter than what was last sent.", alias="defaultSharingAccessRights", json_schema_extra={"examples": [[1, 2]]})
    max_upload_thread_count: Optional[StrictInt] = Field(default=None, description="How many upload requests the portal accepts from one account at a time. Sending more than this in parallel  gets the extra ones refused rather than queued.", alias="maxUploadThreadCount", json_schema_extra={"examples": [10]})
    chunk_upload_size: Optional[StrictInt] = Field(default=None, description="The size in bytes of one chunk of a chunked upload. Split a large file exactly along this size: a chunk that  does not match is refused by the upload session.", alias="chunkUploadSize", json_schema_extra={"examples": [10485760]})
    open_editor_in_same_tab: Optional[StrictBool] = Field(default=None, description="Whether the caller asked for documents to open in the current browser tab.", alias="openEditorInSameTab", json_schema_extra={"examples": [False]})
    organize_rooms_grouping: Optional[StrictBool] = Field(default=None, description="Whether the caller asked to see rooms arranged by the groups they belong to.", alias="organizeRoomsGrouping", json_schema_extra={"examples": [True]})
    default_share_link_internal: Optional[StrictBool] = Field(default=None, description="The kind of external link this portal offers first: true for a link only its own accounts can open, false for  one anyone holding it can open.", alias="defaultShareLinkInternal", json_schema_extra={"examples": [False]})
    external_share_apply_to_documents: Optional[StrictBool] = Field(default=None, description="Whether the external sharing restriction covers personal documents. It matters only while external sharing is  off.", alias="externalShareApplyToDocuments", json_schema_extra={"examples": [True]})
    external_share_apply_to_rooms: Optional[StrictBool] = Field(default=None, description="Whether the external sharing restriction covers rooms, including making a new one public. It matters only  while external sharing is off.", alias="externalShareApplyToRooms", json_schema_extra={"examples": [True]})
    block_existing_links_on_restrict: Optional[StrictBool] = Field(default=None, description="Whether links created before the restriction stop opening as well, rather than only new ones being refused.", alias="blockExistingLinksOnRestrict", json_schema_extra={"examples": [True]})
    exts_files_vectorized: Optional[List[StrictStr]] = Field(default=None, description="Formats whose content can be indexed for the AI features of the portal. A file outside the list is left out of  that index.", alias="extsFilesVectorized", json_schema_extra={"examples": [[".docx", ".pdf", ".txt"]]})
    max_vectorization_file_size: Optional[StrictInt] = Field(default=None, description="The largest file size in bytes that is indexed for the AI features. A larger file is skipped even when its  format is listed above.", alias="maxVectorizationFileSize", json_schema_extra={"examples": [5242880]})
    __properties: ClassVar[List[str]] = ["extsImagePreviewed", "extsMediaPreviewed", "extsWebPreviewed", "extsWebEdited", "extsWebEncrypt", "extsWebReviewed", "extsWebCustomFilterEditing", "extsWebRestrictedEditing", "extsWebCommented", "extsWebTemplate", "extsMustConvert", "extsConvertible", "extsUploadable", "extsArchive", "extsVideo", "extsAudio", "extsImage", "extsSpreadsheet", "extsPresentation", "extsDocument", "extsDiagram", "internalFormats", "masterFormExtension", "paramVersion", "paramOutType", "fileDownloadUrlString", "fileWebViewerUrlString", "fileWebViewerExternalUrlString", "fileWebEditorUrlString", "fileWebEditorExternalUrlString", "fileRedirectPreviewUrlString", "fileThumbnailUrlString", "confirmDelete", "enableThirdParty", "externalShare", "externalShareSocialMedia", "storeOriginalFiles", "keepNewFileName", "displayFileExtension", "showQuickActions", "convertNotify", "hideConfirmCancelOperation", "hideConfirmConvertSave", "hideConfirmConvertOpen", "hideConfirmRoomLifetime", "defaultOrder", "forcesave", "storeForcesave", "recentSection", "favoritesSection", "templatesSection", "downloadTarGz", "automaticallyCleanUp", "canSearchByContent", "defaultSharingAccessRights", "maxUploadThreadCount", "chunkUploadSize", "openEditorInSameTab", "organizeRoomsGrouping", "defaultShareLinkInternal", "externalShareApplyToDocuments", "externalShareApplyToRooms", "blockExistingLinksOnRestrict", "extsFilesVectorized", "maxVectorizationFileSize"]

    @field_validator('default_sharing_access_rights')
    def default_sharing_access_rights_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]):
                raise ValueError("each list item must be one of (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)")
        return value

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
        """Create an instance of FilesSettingsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of internal_formats
        if self.internal_formats:
            _dict['internalFormats'] = self.internal_formats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_order
        if self.default_order:
            _dict['defaultOrder'] = self.default_order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of automatically_clean_up
        if self.automatically_clean_up:
            _dict['automaticallyCleanUp'] = self.automatically_clean_up.to_dict()
        # set to None if exts_image_previewed (nullable) is None
        # and model_fields_set contains the field
        if self.exts_image_previewed is None and "exts_image_previewed" in self.model_fields_set:
            _dict['extsImagePreviewed'] = None

        # set to None if exts_media_previewed (nullable) is None
        # and model_fields_set contains the field
        if self.exts_media_previewed is None and "exts_media_previewed" in self.model_fields_set:
            _dict['extsMediaPreviewed'] = None

        # set to None if exts_web_previewed (nullable) is None
        # and model_fields_set contains the field
        if self.exts_web_previewed is None and "exts_web_previewed" in self.model_fields_set:
            _dict['extsWebPreviewed'] = None

        # set to None if exts_web_edited (nullable) is None
        # and model_fields_set contains the field
        if self.exts_web_edited is None and "exts_web_edited" in self.model_fields_set:
            _dict['extsWebEdited'] = None

        # set to None if exts_web_encrypt (nullable) is None
        # and model_fields_set contains the field
        if self.exts_web_encrypt is None and "exts_web_encrypt" in self.model_fields_set:
            _dict['extsWebEncrypt'] = None

        # set to None if exts_web_reviewed (nullable) is None
        # and model_fields_set contains the field
        if self.exts_web_reviewed is None and "exts_web_reviewed" in self.model_fields_set:
            _dict['extsWebReviewed'] = None

        # set to None if exts_web_custom_filter_editing (nullable) is None
        # and model_fields_set contains the field
        if self.exts_web_custom_filter_editing is None and "exts_web_custom_filter_editing" in self.model_fields_set:
            _dict['extsWebCustomFilterEditing'] = None

        # set to None if exts_web_restricted_editing (nullable) is None
        # and model_fields_set contains the field
        if self.exts_web_restricted_editing is None and "exts_web_restricted_editing" in self.model_fields_set:
            _dict['extsWebRestrictedEditing'] = None

        # set to None if exts_web_commented (nullable) is None
        # and model_fields_set contains the field
        if self.exts_web_commented is None and "exts_web_commented" in self.model_fields_set:
            _dict['extsWebCommented'] = None

        # set to None if exts_web_template (nullable) is None
        # and model_fields_set contains the field
        if self.exts_web_template is None and "exts_web_template" in self.model_fields_set:
            _dict['extsWebTemplate'] = None

        # set to None if exts_must_convert (nullable) is None
        # and model_fields_set contains the field
        if self.exts_must_convert is None and "exts_must_convert" in self.model_fields_set:
            _dict['extsMustConvert'] = None

        # set to None if exts_uploadable (nullable) is None
        # and model_fields_set contains the field
        if self.exts_uploadable is None and "exts_uploadable" in self.model_fields_set:
            _dict['extsUploadable'] = None

        # set to None if exts_archive (nullable) is None
        # and model_fields_set contains the field
        if self.exts_archive is None and "exts_archive" in self.model_fields_set:
            _dict['extsArchive'] = None

        # set to None if exts_video (nullable) is None
        # and model_fields_set contains the field
        if self.exts_video is None and "exts_video" in self.model_fields_set:
            _dict['extsVideo'] = None

        # set to None if exts_audio (nullable) is None
        # and model_fields_set contains the field
        if self.exts_audio is None and "exts_audio" in self.model_fields_set:
            _dict['extsAudio'] = None

        # set to None if exts_image (nullable) is None
        # and model_fields_set contains the field
        if self.exts_image is None and "exts_image" in self.model_fields_set:
            _dict['extsImage'] = None

        # set to None if exts_spreadsheet (nullable) is None
        # and model_fields_set contains the field
        if self.exts_spreadsheet is None and "exts_spreadsheet" in self.model_fields_set:
            _dict['extsSpreadsheet'] = None

        # set to None if exts_presentation (nullable) is None
        # and model_fields_set contains the field
        if self.exts_presentation is None and "exts_presentation" in self.model_fields_set:
            _dict['extsPresentation'] = None

        # set to None if exts_document (nullable) is None
        # and model_fields_set contains the field
        if self.exts_document is None and "exts_document" in self.model_fields_set:
            _dict['extsDocument'] = None

        # set to None if exts_diagram (nullable) is None
        # and model_fields_set contains the field
        if self.exts_diagram is None and "exts_diagram" in self.model_fields_set:
            _dict['extsDiagram'] = None

        # set to None if internal_formats (nullable) is None
        # and model_fields_set contains the field
        if self.internal_formats is None and "internal_formats" in self.model_fields_set:
            _dict['internalFormats'] = None

        # set to None if master_form_extension (nullable) is None
        # and model_fields_set contains the field
        if self.master_form_extension is None and "master_form_extension" in self.model_fields_set:
            _dict['masterFormExtension'] = None

        # set to None if param_version (nullable) is None
        # and model_fields_set contains the field
        if self.param_version is None and "param_version" in self.model_fields_set:
            _dict['paramVersion'] = None

        # set to None if param_out_type (nullable) is None
        # and model_fields_set contains the field
        if self.param_out_type is None and "param_out_type" in self.model_fields_set:
            _dict['paramOutType'] = None

        # set to None if file_download_url_string (nullable) is None
        # and model_fields_set contains the field
        if self.file_download_url_string is None and "file_download_url_string" in self.model_fields_set:
            _dict['fileDownloadUrlString'] = None

        # set to None if file_web_viewer_url_string (nullable) is None
        # and model_fields_set contains the field
        if self.file_web_viewer_url_string is None and "file_web_viewer_url_string" in self.model_fields_set:
            _dict['fileWebViewerUrlString'] = None

        # set to None if file_web_viewer_external_url_string (nullable) is None
        # and model_fields_set contains the field
        if self.file_web_viewer_external_url_string is None and "file_web_viewer_external_url_string" in self.model_fields_set:
            _dict['fileWebViewerExternalUrlString'] = None

        # set to None if file_web_editor_url_string (nullable) is None
        # and model_fields_set contains the field
        if self.file_web_editor_url_string is None and "file_web_editor_url_string" in self.model_fields_set:
            _dict['fileWebEditorUrlString'] = None

        # set to None if file_web_editor_external_url_string (nullable) is None
        # and model_fields_set contains the field
        if self.file_web_editor_external_url_string is None and "file_web_editor_external_url_string" in self.model_fields_set:
            _dict['fileWebEditorExternalUrlString'] = None

        # set to None if file_redirect_preview_url_string (nullable) is None
        # and model_fields_set contains the field
        if self.file_redirect_preview_url_string is None and "file_redirect_preview_url_string" in self.model_fields_set:
            _dict['fileRedirectPreviewUrlString'] = None

        # set to None if file_thumbnail_url_string (nullable) is None
        # and model_fields_set contains the field
        if self.file_thumbnail_url_string is None and "file_thumbnail_url_string" in self.model_fields_set:
            _dict['fileThumbnailUrlString'] = None

        # set to None if default_sharing_access_rights (nullable) is None
        # and model_fields_set contains the field
        if self.default_sharing_access_rights is None and "default_sharing_access_rights" in self.model_fields_set:
            _dict['defaultSharingAccessRights'] = None

        # set to None if exts_files_vectorized (nullable) is None
        # and model_fields_set contains the field
        if self.exts_files_vectorized is None and "exts_files_vectorized" in self.model_fields_set:
            _dict['extsFilesVectorized'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FilesSettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extsImagePreviewed": obj.get("extsImagePreviewed"),
            "extsMediaPreviewed": obj.get("extsMediaPreviewed"),
            "extsWebPreviewed": obj.get("extsWebPreviewed"),
            "extsWebEdited": obj.get("extsWebEdited"),
            "extsWebEncrypt": obj.get("extsWebEncrypt"),
            "extsWebReviewed": obj.get("extsWebReviewed"),
            "extsWebCustomFilterEditing": obj.get("extsWebCustomFilterEditing"),
            "extsWebRestrictedEditing": obj.get("extsWebRestrictedEditing"),
            "extsWebCommented": obj.get("extsWebCommented"),
            "extsWebTemplate": obj.get("extsWebTemplate"),
            "extsMustConvert": obj.get("extsMustConvert"),
            "extsConvertible": obj.get("extsConvertible"),
            "extsUploadable": obj.get("extsUploadable"),
            "extsArchive": obj.get("extsArchive"),
            "extsVideo": obj.get("extsVideo"),
            "extsAudio": obj.get("extsAudio"),
            "extsImage": obj.get("extsImage"),
            "extsSpreadsheet": obj.get("extsSpreadsheet"),
            "extsPresentation": obj.get("extsPresentation"),
            "extsDocument": obj.get("extsDocument"),
            "extsDiagram": obj.get("extsDiagram"),
            "internalFormats": FilesSettingsDtoInternalFormats.from_dict(obj["internalFormats"]) if obj.get("internalFormats") is not None else None,
            "masterFormExtension": obj.get("masterFormExtension"),
            "paramVersion": obj.get("paramVersion"),
            "paramOutType": obj.get("paramOutType"),
            "fileDownloadUrlString": obj.get("fileDownloadUrlString"),
            "fileWebViewerUrlString": obj.get("fileWebViewerUrlString"),
            "fileWebViewerExternalUrlString": obj.get("fileWebViewerExternalUrlString"),
            "fileWebEditorUrlString": obj.get("fileWebEditorUrlString"),
            "fileWebEditorExternalUrlString": obj.get("fileWebEditorExternalUrlString"),
            "fileRedirectPreviewUrlString": obj.get("fileRedirectPreviewUrlString"),
            "fileThumbnailUrlString": obj.get("fileThumbnailUrlString"),
            "confirmDelete": obj.get("confirmDelete"),
            "enableThirdParty": obj.get("enableThirdParty"),
            "externalShare": obj.get("externalShare"),
            "externalShareSocialMedia": obj.get("externalShareSocialMedia"),
            "storeOriginalFiles": obj.get("storeOriginalFiles"),
            "keepNewFileName": obj.get("keepNewFileName"),
            "displayFileExtension": obj.get("displayFileExtension"),
            "showQuickActions": obj.get("showQuickActions"),
            "convertNotify": obj.get("convertNotify"),
            "hideConfirmCancelOperation": obj.get("hideConfirmCancelOperation"),
            "hideConfirmConvertSave": obj.get("hideConfirmConvertSave"),
            "hideConfirmConvertOpen": obj.get("hideConfirmConvertOpen"),
            "hideConfirmRoomLifetime": obj.get("hideConfirmRoomLifetime"),
            "defaultOrder": OrderBy.from_dict(obj["defaultOrder"]) if obj.get("defaultOrder") is not None else None,
            "forcesave": obj.get("forcesave"),
            "storeForcesave": obj.get("storeForcesave"),
            "recentSection": obj.get("recentSection"),
            "favoritesSection": obj.get("favoritesSection"),
            "templatesSection": obj.get("templatesSection"),
            "downloadTarGz": obj.get("downloadTarGz"),
            "automaticallyCleanUp": AutoCleanUpData.from_dict(obj["automaticallyCleanUp"]) if obj.get("automaticallyCleanUp") is not None else None,
            "canSearchByContent": obj.get("canSearchByContent"),
            "defaultSharingAccessRights": obj.get("defaultSharingAccessRights"),
            "maxUploadThreadCount": obj.get("maxUploadThreadCount"),
            "chunkUploadSize": obj.get("chunkUploadSize"),
            "openEditorInSameTab": obj.get("openEditorInSameTab"),
            "organizeRoomsGrouping": obj.get("organizeRoomsGrouping"),
            "defaultShareLinkInternal": obj.get("defaultShareLinkInternal"),
            "externalShareApplyToDocuments": obj.get("externalShareApplyToDocuments"),
            "externalShareApplyToRooms": obj.get("externalShareApplyToRooms"),
            "blockExistingLinksOnRestrict": obj.get("blockExistingLinksOnRestrict"),
            "extsFilesVectorized": obj.get("extsFilesVectorized"),
            "maxVectorizationFileSize": obj.get("maxVectorizationFileSize")
        })
        return _obj


