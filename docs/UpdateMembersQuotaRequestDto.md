# UpdateMembersQuotaRequestDto
The request parameters for updating a user quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | The list of user IDs. | [optional] 
**quota** | [**UpdateMembersQuotaRequestDtoQuota**](UpdateMembersQuotaRequestDtoQuota.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.update_members_quota_request_dto import UpdateMembersQuotaRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembersQuotaRequestDto from a JSON string
update_members_quota_request_dto_instance = UpdateMembersQuotaRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateMembersQuotaRequestDto.to_json())

# convert the object into a dict
update_members_quota_request_dto_dict = update_members_quota_request_dto_instance.to_dict()
# create an instance of UpdateMembersQuotaRequestDto from a dict
update_members_quota_request_dto_from_dict = UpdateMembersQuotaRequestDto.from_dict(update_members_quota_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


