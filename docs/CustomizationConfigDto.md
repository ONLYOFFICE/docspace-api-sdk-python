# CustomizationConfigDto
The customization config parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **bool** | Specifies if the customization is about. | [optional] 
**customer** | [**CustomerConfigDto**](CustomerConfigDto.md) | The customization customer configuration. | [optional] 
**anonymous** | [**AnonymousConfigDto**](AnonymousConfigDto.md) | The anonymous configuration of the customization. | [optional] 
**feedback** | [**FeedbackConfig**](FeedbackConfig.md) | The feedback configuration of the customization. | [optional] 
**forcesave** | **bool** | Specifies if the customization should be force saved. | [optional] 
**goback** | [**GobackConfig**](GobackConfig.md) | The go back configuration of the customization. | [optional] 
**review** | [**ReviewConfig**](ReviewConfig.md) | The review configuration of the customization. | [optional] 
**logo** | [**LogoConfigDto**](LogoConfigDto.md) | The logo of the customization. | [optional] 
**mention_share** | **bool** | Specifies if the share should be mentioned. | [optional] 
**submit_form** | [**SubmitForm**](SubmitForm.md) | The Complete & Submit button settings. | [optional] 
**start_filling_form** | [**StartFillingForm**](StartFillingForm.md) | The parameters of the button that starts filling out the form. | [optional] 

## Example

```python
from docspace_api_sdk.models.customization_config_dto import CustomizationConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationConfigDto from a JSON string
customization_config_dto_instance = CustomizationConfigDto.from_json(json)
# print the JSON string representation of the object
print(CustomizationConfigDto.to_json())

# convert the object into a dict
customization_config_dto_dict = customization_config_dto_instance.to_dict()
# create an instance of CustomizationConfigDto from a dict
customization_config_dto_from_dict = CustomizationConfigDto.from_dict(customization_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


