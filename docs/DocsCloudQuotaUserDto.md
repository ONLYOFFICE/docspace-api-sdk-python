# DocsCloudQuotaUserDto
Represents a single user entry of a Docs Connect quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user ID. | [optional] 
**expire** | **str** | The expiration date of the user. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_quota_user_dto import DocsCloudQuotaUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudQuotaUserDto from a JSON string
docs_cloud_quota_user_dto_instance = DocsCloudQuotaUserDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudQuotaUserDto.to_json())

# convert the object into a dict
docs_cloud_quota_user_dto_dict = docs_cloud_quota_user_dto_instance.to_dict()
# create an instance of DocsCloudQuotaUserDto from a dict
docs_cloud_quota_user_dto_from_dict = DocsCloudQuotaUserDto.from_dict(docs_cloud_quota_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


