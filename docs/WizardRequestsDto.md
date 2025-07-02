# WizardRequestsDto
The request parameters for initial configuration of the setup wizard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s email address for authentication and communication. | 
**password_hash** | **str** | The hashed representation of the user&#39;s password. | 
**lng** | **str** | The user&#39;s preferred interface language code. | [optional] 
**time_zone** | **str** | The user&#39;s time zone identifier. | [optional] 
**ami_id** | **str** | The Amazon Machine Image (AMI) identifier. | [optional] 
**subscribe_from_site** | **bool** | Specifies whether the user opted in for site communications. | [optional] 

## Example

```python
from docspace-api-python.models.wizard_requests_dto import WizardRequestsDto

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


