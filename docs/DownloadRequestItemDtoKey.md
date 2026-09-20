# DownloadRequestItemDtoKey
The file to convert and pack, by id — a number for a file stored in the portal itself, a string for a file on  a connected third-party account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.download_request_item_dto_key import DownloadRequestItemDtoKey

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadRequestItemDtoKey from a JSON string
download_request_item_dto_key_instance = DownloadRequestItemDtoKey.from_json(json)
# print the JSON string representation of the object
print(DownloadRequestItemDtoKey.to_json())

# convert the object into a dict
download_request_item_dto_key_dict = download_request_item_dto_key_instance.to_dict()
# create an instance of DownloadRequestItemDtoKey from a dict
download_request_item_dto_key_from_dict = DownloadRequestItemDtoKey.from_dict(download_request_item_dto_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


