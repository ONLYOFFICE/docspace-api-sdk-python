# EnabledModuleDto
One portal module the calling user may open.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The module's product class name, HTML-escaped. It is a display-oriented identifier and not the GUID the  access-settings operations work with, so it must not be passed to `GET api/2.0/settings/security/{id}`. | [optional] 
**title** | **str** | The module name in the portal language, HTML-escaped and ready to be rendered as text. | [optional] 

## Example

```python
from docspace_api_sdk.models.enabled_module_dto import EnabledModuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of EnabledModuleDto from a JSON string
enabled_module_dto_instance = EnabledModuleDto.from_json(json)
# print the JSON string representation of the object
print(EnabledModuleDto.to_json())

# convert the object into a dict
enabled_module_dto_dict = enabled_module_dto_instance.to_dict()
# create an instance of EnabledModuleDto from a dict
enabled_module_dto_from_dict = EnabledModuleDto.from_dict(enabled_module_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


