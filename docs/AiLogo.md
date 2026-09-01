# AiLogo
The room logo information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** | The original logo. | 
**large** | **str** | The large logo. | 
**medium** | **str** | The medium logo. | 
**small** | **str** | The small logo. | 
**color** | **str** | The logo color. | [optional] 
**cover** | [**AiLogoCover**](AiLogoCover.md) | The logo cover. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_logo import AiLogo

# TODO update the JSON string below
json = "{}"
# create an instance of AiLogo from a JSON string
ai_logo_instance = AiLogo.from_json(json)
# print the JSON string representation of the object
print(AiLogo.to_json())

# convert the object into a dict
ai_logo_dict = ai_logo_instance.to_dict()
# create an instance of AiLogo from a dict
ai_logo_from_dict = AiLogo.from_dict(ai_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


