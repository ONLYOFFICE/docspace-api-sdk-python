# EncryptionKeyArrayWrapper
The successful API response containing the list of EncryptionKeyDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[EncryptionKeyDto]**](EncryptionKeyDto.md) | The list of EncryptionKeyDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.encryption_key_array_wrapper import EncryptionKeyArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeyArrayWrapper from a JSON string
encryption_key_array_wrapper_instance = EncryptionKeyArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(EncryptionKeyArrayWrapper.to_json())

# convert the object into a dict
encryption_key_array_wrapper_dict = encryption_key_array_wrapper_instance.to_dict()
# create an instance of EncryptionKeyArrayWrapper from a dict
encryption_key_array_wrapper_from_dict = EncryptionKeyArrayWrapper.from_dict(encryption_key_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


