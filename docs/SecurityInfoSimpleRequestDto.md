# SecurityInfoSimpleRequestDto
The parameters of the security information request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share** | [**List[FileShareParams]**](FileShareParams.md) | The collection of sharing parameters. | [optional] 
**notify** | **bool** | Specifies whether to notify users about the shared file or not. | [optional] 
**sharing_message** | **str** | The message to send when notifying about the shared file. | [optional] 

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


