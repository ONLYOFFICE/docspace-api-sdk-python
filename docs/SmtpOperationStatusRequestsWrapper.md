# SmtpOperationStatusRequestsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SmtpOperationStatusRequestsDto**](SmtpOperationStatusRequestsDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.smtp_operation_status_requests_wrapper import SmtpOperationStatusRequestsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SmtpOperationStatusRequestsWrapper from a JSON string
smtp_operation_status_requests_wrapper_instance = SmtpOperationStatusRequestsWrapper.from_json(json)
# print the JSON string representation of the object
print(SmtpOperationStatusRequestsWrapper.to_json())

# convert the object into a dict
smtp_operation_status_requests_wrapper_dict = smtp_operation_status_requests_wrapper_instance.to_dict()
# create an instance of SmtpOperationStatusRequestsWrapper from a dict
smtp_operation_status_requests_wrapper_from_dict = SmtpOperationStatusRequestsWrapper.from_dict(smtp_operation_status_requests_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


