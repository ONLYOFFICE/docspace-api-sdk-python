# AiLogoDto
The room logo information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** | The original logo. | 
**large** | **str** | The large logo. | 
**medium** | **str** | The medium logo. | 
**small** | **str** | The small logo. | 
**color** | **str** | The logo color. | [optional] 
**cover** | [**AiLogoCoverDto**](AiLogoCoverDto.md) | The logo cover. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_logo_dto import AiLogoDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiLogoDto from a JSON string
ai_logo_dto_instance = AiLogoDto.from_json(json)
# print the JSON string representation of the object
print(AiLogoDto.to_json())

# convert the object into a dict
ai_logo_dto_dict = ai_logo_dto_instance.to_dict()
# create an instance of AiLogoDto from a dict
ai_logo_dto_from_dict = AiLogoDto.from_dict(ai_logo_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


