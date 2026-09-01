# DocsCloudQuotaUser
Represents a single user entry of a DocsCloud quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user ID. | [optional] 
**expire** | **str** | The expiration date of the user. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_quota_user import DocsCloudQuotaUser

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudQuotaUser from a JSON string
docs_cloud_quota_user_instance = DocsCloudQuotaUser.from_json(json)
# print the JSON string representation of the object
print(DocsCloudQuotaUser.to_json())

# convert the object into a dict
docs_cloud_quota_user_dict = docs_cloud_quota_user_instance.to_dict()
# create an instance of DocsCloudQuotaUser from a dict
docs_cloud_quota_user_from_dict = DocsCloudQuotaUser.from_dict(docs_cloud_quota_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


