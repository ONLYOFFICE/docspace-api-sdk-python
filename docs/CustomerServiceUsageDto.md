# CustomerServiceUsageDto
Aggregated customer usage statistics for a service over a period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | The name of the service. | [optional] 
**title** | **str** | The title of the service. | [optional] 
**service_unit** | **str** | The unit of measurement for the service. | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol of the amounts. | [optional] 
**total_quantity** | **int** | The total number of units consumed. | [optional] 
**total_amount** | **float** | The total amount charged for the service. | [optional] 
**operation_count** | **int** | The number of individual purchase operations. | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_service_usage_dto import CustomerServiceUsageDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerServiceUsageDto from a JSON string
customer_service_usage_dto_instance = CustomerServiceUsageDto.from_json(json)
# print the JSON string representation of the object
print(CustomerServiceUsageDto.to_json())

# convert the object into a dict
customer_service_usage_dto_dict = customer_service_usage_dto_instance.to_dict()
# create an instance of CustomerServiceUsageDto from a dict
customer_service_usage_dto_from_dict = CustomerServiceUsageDto.from_dict(customer_service_usage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


