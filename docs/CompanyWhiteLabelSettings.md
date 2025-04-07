# CompanyWhiteLabelSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Company name | [optional] 
**site** | **str** | Site | [optional] 
**email** | **str** | Email address | [optional] 
**address** | **str** | Address | [optional] 
**phone** | **str** | Phone | [optional] 
**is_licensor** | **bool** | Specifies if a company is a licensor or not | [optional] 

## Example

```python
from docspace.models.company_white_label_settings import CompanyWhiteLabelSettings

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


