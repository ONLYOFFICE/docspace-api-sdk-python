# DisplayRequestDto
The settings request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | Specifies whether to set the specified settings or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.display_request_dto import DisplayRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayRequestDto from a JSON string
display_request_dto_instance = DisplayRequestDto.from_json(json)
# print the JSON string representation of the object
print(DisplayRequestDto.to_json())

# convert the object into a dict
display_request_dto_dict = display_request_dto_instance.to_dict()
# create an instance of DisplayRequestDto from a dict
display_request_dto_from_dict = DisplayRequestDto.from_dict(display_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


