# DocsCloudQuotaDto
Represents the current user quota of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[DocsCloudQuotaUserDto]**](DocsCloudQuotaUserDto.md) | The editor users. | [optional] 
**users_view** | [**List[DocsCloudQuotaUserDto]**](DocsCloudQuotaUserDto.md) | The viewer users. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_quota_dto import DocsCloudQuotaDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudQuotaDto from a JSON string
docs_cloud_quota_dto_instance = DocsCloudQuotaDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudQuotaDto.to_json())

# convert the object into a dict
docs_cloud_quota_dto_dict = docs_cloud_quota_dto_instance.to_dict()
# create an instance of DocsCloudQuotaDto from a dict
docs_cloud_quota_dto_from_dict = DocsCloudQuotaDto.from_dict(docs_cloud_quota_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


