# ClientInfoResponse
The consent-facing subset of a client: everything needed to render a consent screen, and nothing that would let a caller act as the client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name shown to the user on the consent screen, between 3 and 256 characters. | [optional] 
**description** | **str** | The free-text description shown next to the name on the consent screen, at most 255 characters. | [optional] 
**scopes** | **List[str]** | The permissions the client may ask for, named as they appear in the tenant scope catalogue - for example files:read, rooms:write or openid. A client cannot request a scope that is not listed here. | [optional] 
**client_id** | **str** | The generated identifier of the client, sent as client_id in every OAuth2 request. It is assigned when the client is registered and never changes afterwards. | [optional] 
**website_url** | **str** | The URL of the client home page, offered to the user before they consent. | [optional] 
**terms_url** | **str** | The URL of the client terms of service, linked from the consent screen. | [optional] 
**policy_url** | **str** | The URL of the client privacy policy, linked from the consent screen. | [optional] 
**logo** | **str** | The client logo as a data URI carrying base64 image data, shown on the consent screen. Only png, jpeg, jpg and svg+xml are accepted, the whole string may not exceed 2000000 characters and the decoded image may not exceed 256000 bytes. | [optional] 
**authentication_methods** | **List[str]** | How the client authenticates itself at the token endpoint: client_secret_post for a confidential client that sends its secret, none for a public client that proves itself with PKCE instead. | [optional] 
**created_on** | **datetime** | When the client was registered, as an ISO-8601 timestamp with a zone offset. | [optional] 
**created_by** | **str** | The identifier of the user who registered the client. A plain user may read and change only the clients where this is their own identifier. | [optional] 
**modified_on** | **datetime** | When the client was last changed, as an ISO-8601 timestamp with a zone offset. | [optional] 
**modified_by** | **str** | The identifier of the user who last changed the client. | [optional] 
**is_public** | **bool** | Whether the client is offered to third-party tenants rather than only to the tenant that registered it. | [optional] 

## Example

```python
from docspace_api_sdk.models.client_info_response import ClientInfoResponse

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


