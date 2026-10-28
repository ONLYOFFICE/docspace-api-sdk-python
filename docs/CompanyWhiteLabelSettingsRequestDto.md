# CompanyWhiteLabelSettingsRequestDto
The body of a company details change for the installation's branding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**SaveCompanyInfoRequest**](SaveCompanyInfoRequest.md) | The company details to store. | [optional] 

## Example

```python
from docspace_api_sdk.models.company_white_label_settings_request_dto import CompanyWhiteLabelSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyWhiteLabelSettingsRequestDto from a JSON string
company_white_label_settings_request_dto_instance = CompanyWhiteLabelSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(CompanyWhiteLabelSettingsRequestDto.to_json())

# convert the object into a dict
company_white_label_settings_request_dto_dict = company_white_label_settings_request_dto_instance.to_dict()
# create an instance of CompanyWhiteLabelSettingsRequestDto from a dict
company_white_label_settings_request_dto_from_dict = CompanyWhiteLabelSettingsRequestDto.from_dict(company_white_label_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


