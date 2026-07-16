# CustomerServiceUsageReportWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CustomerServiceUsageReportDto**](CustomerServiceUsageReportDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_service_usage_report_wrapper import CustomerServiceUsageReportWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerServiceUsageReportWrapper from a JSON string
customer_service_usage_report_wrapper_instance = CustomerServiceUsageReportWrapper.from_json(json)
# print the JSON string representation of the object
print(CustomerServiceUsageReportWrapper.to_json())

# convert the object into a dict
customer_service_usage_report_wrapper_dict = customer_service_usage_report_wrapper_instance.to_dict()
# create an instance of CustomerServiceUsageReportWrapper from a dict
customer_service_usage_report_wrapper_from_dict = CustomerServiceUsageReportWrapper.from_dict(customer_service_usage_report_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


