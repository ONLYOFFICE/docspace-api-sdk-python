# CustomizationConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **bool** | About | [optional] 
**customer** | [**CustomerConfigDto**](CustomerConfigDto.md) |  | [optional] 
**anonymous** | [**AnonymousConfigDto**](AnonymousConfigDto.md) |  | [optional] 
**feedback** | [**FeedbackConfig**](FeedbackConfig.md) |  | [optional] 
**forcesave** | **bool** | Forcesave | [optional] 
**goback** | [**GobackConfig**](GobackConfig.md) |  | [optional] 
**logo** | [**LogoConfigDto**](LogoConfigDto.md) |  | [optional] 
**mention_share** | **bool** | MentionShare | [optional] 
**review_display** | **str** | Review display | [optional] 
**submit_form** | **bool** | Submit form | [optional] 

## Example

```python
from docspace.models.customization_config_dto import CustomizationConfigDto

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


