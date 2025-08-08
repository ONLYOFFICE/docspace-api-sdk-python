# ProductAdministratorDto
The product administrator parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The product ID. | [optional] 
**user_id** | **str** | The user unique identifier. | [optional] 
**administrator** | **bool** | Indicates whether the user has administrator privileges for the product. | [optional] 

## Example

```python
from docspace_api_sdk.models.product_administrator_dto import ProductAdministratorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAdministratorDto from a JSON string
product_administrator_dto_instance = ProductAdministratorDto.from_json(json)
# print the JSON string representation of the object
print(ProductAdministratorDto.to_json())

# convert the object into a dict
product_administrator_dto_dict = product_administrator_dto_instance.to_dict()
# create an instance of ProductAdministratorDto from a dict
product_administrator_dto_from_dict = ProductAdministratorDto.from_dict(product_administrator_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


