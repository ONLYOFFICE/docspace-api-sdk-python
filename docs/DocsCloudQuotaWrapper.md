# DocsCloudQuotaWrapper
The successful API response containing the DocsCloudQuota object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DocsCloudQuota**](DocsCloudQuota.md) | The DocsCloudQuota object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_quota_wrapper import DocsCloudQuotaWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudQuotaWrapper from a JSON string
docs_cloud_quota_wrapper_instance = DocsCloudQuotaWrapper.from_json(json)
# print the JSON string representation of the object
print(DocsCloudQuotaWrapper.to_json())

# convert the object into a dict
docs_cloud_quota_wrapper_dict = docs_cloud_quota_wrapper_instance.to_dict()
# create an instance of DocsCloudQuotaWrapper from a dict
docs_cloud_quota_wrapper_from_dict = DocsCloudQuotaWrapper.from_dict(docs_cloud_quota_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


