# FilesSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exts_image_previewed** | **List[str]** | Exts image previewed | [optional] 
**exts_media_previewed** | **List[str]** | Exts media previewed | [optional] 
**exts_web_previewed** | **List[str]** | Exts web previewed | [optional] 
**exts_web_edited** | **List[str]** | Exts web edited | [optional] 
**exts_web_encrypt** | **List[str]** | Exts web encrypt | [optional] 
**exts_web_reviewed** | **List[str]** | Exts web reviewed | [optional] 
**exts_web_custom_filter_editing** | **List[str]** | Exts web custom filter editing | [optional] 
**exts_web_restricted_editing** | **List[str]** | Exts web restricted editing | [optional] 
**exts_web_commented** | **List[str]** | Exts web commented | [optional] 
**exts_web_template** | **List[str]** | Exts web template | [optional] 
**exts_co_authoring** | **List[str]** | Exts co authoring | [optional] 
**exts_must_convert** | **List[str]** | Exts must convert | [optional] 
**exts_convertible** | **Dict[str, Optional[List[str]]]** | Exts convertible | [optional] 
**exts_uploadable** | **List[str]** | Exts uploadable | [optional] 
**exts_archive** | **List[str]** | Exts archive | [optional] 
**exts_video** | **List[str]** | Exts video | [optional] 
**exts_audio** | **List[str]** | Exts audio | [optional] 
**exts_image** | **List[str]** | Exts image | [optional] 
**exts_spreadsheet** | **List[str]** | Exts spreadsheet | [optional] 
**exts_presentation** | **List[str]** | Exts presentation | [optional] 
**exts_document** | **List[str]** | Exts document | [optional] 
**internal_formats** | [**FilesSettingsDtoInternalFormats**](FilesSettingsDtoInternalFormats.md) |  | [optional] 
**master_form_extension** | **str** | Master form extension | [optional] 
**param_version** | **str** | Param version | [optional] 
**param_out_type** | **str** | Param out type | [optional] 
**file_download_url_string** | **str** | File download url string | [optional] 
**file_web_viewer_url_string** | **str** | File web viewer url string | [optional] 
**file_web_viewer_external_url_string** | **str** | File web viewer external url string | [optional] 
**file_web_editor_url_string** | **str** | File web editor url string | [optional] 
**file_web_editor_external_url_string** | **str** | File web editor external url string | [optional] 
**file_redirect_preview_url_string** | **str** | File redirect preview url string | [optional] 
**file_thumbnail_url_string** | **str** | File thumbnail url string | [optional] 
**confirm_delete** | **bool** | Confirm delete | [optional] 
**enable_third_party** | **bool** | EnableT third party | [optional] 
**external_share** | **bool** | External share | [optional] 
**external_share_social_media** | **bool** | External share social media | [optional] 
**store_original_files** | **bool** | Store original files | [optional] 
**keep_new_file_name** | **bool** | Keep new file name | [optional] 
**display_file_extension** | **bool** | Display file extension | [optional] 
**convert_notify** | **bool** | Convert notify | [optional] 
**hide_confirm_cancel_operation** | **bool** | Hide confirm cancel operation | [optional] 
**hide_confirm_convert_save** | **bool** | HideC confirm convert save | [optional] 
**hide_confirm_convert_open** | **bool** | Hide confirm convert open | [optional] 
**hide_confirm_room_lifetime** | **bool** | Hide confirm room lifetime | [optional] 
**default_order** | [**OrderBy**](OrderBy.md) |  | [optional] 
**forcesave** | **bool** | Forcesave | [optional] 
**store_forcesave** | **bool** | Store forcesave | [optional] 
**recent_section** | **bool** | Recent section | [optional] 
**favorites_section** | **bool** | Favorites section | [optional] 
**templates_section** | **bool** | Templates section | [optional] 
**download_tar_gz** | **bool** | Download tar gz | [optional] 
**automatically_clean_up** | [**AutoCleanUpData**](AutoCleanUpData.md) |  | [optional] 
**can_search_by_content** | **bool** | Can search by content | [optional] 
**default_sharing_access_rights** | [**List[FileShare]**](FileShare.md) | Default sharing access rights | [optional] 
**max_upload_thread_count** | **int** | Max upload thread count | [optional] 
**chunk_upload_size** | **int** | Chunk upload size | [optional] 
**open_editor_in_same_tab** | **bool** | Open editor in same tab | [optional] 

## Example

```python
from docspace.models.files_settings_dto import FilesSettingsDto

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


