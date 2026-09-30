# IAccountEntryArrayWrapper
The successful API response containing the list of IAccountEntryDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[IAccountEntryDto]**](IAccountEntryDto.md) | The list of IAccountEntryDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.i_account_entry_array_wrapper import IAccountEntryArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of IAccountEntryArrayWrapper from a JSON string
i_account_entry_array_wrapper_instance = IAccountEntryArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(IAccountEntryArrayWrapper.to_json())

# convert the object into a dict
i_account_entry_array_wrapper_dict = i_account_entry_array_wrapper_instance.to_dict()
# create an instance of IAccountEntryArrayWrapper from a dict
i_account_entry_array_wrapper_from_dict = IAccountEntryArrayWrapper.from_dict(i_account_entry_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


