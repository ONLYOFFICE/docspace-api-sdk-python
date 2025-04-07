# ConfirmData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address | [optional] 
**first** | **bool** | Access an account for the first time or not | [optional] 
**key** | **str** | Key | [optional] 

## Example

```python
from docspace.models.confirm_data import ConfirmData

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmData from a JSON string
confirm_data_instance = ConfirmData.from_json(json)
# print the JSON string representation of the object
print(ConfirmData.to_json())

# convert the object into a dict
confirm_data_dict = confirm_data_instance.to_dict()
# create an instance of ConfirmData from a dict
confirm_data_from_dict = ConfirmData.from_dict(confirm_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


