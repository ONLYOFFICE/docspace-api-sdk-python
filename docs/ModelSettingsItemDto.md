# ModelSettingsItemDto
A single model settings entry within a provider create or update request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | The model identifier. | 
**is_enabled** | **bool** | Whether the model is enabled for use in chat. | [optional] 
**alias** | **str** | The display name for the model. Only applies to non-recommended models. | [optional] 
**capabilities** | [**AiModelCapabilities**](AiModelCapabilities.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.model_settings_item_dto import ModelSettingsItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSettingsItemDto from a JSON string
model_settings_item_dto_instance = ModelSettingsItemDto.from_json(json)
# print the JSON string representation of the object
print(ModelSettingsItemDto.to_json())

# convert the object into a dict
model_settings_item_dto_dict = model_settings_item_dto_instance.to_dict()
# create an instance of ModelSettingsItemDto from a dict
model_settings_item_dto_from_dict = ModelSettingsItemDto.from_dict(model_settings_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


