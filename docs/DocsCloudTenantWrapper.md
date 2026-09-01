# DocsCloudTenantWrapper
The successful API response containing the DocsCloudTenant object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DocsCloudTenant**](DocsCloudTenant.md) | The DocsCloudTenant object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_tenant_wrapper import DocsCloudTenantWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudTenantWrapper from a JSON string
docs_cloud_tenant_wrapper_instance = DocsCloudTenantWrapper.from_json(json)
# print the JSON string representation of the object
print(DocsCloudTenantWrapper.to_json())

# convert the object into a dict
docs_cloud_tenant_wrapper_dict = docs_cloud_tenant_wrapper_instance.to_dict()
# create an instance of DocsCloudTenantWrapper from a dict
docs_cloud_tenant_wrapper_from_dict = DocsCloudTenantWrapper.from_dict(docs_cloud_tenant_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


