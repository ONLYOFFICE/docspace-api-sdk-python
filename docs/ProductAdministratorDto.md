# ProductAdministratorDto
Whether one user administers one portal module, echoing back the pair that was asked about.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | The module the verdict is about, echoed from the request. The all-zero GUID stands for the portal as a  whole rather than for any single module. | 
**user_id** | **UUID** | The user the verdict is about, echoed from the request unchanged - it is not checked for existing. | 
**administrator** | **bool** | Whether that user administers that module. It is `true` for a DocSpace administrator whatever the module,  since the portal-wide role covers every one of them. A `false` can also mean the identifiers name no user  or no module at all, so it is not proof that the user exists, and it says nothing about whether the module  is enabled for the portal - `GET api/2.0/settings/security/{id}` reports that. | 

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


