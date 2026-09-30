# TfaRequestsDto
The portal two-factor policy: which method is in force, who must pass it, and from where it is waived.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TfaRequestsDtoType**](TfaRequestsDtoType.md) | The second factor the portal demands. The two methods are mutually exclusive, so switching one on switches  the other off, and any value outside the defined set is read as switching TFA off rather than refused. | [optional] 
**id** | **UUID** | The account the request concerns, by portal user ID. Naming the portal owner is refused unless it is the  caller's own account. Where an operation detaches an authenticator application, the empty GUID and the  caller's own ID both mean the caller. | [optional] 
**trusted_ips** | **List[str]** | The list of IP addresses that bypass TFA verification. Each entry is a single address, an inclusive  from-to range or a CIDR block. This is the whole list that is to hold afterwards, so send the addresses  already trusted along with a new one; an entry that cannot be parsed fails the call with 400, and accounts  named as mandatory still have to pass the challenge even from a trusted address. | [optional] 
**mandatory_users** | **List[UUID]** | The accounts that must pass the challenge whatever their address, by portal user ID. This is the whole list  that is to hold afterwards - leaving it out clears it rather than keeping it - and naming the portal owner is  refused unless the caller is the owner. | [optional] 
**mandatory_groups** | **List[UUID]** | The groups whose members must pass the challenge whatever their address, by group ID. This is the whole list  that is to hold afterwards - leaving it out clears it rather than keeping it. | [optional] 

## Example

```python
from docspace_api_sdk.models.tfa_requests_dto import TfaRequestsDto

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


