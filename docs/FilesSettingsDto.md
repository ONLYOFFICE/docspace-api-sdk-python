# FilesSettingsDto
The file settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exts_image_previewed** | **List[str]** | The list of extensions of the viewed images. | [optional] 
**exts_media_previewed** | **List[str]** | The list of extensions of the viewed media files. | [optional] 
**exts_web_previewed** | **List[str]** | The list of extensions of the viewed files. | [optional] 
**exts_web_edited** | **List[str]** | The list of extensions of the edited files. | [optional] 
**exts_web_encrypt** | **List[str]** | The list of extensions of the encrypted files. | [optional] 
**exts_web_reviewed** | **List[str]** | The list of extensions of the reviewed files. | [optional] 
**exts_web_custom_filter_editing** | **List[str]** | The list of extensions of the custom filter files. | [optional] 
**exts_web_restricted_editing** | **List[str]** | The list of extensions of the files that are restricted for editing. | [optional] 
**exts_web_commented** | **List[str]** | The list of extensions of the commented files. | [optional] 
**exts_web_template** | **List[str]** | The list of extensions of the template files. | [optional] 
**exts_co_authoring** | **List[str]** | The list of extensions of the co-authoring files. | [optional] 
**exts_must_convert** | **List[str]** | The list of extensions of the files that must be converted. | [optional] 
**exts_convertible** | **Dict[str, Optional[List[str]]]** | The list of the convertible extensions. | [optional] 
**exts_uploadable** | **List[str]** | The list of the uploadable extensions. | [optional] 
**exts_archive** | **List[str]** | The list of extensions of the archive files. | [optional] 
**exts_video** | **List[str]** | The list of the video extensions. | [optional] 
**exts_audio** | **List[str]** | The list of the audio extensions. | [optional] 
**exts_image** | **List[str]** | The list of the image extensions. | [optional] 
**exts_spreadsheet** | **List[str]** | The list of the spreadsheet extensions. | [optional] 
**exts_presentation** | **List[str]** | The list of the presentation extensions. | [optional] 
**exts_document** | **List[str]** | The list of the text document extensions. | [optional] 
**exts_diagram** | **List[str]** | The list of the diagram extensions. | [optional] 
**internal_formats** | [**FilesSettingsDtoInternalFormats**](FilesSettingsDtoInternalFormats.md) |  | [optional] 
**master_form_extension** | **str** | The master form extension. | [optional] 
**param_version** | **str** | The URL parameter which specifies the file version. | [optional] 
**param_out_type** | **str** | The URL parameter which specifies the output type of the converted file. | [optional] 
**file_download_url_string** | **str** | The URL to download a file. | [optional] 
**file_web_viewer_url_string** | **str** | The URL to the file web viewer. | [optional] 
**file_web_viewer_external_url_string** | **str** | The external URL to the file web viewer. | [optional] 
**file_web_editor_url_string** | **str** | The URL to the file web editor. | [optional] 
**file_web_editor_external_url_string** | **str** | The external URL to the file web editor. | [optional] 
**file_redirect_preview_url_string** | **str** | The redirect URL to the file viewer. | [optional] 
**file_thumbnail_url_string** | **str** | The URL to the file thumbnail. | [optional] 
**confirm_delete** | **bool** | Specifies whether to confirm the file deletion or not. | [optional] 
**enable_third_party** | **bool** | Specifies whether to allow users to connect the third-party storages. | [optional] 
**external_share** | **bool** | Specifies whether to enable sharing external links to the files. | [optional] 
**external_share_social_media** | **bool** | Specifies whether to enable sharing files on social media. | [optional] 
**store_original_files** | **bool** | Specifies whether to enable storing original files. | [optional] 
**keep_new_file_name** | **bool** | Specifies whether to keep the new file name. | [optional] 
**display_file_extension** | **bool** | Specifies whether to display the file extension. | [optional] 
**convert_notify** | **bool** | Specifies whether to display the conversion notification. | [optional] 
**hide_confirm_cancel_operation** | **bool** | Specifies whether to hide the confirmation dialog for the cancel operation. | [optional] 
**hide_confirm_convert_save** | **bool** | Specifies whether to hide the confirmation dialog  for saving the file copy in the original format when converting a file. | [optional] 
**hide_confirm_convert_open** | **bool** | Specifies whether to hide the confirmation dialog  for opening the conversion result. | [optional] 
**hide_confirm_room_lifetime** | **bool** | Specifies whether to hide the confirmation dialog about the file lifetime in the room. | [optional] 
**default_order** | [**OrderBy**](OrderBy.md) |  | [optional] 
**forcesave** | **bool** | Specifies whether to forcesave the files or not. | [optional] 
**store_forcesave** | **bool** | Specifies whether to store the forcesaved file versions or not. | [optional] 
**recent_section** | **bool** | Specifies if the \&quot;Recent\&quot; section is displayed or not. | [optional] 
**favorites_section** | **bool** | Specifies if the \&quot;Favorites\&quot; section is displayed or not. | [optional] 
**templates_section** | **bool** | Specifies if the \&quot;Templates\&quot; section is displayed or not. | [optional] 
**download_tar_gz** | **bool** | Specifies whether to download the .tar.gz files or not. | [optional] 
**automatically_clean_up** | [**AutoCleanUpData**](AutoCleanUpData.md) |  | [optional] 
**can_search_by_content** | **bool** | Specifies whether the file can be searched by its content or not. | [optional] 
**default_sharing_access_rights** | **List[int]** | The default access rights in sharing settings. | [optional] 
**max_upload_thread_count** | **int** | The maximum number of upload threads. | [optional] 
**chunk_upload_size** | **int** | The size of a large file that is uploaded in chunks. | [optional] 
**open_editor_in_same_tab** | **bool** | Specifies whether to open the editor in the same tab or not. | [optional] 

## Example

```python
from docspace-api-python.models.files_settings_dto import FilesSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FilesSettingsDto from a JSON string
files_settings_dto_instance = FilesSettingsDto.from_json(json)
# print the JSON string representation of the object
print(FilesSettingsDto.to_json())

# convert the object into a dict
files_settings_dto_dict = files_settings_dto_instance.to_dict()
# create an instance of FilesSettingsDto from a dict
files_settings_dto_from_dict = FilesSettingsDto.from_dict(files_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


