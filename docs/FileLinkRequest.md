# FileLinkRequest
The external link request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_id** | **str** | The external link ID. | [optional] 
**access** | [**FileShare**](FileShare.md) |  | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**internal** | **bool** | The link scope, whether it is internal or not. | [optional] 
**primary** | **bool** | Specifies whether the file link is primary or not. | [optional] 

## Example

```python
from docspace-api-sdk.models.file_link_request import FileLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileLinkRequest from a JSON string
file_link_request_instance = FileLinkRequest.from_json(json)
# print the JSON string representation of the object
print(FileLinkRequest.to_json())

# convert the object into a dict
file_link_request_dict = file_link_request_instance.to_dict()
# create an instance of FileLinkRequest from a dict
file_link_request_from_dict = FileLinkRequest.from_dict(file_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


