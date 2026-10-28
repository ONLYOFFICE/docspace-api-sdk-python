# CustomerConfigDto
The branding of the organization running the portal, as the editor About panel shows it. It is reported on a  server installation only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The postal address from the portal branding settings; empty when none was entered. | [optional] 
**logo** | **str** | The About-panel logo of the organization. | [optional] 
**logo_dark** | **str** | The About-panel logo for a dark interface theme. | [optional] 
**mail** | **str** | The contact address from the portal branding settings. | [optional] 
**name** | **str** | The organization name shown in the editor. | [optional] 
**www** | **str** | The website of the organization. | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_config_dto import CustomerConfigDto

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


