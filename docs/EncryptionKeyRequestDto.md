# EncryptionKeyRequestDto
The two halves of an encryption key pair to store for the calling user, plus the identifier the pair is kept  under.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Names the pair inside the caller's own key set. The client generates it, and leaving it out means the all-zero  GUID, which is the pair a client that never sends an identifier keeps working with. | [optional] 
**public_key** | **str** | The public half of the pair, as the client's crypto engine produced it and stored verbatim. This is the half  handed to the other members of a private room so that they can encrypt file keys for this user. | [optional] 
**private_key_enc** | **str** | The private half of the pair, encrypted on the client with the user's password before it is sent. The portal  stores it as opaque text and cannot decrypt it, so material lost on the client cannot be recovered from here. | [optional] 

## Example

```python
from docspace_api_sdk.models.encryption_key_request_dto import EncryptionKeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeyRequestDto from a JSON string
encryption_key_request_dto_instance = EncryptionKeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(EncryptionKeyRequestDto.to_json())

# convert the object into a dict
encryption_key_request_dto_dict = encryption_key_request_dto_instance.to_dict()
# create an instance of EncryptionKeyRequestDto from a dict
encryption_key_request_dto_from_dict = EncryptionKeyRequestDto.from_dict(encryption_key_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


