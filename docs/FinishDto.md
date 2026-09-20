# FinishDto
Whether the finished import mails the imported people their activation links before it is cleared away.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_send_welcome_email** | **bool** | Whether every imported account that has not been activated yet is mailed its activation link. Setting it  requires the finished job to still be in the queue, so the import must not have been cleared first; the  letters go out again on each call, and already active accounts are skipped either way. Setting it false ends  the import quietly and leaves inviting those people for later. | 

## Example

```python
from docspace_api_sdk.models.finish_dto import FinishDto

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


