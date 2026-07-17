# DocumentBuilderTaskWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DocumentBuilderTaskDto**](DocumentBuilderTaskDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper

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


