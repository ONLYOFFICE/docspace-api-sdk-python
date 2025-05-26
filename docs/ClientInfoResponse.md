# ClientInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**client_id** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**terms_url** | **str** |  | [optional] 
**policy_url** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**authentication_methods** | **List[str]** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**modified_on** | **datetime** |  | [optional] 
**modified_by** | **str** |  | [optional] 

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


