# CompanyWhiteLabelSettingsDtoWrapper
The successful API response containing the CompanyWhiteLabelSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CompanyWhiteLabelSettingsDto**](CompanyWhiteLabelSettingsDto.md) | The CompanyWhiteLabelSettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.company_white_label_settings_dto_wrapper import CompanyWhiteLabelSettingsDtoWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWhiteLabelSettingsDtoWrapper from a JSON string
company_white_label_settings_dto_wrapper_instance = CompanyWhiteLabelSettingsDtoWrapper.from_json(json)
# print the JSON string representation of the object
print(CompanyWhiteLabelSettingsDtoWrapper.to_json())

# convert the object into a dict
company_white_label_settings_dto_wrapper_dict = company_white_label_settings_dto_wrapper_instance.to_dict()
# create an instance of CompanyWhiteLabelSettingsDtoWrapper from a dict
company_white_label_settings_dto_wrapper_from_dict = CompanyWhiteLabelSettingsDtoWrapper.from_dict(company_white_label_settings_dto_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


