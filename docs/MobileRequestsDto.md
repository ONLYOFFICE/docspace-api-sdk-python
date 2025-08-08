# MobileRequestsDto
The parameters required for the mobile phone verification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_phone** | **str** | The user&#39;s mobile phone number. | [optional] 

## Example

```python
from docspace_api_sdk.models.mobile_requests_dto import MobileRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MobileRequestsDto from a JSON string
mobile_requests_dto_instance = MobileRequestsDto.from_json(json)
# print the JSON string representation of the object
print(MobileRequestsDto.to_json())

# convert the object into a dict
mobile_requests_dto_dict = mobile_requests_dto_instance.to_dict()
# create an instance of MobileRequestsDto from a dict
mobile_requests_dto_from_dict = MobileRequestsDto.from_dict(mobile_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


