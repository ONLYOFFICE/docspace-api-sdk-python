# AppDto
One feature module of the portal: whether it is switched on here, and the settings stored for it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The application's stable key, declared in the installation configuration - `ai-rooms`, `docs-cloud` and  the like. It is what every other operation of this group addresses an application by, and a client maps it  to a title and an icon of its own; the portal ships no display name for it. | [optional] 
**enabled** | **bool** | Whether the application is switched on for this portal. It is the portal's own flag where one has been  saved, and the default the installation configuration gives the application otherwise. | [optional] 
**settings** | **object** |  | [optional] 

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


