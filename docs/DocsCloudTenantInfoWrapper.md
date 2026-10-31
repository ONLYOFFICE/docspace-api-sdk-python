# DocsCloudTenantInfoWrapper
The successful API response containing the DocsCloudTenantInfoDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DocsCloudTenantInfoDto**](DocsCloudTenantInfoDto.md) | The DocsCloudTenantInfoDto object returned by the operation. | [optional] 
**count** | **int** | How many items this response carries: the length of the page for a list, 1 for a single object | [optional] 
**total** | **int** | How many items the whole list holds across all pages, for working out how many pages to request. Sent only by the operations that page their results, and left out of every other response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_tenant_info_wrapper import DocsCloudTenantInfoWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudTenantInfoWrapper from a JSON string
docs_cloud_tenant_info_wrapper_instance = DocsCloudTenantInfoWrapper.from_json(json)
# print the JSON string representation of the object
print(DocsCloudTenantInfoWrapper.to_json())

# convert the object into a dict
docs_cloud_tenant_info_wrapper_dict = docs_cloud_tenant_info_wrapper_instance.to_dict()
# create an instance of DocsCloudTenantInfoWrapper from a dict
docs_cloud_tenant_info_wrapper_from_dict = DocsCloudTenantInfoWrapper.from_dict(docs_cloud_tenant_info_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


