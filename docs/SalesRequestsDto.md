# SalesRequestsDto
The request parameters for handling sales and payment inquiries in the portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | The name of the user submitting the sales request. | [optional] 
**email** | **str** | The contact email address for the sales inquiry. | 
**message** | **str** | The details of the sales inquiry or payment request. | 

## Example

```python
from docspace-api-sdk.models.sales_requests_dto import SalesRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SalesRequestsDto from a JSON string
sales_requests_dto_instance = SalesRequestsDto.from_json(json)
# print the JSON string representation of the object
print(SalesRequestsDto.to_json())

# convert the object into a dict
sales_requests_dto_dict = sales_requests_dto_instance.to_dict()
# create an instance of SalesRequestsDto from a dict
sales_requests_dto_from_dict = SalesRequestsDto.from_dict(sales_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


