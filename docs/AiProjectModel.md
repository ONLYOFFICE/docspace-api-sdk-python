# AiProjectModel
The project's own model; `null` when the project runs on the portal default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**AiProjectModelProfile**](AiProjectModelProfile.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_project_model import AiProjectModel

# TODO update the JSON string below
json = "{}"
# create an instance of AiProjectModel from a JSON string
ai_project_model_instance = AiProjectModel.from_json(json)
# print the JSON string representation of the object
print(AiProjectModel.to_json())

# convert the object into a dict
ai_project_model_dict = ai_project_model_instance.to_dict()
# create an instance of AiProjectModel from a dict
ai_project_model_from_dict = AiProjectModel.from_dict(ai_project_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


