# SmtpOperationStatusRequestsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SmtpOperationStatusRequestsDto**](SmtpOperationStatusRequestsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.smtp_operation_status_requests_wrapper import SmtpOperationStatusRequestsWrapper

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


