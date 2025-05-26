# TerminateRequestDto

The request parameters for terminating the reassignment/deletion process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user ID whose data is reassigned/removed. | 

## Example

```python
from docspace.models.terminate_request_dto import TerminateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateRequestDto from a JSON string
terminate_request_dto_instance = TerminateRequestDto.from_json(json)
# print the JSON string representation of the object
print(TerminateRequestDto.to_json())

# convert the object into a dict
terminate_request_dto_dict = terminate_request_dto_instance.to_dict()
# create an instance of TerminateRequestDto from a dict
terminate_request_dto_from_dict = TerminateRequestDto.from_dict(terminate_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


