# ClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant** | **int** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**terms_url** | **str** |  | [optional] 
**policy_url** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**authentication_methods** | **List[str]** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 
**allowed_origins** | **List[str]** |  | [optional] 
**logout_redirect_uris** | **List[str]** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_on** | **datetime** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 

## Example

```python
from docspace.models.client_response import ClientResponse

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


