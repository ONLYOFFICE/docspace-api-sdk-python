# CreateClientRequest

Client creation request containing client details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the client | [optional] 
**description** | **str** | The description of the client | [optional] 
**logo** | **str** | The logo of the client in base64 format | [optional] 
**scopes** | **List[str]** | The scopes for the client | [optional] 
**allow_pkce** | **bool** | Indicates whether PKCE is allowed for the client | [optional] 
**is_public** | **bool** | Indicates if the client is public | [optional] 
**website_url** | **str** | The website URL of the client | [optional] 
**terms_url** | **str** | The terms URL of the client | [optional] 
**policy_url** | **str** | The policy URL of the client | [optional] 
**redirect_uris** | **List[str]** | The redirect URIs for the client | 
**allowed_origins** | **List[str]** | The allowed origins for the client | 
**logout_redirect_uri** | **str** | The logout redirect URI for the client | [optional] 

## Example

```python
from docspace.models.create_client_request import CreateClientRequest

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


