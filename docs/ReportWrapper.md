# ReportWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ReportDto**](ReportDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.report_wrapper import ReportWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ReportWrapper from a JSON string
report_wrapper_instance = ReportWrapper.from_json(json)
# print the JSON string representation of the object
print(ReportWrapper.to_json())

# convert the object into a dict
report_wrapper_dict = report_wrapper_instance.to_dict()
# create an instance of ReportWrapper from a dict
report_wrapper_from_dict = ReportWrapper.from_dict(report_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


