# AiWebSearchConfigureRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AiWebSearchConfig**](AiWebSearchConfig.md) |  | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_web_search_configure_request import AiWebSearchConfigureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiWebSearchConfigureRequest from a JSON string
ai_web_search_configure_request_instance = AiWebSearchConfigureRequest.from_json(json)
# print the JSON string representation of the object
print(AiWebSearchConfigureRequest.to_json())

# convert the object into a dict
ai_web_search_configure_request_dict = ai_web_search_configure_request_instance.to_dict()
# create an instance of AiWebSearchConfigureRequest from a dict
ai_web_search_configure_request_from_dict = AiWebSearchConfigureRequest.from_dict(ai_web_search_configure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


