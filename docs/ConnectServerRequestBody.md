# ConnectServerRequestBody
Parameters for completing an OAuth connection to an MCP server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | OAuth authorization code received from the provider's redirect. Used to exchange for access and refresh tokens. | 

## Example

```python
from docspace_api_sdk.models.connect_server_request_body import ConnectServerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectServerRequestBody from a JSON string
connect_server_request_body_instance = ConnectServerRequestBody.from_json(json)
# print the JSON string representation of the object
print(ConnectServerRequestBody.to_json())

# convert the object into a dict
connect_server_request_body_dict = connect_server_request_body_instance.to_dict()
# create an instance of ConnectServerRequestBody from a dict
connect_server_request_body_from_dict = ConnectServerRequestBody.from_dict(connect_server_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


