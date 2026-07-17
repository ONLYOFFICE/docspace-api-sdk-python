# UpdateProviderBody
Parameters for updating an AI provider's configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The new display title for the AI provider. If null, the title is not changed. | [optional] 
**url** | **str** | The new API endpoint URL for the AI provider. If null, the URL is not changed. | [optional] 
**key** | **str** | The new authentication API key for the AI provider. If null, the key is not changed. | [optional] 
**model_settings** | [**List[ModelSettingsItemDto]**](ModelSettingsItemDto.md) | Optional list of model settings changes to apply atomically with the provider update. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_provider_body import UpdateProviderBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProviderBody from a JSON string
update_provider_body_instance = UpdateProviderBody.from_json(json)
# print the JSON string representation of the object
print(UpdateProviderBody.to_json())

# convert the object into a dict
update_provider_body_dict = update_provider_body_instance.to_dict()
# create an instance of UpdateProviderBody from a dict
update_provider_body_from_dict = UpdateProviderBody.from_dict(update_provider_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


