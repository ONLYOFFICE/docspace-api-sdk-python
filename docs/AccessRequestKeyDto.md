# AccessRequestKeyDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | User ID | [optional] 
**public_key_id** | **UUID** | Public key ID | [optional] 
**private_key_enc** | **str** | Encrypted private key | [optional] 

## Example

```python
from docspace_api_sdk.models.access_request_key_dto import AccessRequestKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestKeyDto from a JSON string
access_request_key_dto_instance = AccessRequestKeyDto.from_json(json)
# print the JSON string representation of the object
print(AccessRequestKeyDto.to_json())

# convert the object into a dict
access_request_key_dto_dict = access_request_key_dto_instance.to_dict()
# create an instance of AccessRequestKeyDto from a dict
access_request_key_dto_from_dict = AccessRequestKeyDto.from_dict(access_request_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


