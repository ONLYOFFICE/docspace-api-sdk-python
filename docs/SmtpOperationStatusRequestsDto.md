# SmtpOperationStatusRequestsDto
The state of the background job that sends the portal SMTP test message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Whether the job has finished. This is the field to poll; the first answer that reports it true also discards  the job, so read `error` out of that same answer rather than calling again. | [optional] 
**id** | **str** | The identifier of the queued job. A portal only ever has one test job at a time, so it names the run rather  than selecting among several. | [optional] 
**error** | **str** | Why the test failed. It stays empty while the job runs and also once the relay has accepted the message, so  an empty value on a finished job is what success looks like; an unreachable relay is reported here after a  30-second connection timeout rather than as a failed request. | [optional] 
**status** | **str** | The step the job has reached, in words - `Connect to host` or `Send test message`, for instance. It is meant  to be shown to a person and is not a fixed set of values to branch on. | [optional] 
**percents** | **int** | How far the job has got, as a percentage climbing to 100. Reaching 100 says the job ran to the end, not that  the message was accepted - that is what an empty `error` says. | [optional] 

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


