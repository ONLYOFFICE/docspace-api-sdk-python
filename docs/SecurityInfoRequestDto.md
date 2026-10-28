# SecurityInfoRequestDto
The entries whose sharing rights are being changed, and the rights to apply to them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_ids** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The folders and rooms whose rights are being changed, identified as a listing operation returns them - a  number on the portal, a string on a connected third-party account. | [optional] 
**file_ids** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The files whose rights are being changed, identified as a listing operation returns them - a number on the  portal, a string on a connected third-party account. | [optional] 
**share** | [**List[FileShareParams]**](FileShareParams.md) | One record per account or group whose rights are being set, each naming the subject and the level it gets on  all of the listed entries; a level of `None` takes the access away. An empty collection makes the call change  nothing. | [optional] 
**notify** | **bool** | Set to true to have every account named in `share` emailed about the access it just received; false changes  the rights without telling anyone. | [optional] 
**sharing_message** | **str** | The text put into that email, ignored while `notify` is false. Markup is stripped before sending, so only the  plain text of the value survives. | [optional] 

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


