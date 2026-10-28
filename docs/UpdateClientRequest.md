# UpdateClientRequest
Client update request containing modified client details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name shown to the user on the consent screen. It has to be between 3 and 256 characters long. | 
**description** | **str** | The free-text description shown next to the name on the consent screen, at most 255 characters. | [optional] 
**logo** | **str** | The client logo as a data URI carrying base64 image data, shown on the consent screen. Only png, jpeg, jpg and svg+xml are accepted. | 
**scopes** | **List[str]** | The permissions the client may ask for, named as they appear in the tenant scope catalogue - for example files:read, rooms:write or openid. A client cannot request a scope that is not listed here. | 
**allow_pkce** | **bool** | Whether the client may use PKCE. Turning it on lets the client authenticate with the none method and prove itself with a code verifier instead of sending a secret, which is what a client that cannot keep a secret needs. | [optional] 
**allowed_origins** | **List[str]** | The web origins allowed to call the portal on behalf of this client, used for the CORS check. The set holds between 1 and 12 addresses. | 
**redirect_uris** | **List[str]** | The URIs an authorization code may be delivered to. An authorization request naming any other URI is refused, and the set holds between 1 and 12 addresses. | 
**is_public** | **bool** | Whether the client is offered to third-party tenants rather than only to the tenant that registers it. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_client_request import UpdateClientRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientRequest from a JSON string
update_client_request_instance = UpdateClientRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateClientRequest.to_json())

# convert the object into a dict
update_client_request_dict = update_client_request_instance.to_dict()
# create an instance of UpdateClientRequest from a dict
update_client_request_from_dict = UpdateClientRequest.from_dict(update_client_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


