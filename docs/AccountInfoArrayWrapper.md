# AccountInfoArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AccountInfoDto]**](AccountInfoDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.account_info_array_wrapper import AccountInfoArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoArrayWrapper from a JSON string
account_info_array_wrapper_instance = AccountInfoArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(AccountInfoArrayWrapper.to_json())

# convert the object into a dict
account_info_array_wrapper_dict = account_info_array_wrapper_instance.to_dict()
# create an instance of AccountInfoArrayWrapper from a dict
account_info_array_wrapper_from_dict = AccountInfoArrayWrapper.from_dict(account_info_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


