from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...auto_clean_up_data import AutoCleanUpData
    from ...order_by import OrderBy
    from .files_settings_dto_exts_convertible import FilesSettingsDto_extsConvertible
    from .files_settings_dto_internal_formats import FilesSettingsDto_internalFormats

@dataclass
class FilesSettingsDto(Parsable):
    # The automaticallyCleanUp property
    automatically_clean_up: Optional[AutoCleanUpData] = None
    # Can search by content
    can_search_by_content: Optional[bool] = None
    # Chunk upload size
    chunk_upload_size: Optional[int] = None
    # Confirm delete
    confirm_delete: Optional[bool] = None
    # Convert notify
    convert_notify: Optional[bool] = None
    # The defaultOrder property
    default_order: Optional[OrderBy] = None
    # Default sharing access rights
    default_sharing_access_rights: Optional[List[str]] = None
    # Display file extension
    display_file_extension: Optional[bool] = None
    # Download tar gz
    download_tar_gz: Optional[bool] = None
    # EnableT third party
    enable_third_party: Optional[bool] = None
    # External share
    external_share: Optional[bool] = None
    # External share social media
    external_share_social_media: Optional[bool] = None
    # Exts archive
    exts_archive: Optional[List[str]] = None
    # Exts audio
    exts_audio: Optional[List[str]] = None
    # Exts co authoring
    exts_co_authoring: Optional[List[str]] = None
    # Exts convertible
    exts_convertible: Optional[FilesSettingsDto_extsConvertible] = None
    # Exts document
    exts_document: Optional[List[str]] = None
    # Exts image
    exts_image: Optional[List[str]] = None
    # Exts image previewed
    exts_image_previewed: Optional[List[str]] = None
    # Exts media previewed
    exts_media_previewed: Optional[List[str]] = None
    # Exts must convert
    exts_must_convert: Optional[List[str]] = None
    # Exts presentation
    exts_presentation: Optional[List[str]] = None
    # Exts spreadsheet
    exts_spreadsheet: Optional[List[str]] = None
    # Exts uploadable
    exts_uploadable: Optional[List[str]] = None
    # Exts video
    exts_video: Optional[List[str]] = None
    # Exts web commented
    exts_web_commented: Optional[List[str]] = None
    # Exts web custom filter editing
    exts_web_custom_filter_editing: Optional[List[str]] = None
    # Exts web edited
    exts_web_edited: Optional[List[str]] = None
    # Exts web encrypt
    exts_web_encrypt: Optional[List[str]] = None
    # Exts web previewed
    exts_web_previewed: Optional[List[str]] = None
    # Exts web restricted editing
    exts_web_restricted_editing: Optional[List[str]] = None
    # Exts web reviewed
    exts_web_reviewed: Optional[List[str]] = None
    # Exts web template
    exts_web_template: Optional[List[str]] = None
    # Favorites section
    favorites_section: Optional[bool] = None
    # File download url string
    file_download_url_string: Optional[str] = None
    # File redirect preview url string
    file_redirect_preview_url_string: Optional[str] = None
    # File thumbnail url string
    file_thumbnail_url_string: Optional[str] = None
    # File web editor external url string
    file_web_editor_external_url_string: Optional[str] = None
    # File web editor url string
    file_web_editor_url_string: Optional[str] = None
    # File web viewer external url string
    file_web_viewer_external_url_string: Optional[str] = None
    # File web viewer url string
    file_web_viewer_url_string: Optional[str] = None
    # Forcesave
    forcesave: Optional[bool] = None
    # Hide confirm convert open
    hide_confirm_convert_open: Optional[bool] = None
    # HideC confirm convert save
    hide_confirm_convert_save: Optional[bool] = None
    # Internal formats
    internal_formats: Optional[FilesSettingsDto_internalFormats] = None
    # Keep new file name
    keep_new_file_name: Optional[bool] = None
    # Master form extension
    master_form_extension: Optional[str] = None
    # Max upload thread count
    max_upload_thread_count: Optional[int] = None
    # Open editor in same tab
    open_editor_in_same_tab: Optional[bool] = None
    # Param out type
    param_out_type: Optional[str] = None
    # Param version
    param_version: Optional[str] = None
    # Recent section
    recent_section: Optional[bool] = None
    # Store forcesave
    store_forcesave: Optional[bool] = None
    # Store original files
    store_original_files: Optional[bool] = None
    # Templates section
    templates_section: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilesSettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilesSettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilesSettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...auto_clean_up_data import AutoCleanUpData
        from ...order_by import OrderBy
        from .files_settings_dto_exts_convertible import FilesSettingsDto_extsConvertible
        from .files_settings_dto_internal_formats import FilesSettingsDto_internalFormats

        from ...auto_clean_up_data import AutoCleanUpData
        from ...order_by import OrderBy
        from .files_settings_dto_exts_convertible import FilesSettingsDto_extsConvertible
        from .files_settings_dto_internal_formats import FilesSettingsDto_internalFormats

        fields: Dict[str, Callable[[Any], None]] = {
            "automaticallyCleanUp": lambda n : setattr(self, 'automatically_clean_up', n.get_object_value(AutoCleanUpData)),
            "canSearchByContent": lambda n : setattr(self, 'can_search_by_content', n.get_bool_value()),
            "chunkUploadSize": lambda n : setattr(self, 'chunk_upload_size', n.get_int_value()),
            "confirmDelete": lambda n : setattr(self, 'confirm_delete', n.get_bool_value()),
            "convertNotify": lambda n : setattr(self, 'convert_notify', n.get_bool_value()),
            "defaultOrder": lambda n : setattr(self, 'default_order', n.get_object_value(OrderBy)),
            "defaultSharingAccessRights": lambda n : setattr(self, 'default_sharing_access_rights', n.get_collection_of_primitive_values(str)),
            "displayFileExtension": lambda n : setattr(self, 'display_file_extension', n.get_bool_value()),
            "downloadTarGz": lambda n : setattr(self, 'download_tar_gz', n.get_bool_value()),
            "enableThirdParty": lambda n : setattr(self, 'enable_third_party', n.get_bool_value()),
            "externalShare": lambda n : setattr(self, 'external_share', n.get_bool_value()),
            "externalShareSocialMedia": lambda n : setattr(self, 'external_share_social_media', n.get_bool_value()),
            "extsArchive": lambda n : setattr(self, 'exts_archive', n.get_collection_of_primitive_values(str)),
            "extsAudio": lambda n : setattr(self, 'exts_audio', n.get_collection_of_primitive_values(str)),
            "extsCoAuthoring": lambda n : setattr(self, 'exts_co_authoring', n.get_collection_of_primitive_values(str)),
            "extsConvertible": lambda n : setattr(self, 'exts_convertible', n.get_object_value(FilesSettingsDto_extsConvertible)),
            "extsDocument": lambda n : setattr(self, 'exts_document', n.get_collection_of_primitive_values(str)),
            "extsImage": lambda n : setattr(self, 'exts_image', n.get_collection_of_primitive_values(str)),
            "extsImagePreviewed": lambda n : setattr(self, 'exts_image_previewed', n.get_collection_of_primitive_values(str)),
            "extsMediaPreviewed": lambda n : setattr(self, 'exts_media_previewed', n.get_collection_of_primitive_values(str)),
            "extsMustConvert": lambda n : setattr(self, 'exts_must_convert', n.get_collection_of_primitive_values(str)),
            "extsPresentation": lambda n : setattr(self, 'exts_presentation', n.get_collection_of_primitive_values(str)),
            "extsSpreadsheet": lambda n : setattr(self, 'exts_spreadsheet', n.get_collection_of_primitive_values(str)),
            "extsUploadable": lambda n : setattr(self, 'exts_uploadable', n.get_collection_of_primitive_values(str)),
            "extsVideo": lambda n : setattr(self, 'exts_video', n.get_collection_of_primitive_values(str)),
            "extsWebCommented": lambda n : setattr(self, 'exts_web_commented', n.get_collection_of_primitive_values(str)),
            "extsWebCustomFilterEditing": lambda n : setattr(self, 'exts_web_custom_filter_editing', n.get_collection_of_primitive_values(str)),
            "extsWebEdited": lambda n : setattr(self, 'exts_web_edited', n.get_collection_of_primitive_values(str)),
            "extsWebEncrypt": lambda n : setattr(self, 'exts_web_encrypt', n.get_collection_of_primitive_values(str)),
            "extsWebPreviewed": lambda n : setattr(self, 'exts_web_previewed', n.get_collection_of_primitive_values(str)),
            "extsWebRestrictedEditing": lambda n : setattr(self, 'exts_web_restricted_editing', n.get_collection_of_primitive_values(str)),
            "extsWebReviewed": lambda n : setattr(self, 'exts_web_reviewed', n.get_collection_of_primitive_values(str)),
            "extsWebTemplate": lambda n : setattr(self, 'exts_web_template', n.get_collection_of_primitive_values(str)),
            "favoritesSection": lambda n : setattr(self, 'favorites_section', n.get_bool_value()),
            "fileDownloadUrlString": lambda n : setattr(self, 'file_download_url_string', n.get_str_value()),
            "fileRedirectPreviewUrlString": lambda n : setattr(self, 'file_redirect_preview_url_string', n.get_str_value()),
            "fileThumbnailUrlString": lambda n : setattr(self, 'file_thumbnail_url_string', n.get_str_value()),
            "fileWebEditorExternalUrlString": lambda n : setattr(self, 'file_web_editor_external_url_string', n.get_str_value()),
            "fileWebEditorUrlString": lambda n : setattr(self, 'file_web_editor_url_string', n.get_str_value()),
            "fileWebViewerExternalUrlString": lambda n : setattr(self, 'file_web_viewer_external_url_string', n.get_str_value()),
            "fileWebViewerUrlString": lambda n : setattr(self, 'file_web_viewer_url_string', n.get_str_value()),
            "forcesave": lambda n : setattr(self, 'forcesave', n.get_bool_value()),
            "hideConfirmConvertOpen": lambda n : setattr(self, 'hide_confirm_convert_open', n.get_bool_value()),
            "hideConfirmConvertSave": lambda n : setattr(self, 'hide_confirm_convert_save', n.get_bool_value()),
            "internalFormats": lambda n : setattr(self, 'internal_formats', n.get_object_value(FilesSettingsDto_internalFormats)),
            "keepNewFileName": lambda n : setattr(self, 'keep_new_file_name', n.get_bool_value()),
            "masterFormExtension": lambda n : setattr(self, 'master_form_extension', n.get_str_value()),
            "maxUploadThreadCount": lambda n : setattr(self, 'max_upload_thread_count', n.get_int_value()),
            "openEditorInSameTab": lambda n : setattr(self, 'open_editor_in_same_tab', n.get_bool_value()),
            "paramOutType": lambda n : setattr(self, 'param_out_type', n.get_str_value()),
            "paramVersion": lambda n : setattr(self, 'param_version', n.get_str_value()),
            "recentSection": lambda n : setattr(self, 'recent_section', n.get_bool_value()),
            "storeForcesave": lambda n : setattr(self, 'store_forcesave', n.get_bool_value()),
            "storeOriginalFiles": lambda n : setattr(self, 'store_original_files', n.get_bool_value()),
            "templatesSection": lambda n : setattr(self, 'templates_section', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from ...auto_clean_up_data import AutoCleanUpData
        from ...order_by import OrderBy
        from .files_settings_dto_exts_convertible import FilesSettingsDto_extsConvertible
        from .files_settings_dto_internal_formats import FilesSettingsDto_internalFormats

        writer.write_object_value("automaticallyCleanUp", self.automatically_clean_up)
        writer.write_bool_value("canSearchByContent", self.can_search_by_content)
        writer.write_int_value("chunkUploadSize", self.chunk_upload_size)
        writer.write_bool_value("confirmDelete", self.confirm_delete)
        writer.write_bool_value("convertNotify", self.convert_notify)
        writer.write_object_value("defaultOrder", self.default_order)
        writer.write_collection_of_primitive_values("defaultSharingAccessRights", self.default_sharing_access_rights)
        writer.write_bool_value("displayFileExtension", self.display_file_extension)
        writer.write_bool_value("downloadTarGz", self.download_tar_gz)
        writer.write_bool_value("enableThirdParty", self.enable_third_party)
        writer.write_bool_value("externalShare", self.external_share)
        writer.write_bool_value("externalShareSocialMedia", self.external_share_social_media)
        writer.write_collection_of_primitive_values("extsArchive", self.exts_archive)
        writer.write_collection_of_primitive_values("extsAudio", self.exts_audio)
        writer.write_collection_of_primitive_values("extsCoAuthoring", self.exts_co_authoring)
        writer.write_object_value("extsConvertible", self.exts_convertible)
        writer.write_collection_of_primitive_values("extsDocument", self.exts_document)
        writer.write_collection_of_primitive_values("extsImage", self.exts_image)
        writer.write_collection_of_primitive_values("extsImagePreviewed", self.exts_image_previewed)
        writer.write_collection_of_primitive_values("extsMediaPreviewed", self.exts_media_previewed)
        writer.write_collection_of_primitive_values("extsMustConvert", self.exts_must_convert)
        writer.write_collection_of_primitive_values("extsPresentation", self.exts_presentation)
        writer.write_collection_of_primitive_values("extsSpreadsheet", self.exts_spreadsheet)
        writer.write_collection_of_primitive_values("extsUploadable", self.exts_uploadable)
        writer.write_collection_of_primitive_values("extsVideo", self.exts_video)
        writer.write_collection_of_primitive_values("extsWebCommented", self.exts_web_commented)
        writer.write_collection_of_primitive_values("extsWebCustomFilterEditing", self.exts_web_custom_filter_editing)
        writer.write_collection_of_primitive_values("extsWebEdited", self.exts_web_edited)
        writer.write_collection_of_primitive_values("extsWebEncrypt", self.exts_web_encrypt)
        writer.write_collection_of_primitive_values("extsWebPreviewed", self.exts_web_previewed)
        writer.write_collection_of_primitive_values("extsWebRestrictedEditing", self.exts_web_restricted_editing)
        writer.write_collection_of_primitive_values("extsWebReviewed", self.exts_web_reviewed)
        writer.write_collection_of_primitive_values("extsWebTemplate", self.exts_web_template)
        writer.write_bool_value("favoritesSection", self.favorites_section)
        writer.write_str_value("fileDownloadUrlString", self.file_download_url_string)
        writer.write_str_value("fileRedirectPreviewUrlString", self.file_redirect_preview_url_string)
        writer.write_str_value("fileThumbnailUrlString", self.file_thumbnail_url_string)
        writer.write_str_value("fileWebEditorExternalUrlString", self.file_web_editor_external_url_string)
        writer.write_str_value("fileWebEditorUrlString", self.file_web_editor_url_string)
        writer.write_str_value("fileWebViewerExternalUrlString", self.file_web_viewer_external_url_string)
        writer.write_str_value("fileWebViewerUrlString", self.file_web_viewer_url_string)
        writer.write_bool_value("forcesave", self.forcesave)
        writer.write_bool_value("hideConfirmConvertOpen", self.hide_confirm_convert_open)
        writer.write_bool_value("hideConfirmConvertSave", self.hide_confirm_convert_save)
        writer.write_object_value("internalFormats", self.internal_formats)
        writer.write_bool_value("keepNewFileName", self.keep_new_file_name)
        writer.write_str_value("masterFormExtension", self.master_form_extension)
        writer.write_int_value("maxUploadThreadCount", self.max_upload_thread_count)
        writer.write_bool_value("openEditorInSameTab", self.open_editor_in_same_tab)
        writer.write_str_value("paramOutType", self.param_out_type)
        writer.write_str_value("paramVersion", self.param_version)
        writer.write_bool_value("recentSection", self.recent_section)
        writer.write_bool_value("storeForcesave", self.store_forcesave)
        writer.write_bool_value("storeOriginalFiles", self.store_original_files)
        writer.write_bool_value("templatesSection", self.templates_section)
    

