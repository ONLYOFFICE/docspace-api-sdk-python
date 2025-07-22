# DocumentBuilderTaskWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DocumentBuilderTaskDto**](DocumentBuilderTaskDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBuilderTaskWrapper from a JSON string
document_builder_task_wrapper_instance = DocumentBuilderTaskWrapper.from_json(json)
# print the JSON string representation of the object
print(DocumentBuilderTaskWrapper.to_json())

# convert the object into a dict
document_builder_task_wrapper_dict = document_builder_task_wrapper_instance.to_dict()
# create an instance of DocumentBuilderTaskWrapper from a dict
document_builder_task_wrapper_from_dict = DocumentBuilderTaskWrapper.from_dict(document_builder_task_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


