# CompanyWhiteLabelSettingsDto

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
**is_default** | **bool** | Specifies if company white label settings are default or not. | [optional] 

## Example

```python
from docspace.models.company_white_label_settings_dto import CompanyWhiteLabelSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWhiteLabelSettingsDto from a JSON string
company_white_label_settings_dto_instance = CompanyWhiteLabelSettingsDto.from_json(json)
# print the JSON string representation of the object
print(CompanyWhiteLabelSettingsDto.to_json())

# convert the object into a dict
company_white_label_settings_dto_dict = company_white_label_settings_dto_instance.to_dict()
# create an instance of CompanyWhiteLabelSettingsDto from a dict
company_white_label_settings_dto_from_dict = CompanyWhiteLabelSettingsDto.from_dict(company_white_label_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


