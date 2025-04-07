# ConfigurationDtoInteger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**DocumentConfigDto**](DocumentConfigDto.md) |  | [optional] 
**document_type** | **str** | Document type | [optional] 
**editor_config** | [**EditorConfigurationDto**](EditorConfigurationDto.md) |  | [optional] 
**editor_type** | [**EditorType**](EditorType.md) |  | [optional] 
**editor_url** | **str** | Editor URL | [optional] 
**token** | **str** | Token | [optional] 
**type** | **str** | Platform type | [optional] 
**file** | [**FileDtoInteger**](FileDtoInteger.md) |  | [optional] 
**error_message** | **str** | Error message | [optional] 
**start_filling** | **bool** | Specifies if the filling has started or not | [optional] 
**filling_session_id** | **str** | Filling session Id | [optional] 

## Example

```python
from docspace.models.configuration_dto_integer import ConfigurationDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationDtoInteger from a JSON string
configuration_dto_integer_instance = ConfigurationDtoInteger.from_json(json)
# print the JSON string representation of the object
print(ConfigurationDtoInteger.to_json())

# convert the object into a dict
configuration_dto_integer_dict = configuration_dto_integer_instance.to_dict()
# create an instance of ConfigurationDtoInteger from a dict
configuration_dto_integer_from_dict = ConfigurationDtoInteger.from_dict(configuration_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


