# CustomizationConfigDto
The customization config parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **bool** | Specifies if the customization is about. | [optional] 
**customer** | [**CustomerConfigDto**](CustomerConfigDto.md) |  | [optional] 
**anonymous** | [**AnonymousConfigDto**](AnonymousConfigDto.md) |  | [optional] 
**feedback** | [**FeedbackConfig**](FeedbackConfig.md) |  | [optional] 
**forcesave** | **bool** | Specifies if the customization should be force saved. | [optional] 
**goback** | [**GobackConfig**](GobackConfig.md) |  | [optional] 
**review** | [**ReviewConfig**](ReviewConfig.md) |  | [optional] 
**logo** | [**LogoConfigDto**](LogoConfigDto.md) |  | [optional] 
**mention_share** | **bool** | Specifies if the share should be mentioned. | [optional] 
**submit_form** | [**SubmitForm**](SubmitForm.md) |  | [optional] 
**start_filling_form** | [**StartFillingForm**](StartFillingForm.md) |  | [optional] 

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


