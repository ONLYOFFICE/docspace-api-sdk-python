# AiConfigDto
The AI settings the editor opens with. They follow the portal-wide AI access setting for signed-in users; an  anonymous visitor who opened the document through an external link always gets AI disabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Whether the editor hides its AI tools. It is set when AI is turned off for the portal, and always for an  anonymous visitor of an external link. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_config_dto import AiConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiConfigDto from a JSON string
ai_config_dto_instance = AiConfigDto.from_json(json)
# print the JSON string representation of the object
print(AiConfigDto.to_json())

# convert the object into a dict
ai_config_dto_dict = ai_config_dto_instance.to_dict()
# create an instance of AiConfigDto from a dict
ai_config_dto_from_dict = AiConfigDto.from_dict(ai_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


