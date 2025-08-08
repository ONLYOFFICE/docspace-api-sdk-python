# ActiveConnectionsItemDto
The active connection item parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The active connection ID. | [optional] 
**tenant_id** | **int** | The tenant ID. | [optional] 
**user_id** | **str** | The user ID. | [optional] 
**mobile** | **bool** | Specifies if the active connection has a mobile phone or not. | [optional] 
**ip** | **str** | The IP address of the active connection. | [optional] 
**country** | **str** | The active connection country. | [optional] 
**city** | **str** | The active connection city. | [optional] 
**browser** | **str** | The active connection browser. | [optional] 
**platform** | **str** | The active connection platform. | [optional] 
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**page** | **str** | The active connection page. | [optional] 

## Example

```python
from docspace_api_sdk.models.active_connections_item_dto import ActiveConnectionsItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveConnectionsItemDto from a JSON string
active_connections_item_dto_instance = ActiveConnectionsItemDto.from_json(json)
# print the JSON string representation of the object
print(ActiveConnectionsItemDto.to_json())

# convert the object into a dict
active_connections_item_dto_dict = active_connections_item_dto_instance.to_dict()
# create an instance of ActiveConnectionsItemDto from a dict
active_connections_item_dto_from_dict = ActiveConnectionsItemDto.from_dict(active_connections_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


