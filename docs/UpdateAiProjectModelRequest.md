# UpdateAiProjectModelRequest
The AI model to set for the AI project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **UUID** | ID of the AI model profile that answers in the project's chat; take it from the `id` of a profile that `GET api/2.0/ai/profiles/list` returns. | 

## Example

```python
from docspace_api_sdk.models.update_ai_project_model_request import UpdateAiProjectModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAiProjectModelRequest from a JSON string
update_ai_project_model_request_instance = UpdateAiProjectModelRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAiProjectModelRequest.to_json())

# convert the object into a dict
update_ai_project_model_request_dict = update_ai_project_model_request_instance.to_dict()
# create an instance of UpdateAiProjectModelRequest from a dict
update_ai_project_model_request_from_dict = UpdateAiProjectModelRequest.from_dict(update_ai_project_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


