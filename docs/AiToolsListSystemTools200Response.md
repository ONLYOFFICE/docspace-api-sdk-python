# AiToolsListSystemTools200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **Dict[str, List[AiTMCPItem]]** | Tools by server name, covering both the host-configured system servers and the custom MCP servers registered for this scope. | 
**errors** | **Dict[str, str]** | Why a registered custom server could not be reached, keyed by server name. A server that answered is absent from this map. | 
**system** | **List[str]** | Names of the host-configured system servers among the keys of `groups`; everything else there was registered as a custom server. | 

## Example

```python
from docspace_api_sdk.models.ai_tools_list_system_tools200_response import AiToolsListSystemTools200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsListSystemTools200Response from a JSON string
ai_tools_list_system_tools200_response_instance = AiToolsListSystemTools200Response.from_json(json)
# print the JSON string representation of the object
print(AiToolsListSystemTools200Response.to_json())

# convert the object into a dict
ai_tools_list_system_tools200_response_dict = ai_tools_list_system_tools200_response_instance.to_dict()
# create an instance of AiToolsListSystemTools200Response from a dict
ai_tools_list_system_tools200_response_from_dict = AiToolsListSystemTools200Response.from_dict(ai_tools_list_system_tools200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


