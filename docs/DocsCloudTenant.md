# DocsCloudTenant
Represents a DocsCloud tenant of a portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dedicated_resource_ex_id** | **int** | The external ID of the dedicated resource the tenant is hosted on. | [optional] 
**alias** | **str** | The tenant alias. | [optional] 
**name** | **str** | The tenant name. | [optional] 
**modified_date** | **datetime** | The date and time when the tenant was last modified. | [optional] 
**customer_id** | **str** | The customer ID. | [optional] 
**customer_name** | **str** | The customer name. | [optional] 
**end_date** | **datetime** | The date and time when the tenant subscription ends. | [optional] 
**resource_type** | **int** | The resource type. | [optional] 
**is_active** | **bool** | Whether the tenant is active (the end date is in the future). | [optional] 
**address** | **str** | The tenant address. | [optional] 
**payment** | [**DocsCloudPayment**](DocsCloudPayment.md) | The tenant payment information. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_tenant import DocsCloudTenant

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudTenant from a JSON string
docs_cloud_tenant_instance = DocsCloudTenant.from_json(json)
# print the JSON string representation of the object
print(DocsCloudTenant.to_json())

# convert the object into a dict
docs_cloud_tenant_dict = docs_cloud_tenant_instance.to_dict()
# create an instance of DocsCloudTenant from a dict
docs_cloud_tenant_from_dict = DocsCloudTenant.from_dict(docs_cloud_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


