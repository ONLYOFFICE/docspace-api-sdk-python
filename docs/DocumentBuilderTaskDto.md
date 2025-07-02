# DocumentBuilderTaskDto
The document builder task parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The document builder ID. | [optional] 
**error** | **str** | The error message occured while the document building process. | [optional] 
**percentage** | **int** | The percentage of the progress of the document building process. | [optional] 
**is_completed** | **bool** | Specifies whether the document building process is completed or not. | [optional] 
**status** | [**DistributedTaskStatus**](DistributedTaskStatus.md) |  | [optional] 
**result_file_id** | **object** | The result file ID. | [optional] 
**result_file_name** | **str** | The result file name. | [optional] 
**result_file_url** | **str** | The result file URL. | [optional] 

## Example

```python
from docspace-api-python.models.document_builder_task_dto import DocumentBuilderTaskDto

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


