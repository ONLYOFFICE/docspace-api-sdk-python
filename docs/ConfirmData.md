# ConfirmData
The confirmation link a sign-in is authorised with, in place of a password.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The address the confirmation link was issued for. It has to be the same address the key was signed with, and  a value that is not an email address fails the request with 400. | [optional] 
**first** | **bool** | Whether the link is being followed for the first time, taken from the `first` parameter of the confirmation  URL. It is part of what the key was signed over, so passing a different value invalidates the key rather than  changing behaviour. | [optional] 
**key** | **str** | The `key` parameter of the confirmation URL, copied verbatim. It is bound to the address and to the moment it  was issued, so it stops being accepted once the portal email key lifetime has passed. | [optional] 

## Example

```python
from docspace_api_sdk.models.confirm_data import ConfirmData

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


