# ChangeEmailRequest
The request parameters for updating a user email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The new address in plain text, up to 255 characters. It is stored in lowercase, and one of this field and  `encEmail` is required. | [optional] 
**enc_email** | **str** | The new address in the encrypted form the confirmation link carries. Pass the value from the link unchanged;  it is used only when `email` is empty. | [optional] 

## Example

```python
from docspace_api_sdk.models.change_email_request import ChangeEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeEmailRequest from a JSON string
change_email_request_instance = ChangeEmailRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeEmailRequest.to_json())

# convert the object into a dict
change_email_request_dict = change_email_request_instance.to_dict()
# create an instance of ChangeEmailRequest from a dict
change_email_request_from_dict = ChangeEmailRequest.from_dict(change_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


