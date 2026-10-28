# ChangeClientActivationRequest
Client activation change request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Whether the client may obtain tokens from now on. Sending false leaves the registration and the already issued tokens in place but refuses new authorization requests; sending true allows them again. | 

## Example

```python
from docspace_api_sdk.models.change_client_activation_request import ChangeClientActivationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeClientActivationRequest from a JSON string
change_client_activation_request_instance = ChangeClientActivationRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeClientActivationRequest.to_json())

# convert the object into a dict
change_client_activation_request_dict = change_client_activation_request_instance.to_dict()
# create an instance of ChangeClientActivationRequest from a dict
change_client_activation_request_from_dict = ChangeClientActivationRequest.from_dict(change_client_activation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


