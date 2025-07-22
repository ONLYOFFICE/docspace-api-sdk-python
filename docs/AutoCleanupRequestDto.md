# AutoCleanupRequestDto
The auto-clearing request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | Specifies whether to enable the auto-clearing or not. | [optional] 
**gap** | [**DateToAutoCleanUp**](DateToAutoCleanUp.md) |  | [optional] 

## Example

```python
from docspace-api-sdk.models.auto_cleanup_request_dto import AutoCleanupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AutoCleanupRequestDto from a JSON string
auto_cleanup_request_dto_instance = AutoCleanupRequestDto.from_json(json)
# print the JSON string representation of the object
print(AutoCleanupRequestDto.to_json())

# convert the object into a dict
auto_cleanup_request_dto_dict = auto_cleanup_request_dto_instance.to_dict()
# create an instance of AutoCleanupRequestDto from a dict
auto_cleanup_request_dto_from_dict = AutoCleanupRequestDto.from_dict(auto_cleanup_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


