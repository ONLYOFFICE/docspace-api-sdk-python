# DocsCloudQuota
Represents the current user quota of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[DocsCloudQuotaUser]**](DocsCloudQuotaUser.md) | The editor users. | [optional] 
**users_view** | [**List[DocsCloudQuotaUser]**](DocsCloudQuotaUser.md) | The viewer users. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_quota import DocsCloudQuota

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudQuota from a JSON string
docs_cloud_quota_instance = DocsCloudQuota.from_json(json)
# print the JSON string representation of the object
print(DocsCloudQuota.to_json())

# convert the object into a dict
docs_cloud_quota_dict = docs_cloud_quota_instance.to_dict()
# create an instance of DocsCloudQuota from a dict
docs_cloud_quota_from_dict = DocsCloudQuota.from_dict(docs_cloud_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


