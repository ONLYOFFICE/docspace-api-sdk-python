# AiContextFolder
The rooms of one account the caller can connect as context, grouped under the account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud** | **str** | The account the rooms belong to; `docspace` for this portal. | 
**rooms** | [**List[AiContextRoom]**](AiContextRoom.md) | The rooms of that account the caller can connect. | 

## Example

```python
from docspace_api_sdk.models.ai_context_folder import AiContextFolder

# TODO update the JSON string below
json = "{}"
# create an instance of AiContextFolder from a JSON string
ai_context_folder_instance = AiContextFolder.from_json(json)
# print the JSON string representation of the object
print(AiContextFolder.to_json())

# convert the object into a dict
ai_context_folder_dict = ai_context_folder_instance.to_dict()
# create an instance of AiContextFolder from a dict
ai_context_folder_from_dict = AiContextFolder.from_dict(ai_context_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


