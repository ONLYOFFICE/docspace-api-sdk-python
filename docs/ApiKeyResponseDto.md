# ApiKeyResponseDto
The response data for the API key operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the key. This is the value to pass to `PUT api/2.0/keys/{keyId}` and  `DELETE api/2.0/keys/{keyId}`. | 
**name** | **str** | The label given to the key when it was created or last updated. | 
**key** | **str** | The secret to send in the `Authorization` header as `Bearer sk-...`. It is filled in only by the answer of  `POST api/2.0/keys` and cannot be read again afterwards, so it has to be stored at that moment. | 
**key_postfix** | **str** | The last four characters of the secret. It is the only part of the secret that later reads expose, and it is  meant for telling keys apart in a list. | [optional] 
**permissions** | **List[str]** | The scopes the key may use, as accepted by `GET api/2.0/keys/permissions`. An empty list means the key has no  scope restrictions. | 
**last_used** | [**ApiDateTime**](ApiDateTime.md) | The UTC moment the key was last used to authenticate a request. It is empty for a key that has never been  used. | [optional] 
**create_on** | [**ApiDateTime**](ApiDateTime.md) | The UTC moment the key was created. | [optional] 
**create_by** | [**EmployeeDto**](EmployeeDto.md) | The portal member who created the key, and whose access the key acts with. | [optional] 
**expires_at** | [**ApiDateTime**](ApiDateTime.md) | The UTC moment the key stops working. It is empty for a key created without `expiresInDays`, which never  expires. | [optional] 
**is_active** | **bool** | Whether the key may authenticate requests. A key deactivated through `PUT api/2.0/keys/{keyId}` stays in the  list with this field set to false. | 

## Example

```python
from docspace_api_sdk.models.api_key_response_dto import ApiKeyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyResponseDto from a JSON string
api_key_response_dto_instance = ApiKeyResponseDto.from_json(json)
# print the JSON string representation of the object
print(ApiKeyResponseDto.to_json())

# convert the object into a dict
api_key_response_dto_dict = api_key_response_dto_instance.to_dict()
# create an instance of ApiKeyResponseDto from a dict
api_key_response_dto_from_dict = ApiKeyResponseDto.from_dict(api_key_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


