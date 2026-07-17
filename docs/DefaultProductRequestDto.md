# DefaultProductRequestDto
The request parameters for setting the default product configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_folder_type** | [**FolderType**](FolderType.md) |  | 

## Example

```python
from docspace_api_sdk.models.default_product_request_dto import DefaultProductRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultProductRequestDto from a JSON string
default_product_request_dto_instance = DefaultProductRequestDto.from_json(json)
# print the JSON string representation of the object
print(DefaultProductRequestDto.to_json())

# convert the object into a dict
default_product_request_dto_dict = default_product_request_dto_instance.to_dict()
# create an instance of DefaultProductRequestDto from a dict
default_product_request_dto_from_dict = DefaultProductRequestDto.from_dict(default_product_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


