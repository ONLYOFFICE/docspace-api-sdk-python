# TfaRequestsDto

The request parameters for configuring the Two-Factor Authentication (TFA) settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TfaRequestsDtoType**](TfaRequestsDtoType.md) |  | [optional] 
**id** | **str** | The ID of the user for whom the TFA settings are being configured. | [optional] 
**trusted_ips** | **List[str]** | The list of IP addresses that bypass TFA verification. | [optional] 
**mandatory_users** | **List[str]** | The list of user IDs for whom TFA is mandatory. | [optional] 
**mandatory_groups** | **List[str]** | The list group IDs whose members must use TFA. | [optional] 

## Example

```python
from docspace.models.tfa_requests_dto import TfaRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TfaRequestsDto from a JSON string
tfa_requests_dto_instance = TfaRequestsDto.from_json(json)
# print the JSON string representation of the object
print(TfaRequestsDto.to_json())

# convert the object into a dict
tfa_requests_dto_dict = tfa_requests_dto_instance.to_dict()
# create an instance of TfaRequestsDto from a dict
tfa_requests_dto_from_dict = TfaRequestsDto.from_dict(tfa_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


