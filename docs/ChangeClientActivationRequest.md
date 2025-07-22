# ChangeClientActivationRequest
The request parameters for changing the client activation status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | The client activation status. | 

## Example

```python
from docspace-api-sdk.models.change_client_activation_request import ChangeClientActivationRequest

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


