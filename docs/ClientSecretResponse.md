# ClientSecretResponse
The response containing the regenerated client secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** | The newly generated client secret. | [optional] 

## Example

```python
from docspace_api_sdk.models.client_secret_response import ClientSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSecretResponse from a JSON string
client_secret_response_instance = ClientSecretResponse.from_json(json)
# print the JSON string representation of the object
print(ClientSecretResponse.to_json())

# convert the object into a dict
client_secret_response_dict = client_secret_response_instance.to_dict()
# create an instance of ClientSecretResponse from a dict
client_secret_response_from_dict = ClientSecretResponse.from_dict(client_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


