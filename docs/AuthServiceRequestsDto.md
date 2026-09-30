# AuthServiceRequestsDto
One third-party authorization or storage provider and the keys the portal connects to it with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The provider being configured, by its internal key such as `google` or `box`. Take it from the `name` of  `GET api/2.0/settings/authservice`; it is the only field that selects the provider, and a key this  installation does not know is refused the same way a provider that forbids changes is. | [optional] 
**title** | **str** | The provider name as it is shown in the interface. It is filled in by the portal when the providers are  listed and is ignored when keys are saved. | [optional] 
**description** | **str** | A sentence about what connecting the provider gives the portal, shown next to it in the interface. It is  filled in by the portal and ignored when keys are saved. | [optional] 
**instruction** | **str** | The steps an administrator has to take on the provider side to obtain the keys, shown in the interface. It is  filled in by the portal and ignored when keys are saved. | [optional] 
**can_set** | **bool** | Whether this provider accepts keys through the API at all. A provider whose keys are fixed by the  installation reports `false`, and saving keys for it is refused; the field is reported by the portal and  ignored on the way in. | [optional] 
**paid** | **bool** | Whether the provider is a paid option. A paid one can only be connected while the portal plan includes  third-party storage or the installation is licensed as self-hosted; the field is reported by the portal and  ignored on the way in. | [optional] 
**props** | [**List[AuthKey]**](AuthKey.md) | The credentials the portal authenticates to the provider with, as the name and value pairs the provider  defines. Send the whole set the provider expects: leaving every value empty disconnects it, and a set that  fails the provider validation is cleared rather than stored half-applied. The listing operation reports the  values last saved, and a provider that forbids changes reports none at all. | [optional] 

## Example

```python
from docspace_api_sdk.models.auth_service_requests_dto import AuthServiceRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthServiceRequestsDto from a JSON string
auth_service_requests_dto_instance = AuthServiceRequestsDto.from_json(json)
# print the JSON string representation of the object
print(AuthServiceRequestsDto.to_json())

# convert the object into a dict
auth_service_requests_dto_dict = auth_service_requests_dto_instance.to_dict()
# create an instance of AuthServiceRequestsDto from a dict
auth_service_requests_dto_from_dict = AuthServiceRequestsDto.from_dict(auth_service_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


