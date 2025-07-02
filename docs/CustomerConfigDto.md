# CustomerConfigDto
The customer config parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the customer configuration. | [optional] 
**logo** | **str** | The logo of the customer configuration. | [optional] 
**logo_dark** | **str** | The dark logo of the customer configuration. | [optional] 
**mail** | **str** | The mail address of the customer configuration. | [optional] 
**name** | **str** | The name of the customer configuration. | [optional] 
**www** | **str** | The site web address of the customer configuration. | [optional] 

## Example

```python
from docspace-api-python.models.customer_config_dto import CustomerConfigDto

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


