# CustomerConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address | [optional] 
**logo** | **str** | Logo | [optional] 
**logo_dark** | **str** | Dark logo | [optional] 
**mail** | **str** | Mail | [optional] 
**name** | **str** | Name | [optional] 
**www** | **str** | Site | [optional] 

## Example

```python
from docspace.models.customer_config_dto import CustomerConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerConfigDto from a JSON string
customer_config_dto_instance = CustomerConfigDto.from_json(json)
# print the JSON string representation of the object
print(CustomerConfigDto.to_json())

# convert the object into a dict
customer_config_dto_dict = customer_config_dto_instance.to_dict()
# create an instance of CustomerConfigDto from a dict
customer_config_dto_from_dict = CustomerConfigDto.from_dict(customer_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


