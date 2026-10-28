# AdditionalWhiteLabelSettingsRequestDto
The body of a change to the help and community resources the interface offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**SaveAdditionalResourcesRequest**](SaveAdditionalResourcesRequest.md) | The resource flags to store. | [optional] 

## Example

```python
from docspace_api_sdk.models.additional_white_label_settings_request_dto import AdditionalWhiteLabelSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalWhiteLabelSettingsRequestDto from a JSON string
additional_white_label_settings_request_dto_instance = AdditionalWhiteLabelSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(AdditionalWhiteLabelSettingsRequestDto.to_json())

# convert the object into a dict
additional_white_label_settings_request_dto_dict = additional_white_label_settings_request_dto_instance.to_dict()
# create an instance of AdditionalWhiteLabelSettingsRequestDto from a dict
additional_white_label_settings_request_dto_from_dict = AdditionalWhiteLabelSettingsRequestDto.from_dict(additional_white_label_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


