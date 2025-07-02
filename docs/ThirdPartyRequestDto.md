# ThirdPartyRequestDto
The third-party request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The connection URL for the sharepoint. | [optional] 
**login** | **str** | The third-party request login. | [optional] 
**password** | **str** | The third-party request password. | [optional] 
**token** | **str** | The authentication token. | [optional] 
**customer_title** | **str** | The customer title. | [optional] 
**provider_key** | **str** | The provider key. | [optional] 
**provider_id** | **int** | The provider ID. | [optional] 

## Example

```python
from docspace-api-python.models.third_party_request_dto import ThirdPartyRequestDto

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


