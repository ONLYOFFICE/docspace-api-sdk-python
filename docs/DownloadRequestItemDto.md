# DownloadRequestItemDto
One file of a bulk download, together with the format it is converted to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**DownloadRequestItemDtoKey**](DownloadRequestItemDtoKey.md) |  | 
**value** | **str** | The format the file is converted to before it is packed, as a file extension without a leading dot. | 
**password** | **str** | The password that opens the source file, for a file protected with one; a protected file cannot be converted  without it. | [optional] 

## Example

```python
from docspace_api_sdk.models.download_request_item_dto import DownloadRequestItemDto

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


