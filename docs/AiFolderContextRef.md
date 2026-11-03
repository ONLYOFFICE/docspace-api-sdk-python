# AiFolderContextRef
A folder connected as the round's context - any folder of the portal, not only a room - named by its account and ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud** | **str** | The account the folder belongs to; `docspace` for a folder of this portal. | 
**id** | **str** | The folder ID. | 

## Example

```python
from docspace_api_sdk.models.ai_folder_context_ref import AiFolderContextRef

# TODO update the JSON string below
json = "{}"
# create an instance of AiFolderContextRef from a JSON string
ai_folder_context_ref_instance = AiFolderContextRef.from_json(json)
# print the JSON string representation of the object
print(AiFolderContextRef.to_json())

# convert the object into a dict
ai_folder_context_ref_dict = ai_folder_context_ref_instance.to_dict()
# create an instance of AiFolderContextRef from a dict
ai_folder_context_ref_from_dict = AiFolderContextRef.from_dict(ai_folder_context_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


