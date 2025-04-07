# DocumentBuilderTaskDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id | [optional] 
**error** | **str** | Error | [optional] 
**percentage** | **int** | Percentage | [optional] 
**is_completed** | **bool** | Is completed | [optional] 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) |  | [optional] 
**result_file_id** | **object** | Result file id | [optional] 
**result_file_name** | **str** | Result file name | [optional] 
**result_file_url** | **str** | Result file url | [optional] 

## Example

```python
from docspace.models.document_builder_task_dto import DocumentBuilderTaskDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBuilderTaskDto from a JSON string
document_builder_task_dto_instance = DocumentBuilderTaskDto.from_json(json)
# print the JSON string representation of the object
print(DocumentBuilderTaskDto.to_json())

# convert the object into a dict
document_builder_task_dto_dict = document_builder_task_dto_instance.to_dict()
# create an instance of DocumentBuilderTaskDto from a dict
document_builder_task_dto_from_dict = DocumentBuilderTaskDto.from_dict(document_builder_task_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


