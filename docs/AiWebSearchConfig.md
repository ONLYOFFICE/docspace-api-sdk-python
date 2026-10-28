# AiWebSearchConfig
Web-search provider configuration. Credentials and provider selection for the built-in web-search tool group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Provider identifier (e.g. `exa`). | 
**key** | **str** | API key for the provider. Optional for self-hosted or keyless setups. | [optional] 
**base_url** | **str** | Optional override for the provider's base URL. | [optional] 
**is_cloud_provider** | **bool** | Whether this provider is cloud-hosted (vs. self-hosted). | [optional] 
**headers** | **Dict[str, str]** | Extra HTTP headers sent with each request to the ONLYOFFICE / cloud backend (e.g. `X-Tenant`). Merged after the derived `Authorization` header, so a custom header of the same name wins. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_web_search_config import AiWebSearchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AiWebSearchConfig from a JSON string
ai_web_search_config_instance = AiWebSearchConfig.from_json(json)
# print the JSON string representation of the object
print(AiWebSearchConfig.to_json())

# convert the object into a dict
ai_web_search_config_dict = ai_web_search_config_instance.to_dict()
# create an instance of AiWebSearchConfig from a dict
ai_web_search_config_from_dict = AiWebSearchConfig.from_dict(ai_web_search_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


