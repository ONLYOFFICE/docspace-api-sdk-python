# SalesRequestsDto
Who is writing to the ONLYOFFICE sales team, and what about.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | The name the sales team should address the reply to. It is sent as written and is not matched against any  portal account; an empty value fails the request with 400. | 
**email** | **str** | The address the answer is sent to. It has to be a well-formed email address and need not be the caller portal  address; an empty or malformed value fails the request with 400. | 
**message** | **str** | What is being asked of the sales team - a quote, an invoice, or a plan that cannot be bought online. An empty  value fails the request with 400. | 

## Example

```python
from docspace_api_sdk.models.sales_requests_dto import SalesRequestsDto

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


