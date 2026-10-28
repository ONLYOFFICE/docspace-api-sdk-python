# SocketSettingsDto
Where a client connects for the portal's live updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The base address of the Socket.IO hub that pushes file changes, presence and quota alerts, always with a  trailing slash. It is empty when the installation runs no hub, and a client must then fall back to  polling rather than guessing an address. The value comes from the installation's configuration and cannot  be changed through this API. | [optional] 

## Example

```python
from docspace_api_sdk.models.socket_settings_dto import SocketSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SocketSettingsDto from a JSON string
socket_settings_dto_instance = SocketSettingsDto.from_json(json)
# print the JSON string representation of the object
print(SocketSettingsDto.to_json())

# convert the object into a dict
socket_settings_dto_dict = socket_settings_dto_instance.to_dict()
# create an instance of SocketSettingsDto from a dict
socket_settings_dto_from_dict = SocketSettingsDto.from_dict(socket_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


