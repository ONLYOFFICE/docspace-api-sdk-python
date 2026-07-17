# XlsxReportResponseWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**XlsxReportResponseDto**](XlsxReportResponseDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.xlsx_report_response_wrapper import XlsxReportResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of XlsxReportResponseWrapper from a JSON string
xlsx_report_response_wrapper_instance = XlsxReportResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(XlsxReportResponseWrapper.to_json())

# convert the object into a dict
xlsx_report_response_wrapper_dict = xlsx_report_response_wrapper_instance.to_dict()
# create an instance of XlsxReportResponseWrapper from a dict
xlsx_report_response_wrapper_from_dict = XlsxReportResponseWrapper.from_dict(xlsx_report_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


