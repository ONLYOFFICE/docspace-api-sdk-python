# SecurityInfoSimpleRequestDto
The rights to apply to a single file or folder, and how to announce them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share** | [**List[FileShareParams]**](FileShareParams.md) | One record per account or group whose rights are being set, each naming the subject and the level it gets; a  level of `None` takes the access away. An empty collection makes the call change nothing. | [optional] 
**notify** | **bool** | Set to true to have every account named in `share` emailed about the access it just received; false changes  the rights without telling anyone. | [optional] 
**sharing_message** | **str** | The text put into that email, ignored while `notify` is false. Markup is stripped before sending, so only the  plain text of the value survives. | [optional] 

## Example

```python
from docspace_api_sdk.models.security_info_simple_request_dto import SecurityInfoSimpleRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityInfoSimpleRequestDto from a JSON string
security_info_simple_request_dto_instance = SecurityInfoSimpleRequestDto.from_json(json)
# print the JSON string representation of the object
print(SecurityInfoSimpleRequestDto.to_json())

# convert the object into a dict
security_info_simple_request_dto_dict = security_info_simple_request_dto_instance.to_dict()
# create an instance of SecurityInfoSimpleRequestDto from a dict
security_info_simple_request_dto_from_dict = SecurityInfoSimpleRequestDto.from_dict(security_info_simple_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


