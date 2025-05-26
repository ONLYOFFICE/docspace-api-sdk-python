# DownloadRequestItemDto

The download request item with conversion parameters and security settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**DownloadRequestItemDtoKey**](DownloadRequestItemDtoKey.md) |  | 
**value** | **str** | The target format or conversion type for the file download. | 
**password** | **str** | The optional password for accessing protected files. | [optional] 

## Example

```python
from docspace.models.download_request_item_dto import DownloadRequestItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadRequestItemDto from a JSON string
download_request_item_dto_instance = DownloadRequestItemDto.from_json(json)
# print the JSON string representation of the object
print(DownloadRequestItemDto.to_json())

# convert the object into a dict
download_request_item_dto_dict = download_request_item_dto_instance.to_dict()
# create an instance of DownloadRequestItemDto from a dict
download_request_item_dto_from_dict = DownloadRequestItemDto.from_dict(download_request_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


