# SetServerStatusRequestBody
Parameters for toggling the MCP server status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Set to true to enable the server (making it available for room assignment), or false to disable it. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_server_status_request_body import SetServerStatusRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetServerStatusRequestBody from a JSON string
set_server_status_request_body_instance = SetServerStatusRequestBody.from_json(json)
# print the JSON string representation of the object
print(SetServerStatusRequestBody.to_json())

# convert the object into a dict
set_server_status_request_body_dict = set_server_status_request_body_instance.to_dict()
# create an instance of SetServerStatusRequestBody from a dict
set_server_status_request_body_from_dict = SetServerStatusRequestBody.from_dict(set_server_status_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


