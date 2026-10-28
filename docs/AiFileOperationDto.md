# AiFileOperationDto
One background file operation of the caller, as it stood when the answer was built.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the operation, the one to pass to `PUT api/2.0/files/fileops/terminate/{id}` to stop it.  Operations belong to the account that started them, so an identifier of somebody else is never listed here. | 
**operation** | [**AiFileOperationType**](AiFileOperationType.md) | What the operation does with the entries, which also decides what else is reported: only a download fills  `url`, and a deletion leaves `files` and `folders` empty. | 
**progress** | **int** | How far the operation has come, from 0 to 100. Reaching 100 only means it stopped; whether it did what it was  asked for is told by `error`. | 
**error** | **str** | The reason the operation could not finish its work, in the language of the request. Empty when nothing went  wrong, which is the only way to tell a successful operation from a failed one. | 
**processed** | **str** | How many entries the operation has handled so far, written as a decimal number in a string. It counts items,  not percent, and stays behind `progress` on operations that walk into subfolders. | 
**finished** | **bool** | Whether the operation has stopped running. A finished operation is reported once and then dropped, so the next  read of the operation list no longer contains it. | 
**url** | **str** | The address the packed archive can be downloaded from once a bulk download has finished. Empty for every other  kind of operation. | [optional] 
**files** | [**List[AiFileEntryBaseDto]**](AiFileEntryBaseDto.md) | The files the operation produced or moved, in the order it wrote them down. Empty while nothing has been  written yet and for a deletion, which reports no entries at all. | [optional] 
**folders** | [**List[AiFileEntryBaseDto]**](AiFileEntryBaseDto.md) | The folders the operation produced or moved, in the order it wrote them down. Empty while nothing has been  written yet and for a deletion. | [optional] 
**status** | [**AiDistributedTaskStatus**](AiDistributedTaskStatus.md) | The state of the background task behind the operation, which tells a task that was cancelled or that crashed  from one that ran to its end. | [optional] 

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


