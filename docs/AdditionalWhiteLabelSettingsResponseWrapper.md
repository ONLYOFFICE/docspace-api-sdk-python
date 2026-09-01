# AdditionalWhiteLabelSettingsResponseWrapper
The successful API response containing the AdditionalWhiteLabelSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AdditionalWhiteLabelSettings**](AdditionalWhiteLabelSettings.md) | The AdditionalWhiteLabelSettings object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.additional_white_label_settings_response_wrapper import AdditionalWhiteLabelSettingsResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalWhiteLabelSettingsResponseWrapper from a JSON string
additional_white_label_settings_response_wrapper_instance = AdditionalWhiteLabelSettingsResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(AdditionalWhiteLabelSettingsResponseWrapper.to_json())

# convert the object into a dict
additional_white_label_settings_response_wrapper_dict = additional_white_label_settings_response_wrapper_instance.to_dict()
# create an instance of AdditionalWhiteLabelSettingsResponseWrapper from a dict
additional_white_label_settings_response_wrapper_from_dict = AdditionalWhiteLabelSettingsResponseWrapper.from_dict(additional_white_label_settings_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


