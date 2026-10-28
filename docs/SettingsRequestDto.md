# SettingsRequestDto
The body of a file settings switch: a single flag carrying the state to store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | The state to store for the setting the operation addresses: true switches it on, false switches it off. The  flag carries no meaning of its own - what is switched, who is allowed to switch it, and whether the value  belongs to the calling account or to the whole portal are stated by the operation that binds this body. The  answer repeats the value the portal read back afterwards, which is not always the one that was sent. | [optional] 

## Example

```python
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsRequestDto from a JSON string
settings_request_dto_instance = SettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(SettingsRequestDto.to_json())

# convert the object into a dict
settings_request_dto_dict = settings_request_dto_instance.to_dict()
# create an instance of SettingsRequestDto from a dict
settings_request_dto_from_dict = SettingsRequestDto.from_dict(settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


