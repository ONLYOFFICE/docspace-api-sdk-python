# AiLogoCover
The logo cover information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The logo cover ID. | 
**data** | **str** | The logo cover data. | 

## Example

```python
from docspace_api_sdk.models.ai_logo_cover import AiLogoCover

# TODO update the JSON string below
json = "{}"
# create an instance of AiLogoCover from a JSON string
ai_logo_cover_instance = AiLogoCover.from_json(json)
# print the JSON string representation of the object
print(AiLogoCover.to_json())

# convert the object into a dict
ai_logo_cover_dict = ai_logo_cover_instance.to_dict()
# create an instance of AiLogoCover from a dict
ai_logo_cover_from_dict = AiLogoCover.from_dict(ai_logo_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


