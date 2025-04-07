# SmtpOperationStatusRequestsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Specifies if the SMTP operation is completed or not | [optional] 
**id** | **str** | SMTP operation ID | [optional] 
**error** | **str** | SMTP operation error | [optional] 
**status** | **str** | SMTP operation status | [optional] 
**percents** | **int** | Percentage of SMTP operation completion | [optional] 

## Example

```python
from docspace.models.smtp_operation_status_requests_dto import SmtpOperationStatusRequestsDto

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


