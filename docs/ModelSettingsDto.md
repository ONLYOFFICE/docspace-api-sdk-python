# ModelSettingsDto
AI model settings information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The model identifier. | 
**alias** | **str** | The display name for the model. | [optional] 
**is_enabled** | **bool** | Whether the model is enabled for use in chat. | [optional] 
**is_recommended** | **bool** | Whether the model is recommended (defined in configuration). | [optional] 
**capabilities** | [**AiModelCapabilities**](AiModelCapabilities.md) |  | 

## Example

```python
from docspace_api_sdk.models.model_settings_dto import ModelSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSettingsDto from a JSON string
model_settings_dto_instance = ModelSettingsDto.from_json(json)
# print the JSON string representation of the object
print(ModelSettingsDto.to_json())

# convert the object into a dict
model_settings_dto_dict = model_settings_dto_instance.to_dict()
# create an instance of ModelSettingsDto from a dict
model_settings_dto_from_dict = ModelSettingsDto.from_dict(model_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


