# ClientInfoResponse

The response containing public client information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The client name. | [optional] 
**description** | **str** | The client description. | [optional] 
**scopes** | **List[str]** | The client scopes. | [optional] 
**client_id** | **str** | The client ID. | [optional] 
**website_url** | **str** | The URL to the client&#39;s website | [optional] 
**terms_url** | **str** | The URL to the client&#39;s terms of service. | [optional] 
**policy_url** | **str** | The URL to the client&#39;s privacy policy. | [optional] 
**logo** | **str** | The client logo in base64 format. | [optional] 
**authentication_methods** | **List[str]** | The authentication methods supported by the client. | [optional] 
**is_public** | **bool** | Indicates whether the client is accessible by third-party tenants. | [optional] 
**created_on** | **datetime** | The date and time when the client was created. | [optional] 
**created_by** | **str** | The user who created the client. | [optional] 
**modified_on** | **datetime** | The date and time when the client was last modified. | [optional] 
**modified_by** | **str** | The user who last modified the client. | [optional] 

## Example

```python
from docspace.models.client_info_response import ClientInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientInfoResponse from a JSON string
client_info_response_instance = ClientInfoResponse.from_json(json)
# print the JSON string representation of the object
print(ClientInfoResponse.to_json())

# convert the object into a dict
client_info_response_dict = client_info_response_instance.to_dict()
# create an instance of ClientInfoResponse from a dict
client_info_response_from_dict = ClientInfoResponse.from_dict(client_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


