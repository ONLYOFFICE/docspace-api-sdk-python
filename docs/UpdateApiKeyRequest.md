# UpdateApiKeyRequest
The request parameters for updating an existing API key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new label of the key, up to 30 characters. Omit it to keep the current name. | [optional] 
**permissions** | **List[str]** | The scopes that replace the current ones. Every value has to come from `GET api/2.0/keys/permissions`, an  unknown value or an empty array is rejected, and omitting the field keeps the current scopes. | [optional] 
**is_active** | **bool** | Whether the key may authenticate requests. Set it to false to stop the key without deleting it and to true to  let it work again; omit it to keep the current state. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_api_key_request import UpdateApiKeyRequest

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


