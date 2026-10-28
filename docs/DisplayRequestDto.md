# DisplayRequestDto
The body of a file settings switch that turns something on or makes it visible.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | The state to store for the setting the operation addresses: true enables it or shows what it governs, false  disables or hides it. What exactly is affected, and whether the value belongs to the calling account or to the  whole portal, are stated by the operation that binds this body. The portal may store a different value than  the one sent when another setting overrides it, so read the answer rather than assuming. | [optional] 

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


