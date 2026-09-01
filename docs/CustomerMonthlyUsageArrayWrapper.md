# CustomerMonthlyUsageArrayWrapper
The successful API response containing the list of CustomerMonthlyUsageDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CustomerMonthlyUsageDto]**](CustomerMonthlyUsageDto.md) | The list of CustomerMonthlyUsageDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_monthly_usage_array_wrapper import CustomerMonthlyUsageArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerMonthlyUsageArrayWrapper from a JSON string
customer_monthly_usage_array_wrapper_instance = CustomerMonthlyUsageArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(CustomerMonthlyUsageArrayWrapper.to_json())

# convert the object into a dict
customer_monthly_usage_array_wrapper_dict = customer_monthly_usage_array_wrapper_instance.to_dict()
# create an instance of CustomerMonthlyUsageArrayWrapper from a dict
customer_monthly_usage_array_wrapper_from_dict = CustomerMonthlyUsageArrayWrapper.from_dict(customer_monthly_usage_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


