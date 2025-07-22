# CreateClientRequest
The request parameters for creating a client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The client name. | [optional] 
**description** | **str** | The client description. | [optional] 
**logo** | **str** | The client logo in base64 format. | [optional] 
**scopes** | **List[str]** | The client scopes. | [optional] 
**allow_pkce** | **bool** | Indicates whether PKCE is allowed for the client. | [optional] 
**is_public** | **bool** | Indicates whether the client is accessible by third-party tenants. | [optional] 
**website_url** | **str** | The URL to the client&#39;s website. | [optional] 
**terms_url** | **str** | The URL to the client&#39;s terms of service. | [optional] 
**policy_url** | **str** | The URL to the client&#39;s privacy policy. | [optional] 
**redirect_uris** | **List[str]** | The list of allowed redirect URIs. | 
**allowed_origins** | **List[str]** | The list of allowed CORS origins. | 
**logout_redirect_uri** | **str** | The list of allowed logout redirect URIs. | [optional] 

## Example

```python
from docspace-api-sdk.models.create_client_request import CreateClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientRequest from a JSON string
create_client_request_instance = CreateClientRequest.from_json(json)
# print the JSON string representation of the object
print(CreateClientRequest.to_json())

# convert the object into a dict
create_client_request_dict = create_client_request_instance.to_dict()
# create an instance of CreateClientRequest from a dict
create_client_request_from_dict = CreateClientRequest.from_dict(create_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


