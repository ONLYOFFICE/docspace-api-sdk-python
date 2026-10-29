# ServiceLimitReportWrapper
The successful API response containing the ServiceLimitReportDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ServiceLimitReportDto**](ServiceLimitReportDto.md) | The ServiceLimitReportDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.service_limit_report_wrapper import ServiceLimitReportWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLimitReportWrapper from a JSON string
service_limit_report_wrapper_instance = ServiceLimitReportWrapper.from_json(json)
# print the JSON string representation of the object
print(ServiceLimitReportWrapper.to_json())

# convert the object into a dict
service_limit_report_wrapper_dict = service_limit_report_wrapper_instance.to_dict()
# create an instance of ServiceLimitReportWrapper from a dict
service_limit_report_wrapper_from_dict = ServiceLimitReportWrapper.from_dict(service_limit_report_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


