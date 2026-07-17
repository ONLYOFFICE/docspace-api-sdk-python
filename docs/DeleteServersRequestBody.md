# DeleteServersRequestBody
Parameters specifying which MCP servers to delete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **List[UUID]** | Set of unique identifiers of the MCP servers to permanently remove. All room associations and connection data will also be deleted. | 

## Example

```python
from docspace_api_sdk.models.delete_servers_request_body import DeleteServersRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteServersRequestBody from a JSON string
delete_servers_request_body_instance = DeleteServersRequestBody.from_json(json)
# print the JSON string representation of the object
print(DeleteServersRequestBody.to_json())

# convert the object into a dict
delete_servers_request_body_dict = delete_servers_request_body_instance.to_dict()
# create an instance of DeleteServersRequestBody from a dict
delete_servers_request_body_from_dict = DeleteServersRequestBody.from_dict(delete_servers_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


