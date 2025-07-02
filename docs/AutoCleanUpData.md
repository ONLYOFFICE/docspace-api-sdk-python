# AutoCleanUpData
The auto-clearing setting parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_auto_clean_up** | **bool** | Specifies whether to permanently delete files in the Trash folder. | [optional] 
**gap** | [**DateToAutoCleanUp**](DateToAutoCleanUp.md) |  | [optional] 

## Example

```python
from docspace-api-python.models.auto_clean_up_data import AutoCleanUpData

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


