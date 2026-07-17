# SetEmbeddingConfigRequestBody
Parameters for configuring the embedding provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EmbeddingProviderType**](EmbeddingProviderType.md) |  | [optional] 
**key** | **str** | The API key for the selected embedding provider. Pass null to keep the existing key unchanged. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_embedding_config_request_body import SetEmbeddingConfigRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetEmbeddingConfigRequestBody from a JSON string
set_embedding_config_request_body_instance = SetEmbeddingConfigRequestBody.from_json(json)
# print the JSON string representation of the object
print(SetEmbeddingConfigRequestBody.to_json())

# convert the object into a dict
set_embedding_config_request_body_dict = set_embedding_config_request_body_instance.to_dict()
# create an instance of SetEmbeddingConfigRequestBody from a dict
set_embedding_config_request_body_from_dict = SetEmbeddingConfigRequestBody.from_dict(set_embedding_config_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


