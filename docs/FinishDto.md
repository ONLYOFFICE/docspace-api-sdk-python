# FinishDto
The parameters for terminating a process or operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_send_welcome_email** | **bool** | Specifies whether to send a welcome email or not. | [optional] 

## Example

```python
from docspace-api-sdk.models.finish_dto import FinishDto

# TODO update the JSON string below
json = "{}"
# create an instance of FinishDto from a JSON string
finish_dto_instance = FinishDto.from_json(json)
# print the JSON string representation of the object
print(FinishDto.to_json())

# convert the object into a dict
finish_dto_dict = finish_dto_instance.to_dict()
# create an instance of FinishDto from a dict
finish_dto_from_dict = FinishDto.from_dict(finish_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


