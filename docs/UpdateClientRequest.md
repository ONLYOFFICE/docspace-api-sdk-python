# UpdateClientRequest

Client update request containing modified client details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the client | [optional] 
**description** | **str** | The description of the client | [optional] 
**logo** | **str** | The logo of the client in base64 format | [optional] 
**allow_pkce** | **bool** | Indicates whether PKCE is allowed for the client | [optional] 
**is_public** | **bool** | Indicates whether client is accessible by third-party tenants | [optional] 
**allowed_origins** | **List[str]** | The allowed origins for the client | [optional] 

## Example

```python
from docspace.models.update_client_request import UpdateClientRequest

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


