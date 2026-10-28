# AutoCleanupRequestDto
The trash auto-clearing setting to store: the on/off flag together with the interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | Whether the caller's trash is cleared automatically: with true an item is removed for good once it has been in  the trash longer than the interval below, with false the portal removes nothing and waits for the trash to be  emptied by hand. | [optional] 
**gap** | [**DateToAutoCleanUp**](DateToAutoCleanUp.md) | How long an item may stay in the trash before it is removed for good. It is written from every request,  including one that switches clearing off, so send it together with the flag instead of expecting the stored  interval to be kept. | [optional] 

## Example

```python
from docspace_api_sdk.models.auto_cleanup_request_dto import AutoCleanupRequestDto

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


