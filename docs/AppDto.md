# AppDto
The portal application information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The application identifier (stable slug). The client maps this to its title, description and icon. | [optional] 
**enabled** | **bool** | Whether the application is enabled for the current tenant. | [optional] 
**settings** | [**AppDtoSettings**](AppDtoSettings.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.app_dto import AppDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppDto from a JSON string
app_dto_instance = AppDto.from_json(json)
# print the JSON string representation of the object
print(AppDto.to_json())

# convert the object into a dict
app_dto_dict = app_dto_instance.to_dict()
# create an instance of AppDto from a dict
app_dto_from_dict = AppDto.from_dict(app_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


