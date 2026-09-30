# MobileRequestsDto
The phone number a user going through phone activation registers for SMS codes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile_phone** | **str** | The number the SMS codes are sent to, in international form with the leading `+` and no spaces. It is stored  as not yet activated and only becomes the confirmed number once a code sent to it is accepted; an already  activated number is not replaced this way and has to be erased first. | [optional] 

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


