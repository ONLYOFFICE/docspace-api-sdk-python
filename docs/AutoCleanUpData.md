# AutoCleanUpData
The trash auto-clearing setting of an account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auto_clean_up** | **bool** | Whether the trash of the account is cleared automatically. While it is false nothing is removed by the portal  and the interval below is kept but unused. | [optional] 
**gap** | [**DateToAutoCleanUp**](DateToAutoCleanUp.md) | How long an item may stay in the trash before it is removed for good. It is reported even while clearing is  off, and it is what the moment in the `autoDelete` field of a trashed entry is computed from. | [optional] 

## Example

```python
from docspace_api_sdk.models.auto_clean_up_data import AutoCleanUpData

# TODO update the JSON string below
json = "{}"
# create an instance of AutoCleanUpData from a JSON string
auto_clean_up_data_instance = AutoCleanUpData.from_json(json)
# print the JSON string representation of the object
print(AutoCleanUpData.to_json())

# convert the object into a dict
auto_clean_up_data_dict = auto_clean_up_data_instance.to_dict()
# create an instance of AutoCleanUpData from a dict
auto_clean_up_data_from_dict = AutoCleanUpData.from_dict(auto_clean_up_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


