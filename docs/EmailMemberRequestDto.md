# EmailMemberRequestDto
The request parameters for the user email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user email address. | 

## Example

```python
from docspace-api-python.models.email_member_request_dto import EmailMemberRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmailMemberRequestDto from a JSON string
email_member_request_dto_instance = EmailMemberRequestDto.from_json(json)
# print the JSON string representation of the object
print(EmailMemberRequestDto.to_json())

# convert the object into a dict
email_member_request_dto_dict = email_member_request_dto_instance.to_dict()
# create an instance of EmailMemberRequestDto from a dict
email_member_request_dto_from_dict = EmailMemberRequestDto.from_dict(email_member_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


