# ConfirmData

The additional confirmation data required for authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address to confirm the user&#39;s identity. | [optional] 
**first** | **bool** | Specifies whether this is the first access to the user&#39;s account. | [optional] 
**key** | **str** | The unique confirmation key for validating user identity. | [optional] 

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


