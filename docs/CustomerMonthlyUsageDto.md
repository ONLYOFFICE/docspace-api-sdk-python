# CustomerMonthlyUsageDto
Aggregated customer spending for a single calendar month.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | The calendar year. | [optional] 
**month** | **int** | The calendar month (1-12). | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol of the amounts. | [optional] 
**total_amount** | **float** | The total amount charged across all services in this month. | [optional] 
**operation_count** | **int** | The number of individual purchase operations in this month. | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_monthly_usage_dto import CustomerMonthlyUsageDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerMonthlyUsageDto from a JSON string
customer_monthly_usage_dto_instance = CustomerMonthlyUsageDto.from_json(json)
# print the JSON string representation of the object
print(CustomerMonthlyUsageDto.to_json())

# convert the object into a dict
customer_monthly_usage_dto_dict = customer_monthly_usage_dto_instance.to_dict()
# create an instance of CustomerMonthlyUsageDto from a dict
customer_monthly_usage_dto_from_dict = CustomerMonthlyUsageDto.from_dict(customer_monthly_usage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


