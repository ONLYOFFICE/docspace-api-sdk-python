# AiFileOperationDto
The file operation information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The file operation ID. | 
**operation** | [**AiFileOperationType**](AiFileOperationType.md) | The file operation type. | 
**progress** | **int** | The file operation progress in percentage. | 
**error** | **str** | The file operation error message. | 
**processed** | **str** | The file operation processing status. | 
**finished** | **bool** | Specifies if the file operation is finished or not. | 
**url** | **str** | The file operation URL. | [optional] 
**files** | [**List[AiFileEntryBaseDto]**](AiFileEntryBaseDto.md) | The list of files of the file operation. | [optional] 
**folders** | [**List[AiFileEntryBaseDto]**](AiFileEntryBaseDto.md) | The list of folders of the file operation. | [optional] 
**status** | [**AiDistributedTaskStatus**](AiDistributedTaskStatus.md) | The status of the distributed task related to the file operation. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_file_operation_dto import AiFileOperationDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiFileOperationDto from a JSON string
ai_file_operation_dto_instance = AiFileOperationDto.from_json(json)
# print the JSON string representation of the object
print(AiFileOperationDto.to_json())

# convert the object into a dict
ai_file_operation_dto_dict = ai_file_operation_dto_instance.to_dict()
# create an instance of AiFileOperationDto from a dict
ai_file_operation_dto_from_dict = AiFileOperationDto.from_dict(ai_file_operation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


