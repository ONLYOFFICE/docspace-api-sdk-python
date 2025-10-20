# SecurityInfoRequestDto
The security information request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_ids** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The list of the shared folder IDs. | [optional] 
**file_ids** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The list of the shared file IDs. | [optional] 
**share** | [**List[FileShareParams]**](FileShareParams.md) | The collection of sharing parameters. | [optional] 
**notify** | **bool** | Specifies whether to notify users about the shared file or not. | [optional] 
**sharing_message** | **str** | The message to send when notifying about the shared file. | [optional] 

## Example

```python
from docspace_api_sdk.models.security_info_request_dto import SecurityInfoRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityInfoRequestDto from a JSON string
security_info_request_dto_instance = SecurityInfoRequestDto.from_json(json)
# print the JSON string representation of the object
print(SecurityInfoRequestDto.to_json())

# convert the object into a dict
security_info_request_dto_dict = security_info_request_dto_instance.to_dict()
# create an instance of SecurityInfoRequestDto from a dict
security_info_request_dto_from_dict = SecurityInfoRequestDto.from_dict(security_info_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


