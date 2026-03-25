# UpdateServerRequestBody
Parameters for updating an existing MCP server. All fields are optional — only provided fields will be modified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New display name for the server. Only letters, numbers, underscores, and hyphens are allowed. Maximum 128 characters. | [optional] 
**description** | **str** | New human-readable description of the server&#39;s purpose. Maximum 255 characters. | [optional] 
**endpoint** | **str** | New base URL of the MCP server endpoint. If changed, the system will re-verify connectivity before saving. | [optional] 
**headers** | **Dict[str, str]** | New HTTP headers to include with every request. If changed alongside the endpoint, connectivity is re-verified. | [optional] 
**update_icon** | **bool** | Set to true to update the server icon. When true, the Icon field value (or null to remove) will be applied. | [optional] 
**icon** | **str** | New Base64-encoded icon image for the server, or null to remove the existing icon. Only applied when UpdateIcon is true. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_server_request_body import UpdateServerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerRequestBody from a JSON string
update_server_request_body_instance = UpdateServerRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateServerRequestBody.to_json())

# convert the object into a dict
update_server_request_body_dict = update_server_request_body_instance.to_dict()
# create an instance of UpdateServerRequestBody from a dict
update_server_request_body_from_dict = UpdateServerRequestBody.from_dict(update_server_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


