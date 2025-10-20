# CoverRequestDto
The request parameters to change the room cover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The cover color. | [optional] 
**cover** | **str** | The cover name. | [optional] 

## Example

```python
from docspace_api_sdk.models.cover_request_dto import CoverRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CoverRequestDto from a JSON string
cover_request_dto_instance = CoverRequestDto.from_json(json)
# print the JSON string representation of the object
print(CoverRequestDto.to_json())

# convert the object into a dict
cover_request_dto_dict = cover_request_dto_instance.to_dict()
# create an instance of CoverRequestDto from a dict
cover_request_dto_from_dict = CoverRequestDto.from_dict(cover_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


