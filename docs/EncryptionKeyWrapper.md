# EncryptionKeyWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**EncryptionKeyDto**](EncryptionKeyDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.encryption_key_wrapper import EncryptionKeyWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeyWrapper from a JSON string
encryption_key_wrapper_instance = EncryptionKeyWrapper.from_json(json)
# print the JSON string representation of the object
print(EncryptionKeyWrapper.to_json())

# convert the object into a dict
encryption_key_wrapper_dict = encryption_key_wrapper_instance.to_dict()
# create an instance of EncryptionKeyWrapper from a dict
encryption_key_wrapper_from_dict = EncryptionKeyWrapper.from_dict(encryption_key_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


