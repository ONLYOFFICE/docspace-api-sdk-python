# ProductAdministratorWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ProductAdministratorDto**](ProductAdministratorDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.product_administrator_wrapper import ProductAdministratorWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAdministratorWrapper from a JSON string
product_administrator_wrapper_instance = ProductAdministratorWrapper.from_json(json)
# print the JSON string representation of the object
print(ProductAdministratorWrapper.to_json())

# convert the object into a dict
product_administrator_wrapper_dict = product_administrator_wrapper_instance.to_dict()
# create an instance of ProductAdministratorWrapper from a dict
product_administrator_wrapper_from_dict = ProductAdministratorWrapper.from_dict(product_administrator_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


