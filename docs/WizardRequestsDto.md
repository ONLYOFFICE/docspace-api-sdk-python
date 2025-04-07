# WizardRequestsDto

Wizard settings request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email | [optional] 
**password_hash** | **str** | Password hash | [optional] 
**lng** | **str** | Language | [optional] 
**time_zone** | **str** | Time zone | [optional] 
**ami_id** | **str** | AMI ID | [optional] 
**subscribe_from_site** | **bool** | Subscribed from the site or not | [optional] 

## Example

```python
from docspace.models.wizard_requests_dto import WizardRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WizardRequestsDto from a JSON string
wizard_requests_dto_instance = WizardRequestsDto.from_json(json)
# print the JSON string representation of the object
print(WizardRequestsDto.to_json())

# convert the object into a dict
wizard_requests_dto_dict = wizard_requests_dto_instance.to_dict()
# create an instance of WizardRequestsDto from a dict
wizard_requests_dto_from_dict = WizardRequestsDto.from_dict(wizard_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


