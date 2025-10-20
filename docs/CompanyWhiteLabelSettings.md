# CompanyWhiteLabelSettings
The company white label settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | The company name. | [optional] 
**site** | **str** | The company site. | [optional] 
**email** | **str** | The company email address. | [optional] 
**address** | **str** | The company address. | [optional] 
**phone** | **str** | The company phone number. | [optional] 
**is_licensor** | **bool** | Specifies if a company is a licensor or not. | [optional] 
**hide_about** | **bool** | Specifies if the About page is visible or not | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.company_white_label_settings import CompanyWhiteLabelSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWhiteLabelSettings from a JSON string
company_white_label_settings_instance = CompanyWhiteLabelSettings.from_json(json)
# print the JSON string representation of the object
print(CompanyWhiteLabelSettings.to_json())

# convert the object into a dict
company_white_label_settings_dict = company_white_label_settings_instance.to_dict()
# create an instance of CompanyWhiteLabelSettings from a dict
company_white_label_settings_from_dict = CompanyWhiteLabelSettings.from_dict(company_white_label_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


