# TfaRequestsDto

TFA settings request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TfaRequestsDtoType**](TfaRequestsDtoType.md) |  | [optional] 
**id** | **str** | User ID | [optional] 
**trusted_ips** | **List[str]** | List of trusted IP addresses | [optional] 
**mandatory_users** | **List[str]** | List of users who must use the TFA verification | [optional] 
**mandatory_groups** | **List[str]** | List of groups who must use the TFA verification | [optional] 

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


