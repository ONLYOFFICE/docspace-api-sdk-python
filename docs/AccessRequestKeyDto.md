# AccessRequestKeyDto
The file key issued to one account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | The account that is to open the file with this key; it has to have read access to the file. | [optional] 
**public_key_id** | **UUID** | The public key the file key was encrypted with, as reported for that account by  `GET api/2.0/files/file/{fileId}/publickeys`. | [optional] 
**private_key_enc** | **str** | The key of the file itself, encrypted by the client with that public key, so that the plain key never reaches  the portal. | [optional] 

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


