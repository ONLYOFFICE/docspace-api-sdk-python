# SmtpOperationStatusRequestsDto
The request parameters for tracking SMTP (Simple Mail Transfer Protocol) operation status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Specifies whether the SMTP operation has finished processing. | [optional] 
**id** | **str** | The unique identifier for tracking the SMTP operation. | [optional] 
**error** | **str** | The error message if the SMTP operation encountered issues. | [optional] 
**status** | **str** | The current state of the SMTP operation. | [optional] 
**percents** | **int** | The progress indicator showing completion percentage of the operation. | [optional] 

## Example

```python
from docspace_api_sdk.models.smtp_operation_status_requests_dto import SmtpOperationStatusRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SmtpOperationStatusRequestsDto from a JSON string
smtp_operation_status_requests_dto_instance = SmtpOperationStatusRequestsDto.from_json(json)
# print the JSON string representation of the object
print(SmtpOperationStatusRequestsDto.to_json())

# convert the object into a dict
smtp_operation_status_requests_dto_dict = smtp_operation_status_requests_dto_instance.to_dict()
# create an instance of SmtpOperationStatusRequestsDto from a dict
smtp_operation_status_requests_dto_from_dict = SmtpOperationStatusRequestsDto.from_dict(smtp_operation_status_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


