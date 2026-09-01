# CompanyWhiteLabelSettingsResponseWrapper
The successful API response containing the CompanyWhiteLabelSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CompanyWhiteLabelSettings**](CompanyWhiteLabelSettings.md) | The CompanyWhiteLabelSettings object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.company_white_label_settings_response_wrapper import CompanyWhiteLabelSettingsResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWhiteLabelSettingsResponseWrapper from a JSON string
company_white_label_settings_response_wrapper_instance = CompanyWhiteLabelSettingsResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(CompanyWhiteLabelSettingsResponseWrapper.to_json())

# convert the object into a dict
company_white_label_settings_response_wrapper_dict = company_white_label_settings_response_wrapper_instance.to_dict()
# create an instance of CompanyWhiteLabelSettingsResponseWrapper from a dict
company_white_label_settings_response_wrapper_from_dict = CompanyWhiteLabelSettingsResponseWrapper.from_dict(company_white_label_settings_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


