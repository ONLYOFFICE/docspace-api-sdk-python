# ThirdPartyRequestDto

Third-party request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Connection URL for the sharepoint | [optional] 
**login** | **str** | Login | [optional] 
**password** | **str** | Password | [optional] 
**token** | **str** | Authentication token | [optional] 
**customer_title** | **str** | Customer title | [optional] 
**provider_key** | **str** | Provider key | [optional] 
**provider_id** | **int** | Provider ID | [optional] 

## Example

```python
from docspace.models.third_party_request_dto import ThirdPartyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyRequestDto from a JSON string
third_party_request_dto_instance = ThirdPartyRequestDto.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyRequestDto.to_json())

# convert the object into a dict
third_party_request_dto_dict = third_party_request_dto_instance.to_dict()
# create an instance of ThirdPartyRequestDto from a dict
third_party_request_dto_from_dict = ThirdPartyRequestDto.from_dict(third_party_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


