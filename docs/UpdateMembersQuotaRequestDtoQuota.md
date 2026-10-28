# UpdateMembersQuotaRequestDtoQuota
The personal storage limit in bytes, as a whole number. A value of 0 or more becomes the limit, and any  negative value switches the personal limit off so that the portal default applies again. It is read only by  `PUT api/2.0/people/userquota`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.update_members_quota_request_dto_quota import UpdateMembersQuotaRequestDtoQuota

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembersQuotaRequestDtoQuota from a JSON string
update_members_quota_request_dto_quota_instance = UpdateMembersQuotaRequestDtoQuota.from_json(json)
# print the JSON string representation of the object
print(UpdateMembersQuotaRequestDtoQuota.to_json())

# convert the object into a dict
update_members_quota_request_dto_quota_dict = update_members_quota_request_dto_quota_instance.to_dict()
# create an instance of UpdateMembersQuotaRequestDtoQuota from a dict
update_members_quota_request_dto_quota_from_dict = UpdateMembersQuotaRequestDtoQuota.from_dict(update_members_quota_request_dto_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


