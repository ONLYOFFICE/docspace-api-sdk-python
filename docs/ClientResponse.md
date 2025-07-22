# ClientResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The client name. | [optional] 
**description** | **str** | The client description. | [optional] 
**tenant** | **int** | The tenant ID associated with the client. | [optional] 
**scopes** | **List[str]** | The client scopes. | [optional] 
**enabled** | **bool** | Specifies if the client is currently enabled or not. | [optional] 
**client_id** | **str** | The client identifier issued to the client during registration. | [optional] 
**client_secret** | **str** | The client secret issued to the client during registration. | [optional] 
**website_url** | **str** | The URL to the client&#39;s website. | [optional] 
**terms_url** | **str** | The URL to the client&#39;s terms of service. | [optional] 
**policy_url** | **str** | The URL to the client&#39;s privacy policy. | [optional] 
**logo** | **str** | The URL to the client&#39;s logo. | [optional] 
**authentication_methods** | **List[str]** | The authentication methods supported by the client. | [optional] 
**redirect_uris** | **List[str]** | The list of allowed redirect URIs. | [optional] 
**allowed_origins** | **List[str]** | The list of allowed CORS origins. | [optional] 
**logout_redirect_uris** | **List[str]** | The list of allowed logout redirect URIs. | [optional] 
**created_on** | **datetime** | The date and time when the client was created. | [optional] 
**created_by** | **str** | The user who created the client. | [optional] 
**modified_on** | **datetime** | The date and time when the client was last modified. | [optional] 
**modified_by** | **str** | The user who last modified the client. | [optional] 
**is_public** | **bool** | Indicates whether the client is accessible by third-party tenants. | [optional] 

## Example

```python
from docspace-api-sdk.models.client_response import ClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientResponse from a JSON string
client_response_instance = ClientResponse.from_json(json)
# print the JSON string representation of the object
print(ClientResponse.to_json())

# convert the object into a dict
client_response_dict = client_response_instance.to_dict()
# create an instance of ClientResponse from a dict
client_response_from_dict = ClientResponse.from_dict(client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


