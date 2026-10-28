# ActiveConnectionsDto
The connections the calling user currently has open, and which of them the request itself was made with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_event** | **int** | The `id` of the item in `items` that the current request is authenticated by. It is `0` when the request  carried a token in the `Authorization` header instead of the portal cookie, and in that case none of the  items is the current connection. | 
**items** | [**List[ActiveConnectionsItemDto]**](ActiveConnectionsItemDto.md) | One item per sign-in of the caller that is still active, ordered newest sign-in first, with the connection  the request itself uses moved to the front. Sign-ins older than a year are left out, and a caller with no  stored connection gets a single item describing the current request rather than an empty list. | [optional] 

## Example

```python
from docspace_api_sdk.models.active_connections_dto import ActiveConnectionsDto

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


