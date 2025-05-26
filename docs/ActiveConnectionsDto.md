# ActiveConnectionsDto

The active connections parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_event** | **int** | The login event. | [optional] 
**items** | [**List[ActiveConnectionsItemDto]**](ActiveConnectionsItemDto.md) | The list of active connection items. | [optional] 

## Example

```python
from docspace.models.active_connections_dto import ActiveConnectionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveConnectionsDto from a JSON string
active_connections_dto_instance = ActiveConnectionsDto.from_json(json)
# print the JSON string representation of the object
print(ActiveConnectionsDto.to_json())

# convert the object into a dict
active_connections_dto_dict = active_connections_dto_instance.to_dict()
# create an instance of ActiveConnectionsDto from a dict
active_connections_dto_from_dict = ActiveConnectionsDto.from_dict(active_connections_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


