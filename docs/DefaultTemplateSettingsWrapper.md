# DefaultTemplateSettingsWrapper
The successful API response containing the DefaultTemplateSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DefaultTemplateSettingsDto**](DefaultTemplateSettingsDto.md) | The DefaultTemplateSettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.default_template_settings_wrapper import DefaultTemplateSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultTemplateSettingsWrapper from a JSON string
default_template_settings_wrapper_instance = DefaultTemplateSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(DefaultTemplateSettingsWrapper.to_json())

# convert the object into a dict
default_template_settings_wrapper_dict = default_template_settings_wrapper_instance.to_dict()
# create an instance of DefaultTemplateSettingsWrapper from a dict
default_template_settings_wrapper_from_dict = DefaultTemplateSettingsWrapper.from_dict(default_template_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


