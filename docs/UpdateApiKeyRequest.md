# UpdateApiKeyRequest
The request parameters for updating an existing API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the API key. | [optional] 
**permissions** | **List[str]** | The new list of permissions for the API key. | [optional] 
**is_active** | **bool** | Indicates whether the API key should be active or not. | [optional] 

## Example

```python
from docspace-api-python.models.update_api_key_request import UpdateApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApiKeyRequest from a JSON string
update_api_key_request_instance = UpdateApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateApiKeyRequest.to_json())

# convert the object into a dict
update_api_key_request_dict = update_api_key_request_instance.to_dict()
# create an instance of UpdateApiKeyRequest from a dict
update_api_key_request_from_dict = UpdateApiKeyRequest.from_dict(update_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


