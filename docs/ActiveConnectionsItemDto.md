# ActiveConnectionsItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id | [optional] 
**tenant_id** | **int** | Tenant id | [optional] 
**user_id** | **str** | User id | [optional] 
**mobile** | **bool** | Mobile | [optional] 
**ip** | **str** | Ip | [optional] 
**country** | **str** | Country | [optional] 
**city** | **str** | City | [optional] 
**browser** | **str** | Browser | [optional] 
**platform** | **str** | Platform | [optional] 
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**page** | **str** | Page | [optional] 

## Example

```python
from docspace.models.active_connections_item_dto import ActiveConnectionsItemDto

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


