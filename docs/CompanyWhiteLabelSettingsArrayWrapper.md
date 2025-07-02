# CompanyWhiteLabelSettingsArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CompanyWhiteLabelSettings]**](CompanyWhiteLabelSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.company_white_label_settings_array_wrapper import CompanyWhiteLabelSettingsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWhiteLabelSettingsArrayWrapper from a JSON string
company_white_label_settings_array_wrapper_instance = CompanyWhiteLabelSettingsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(CompanyWhiteLabelSettingsArrayWrapper.to_json())

# convert the object into a dict
company_white_label_settings_array_wrapper_dict = company_white_label_settings_array_wrapper_instance.to_dict()
# create an instance of CompanyWhiteLabelSettingsArrayWrapper from a dict
company_white_label_settings_array_wrapper_from_dict = CompanyWhiteLabelSettingsArrayWrapper.from_dict(company_white_label_settings_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


