# ThirdPartyBackupRequestDto
The third-party backup request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The connection URL for the sharepoint. | [optional] 
**login** | **str** | The login. | [optional] 
**password** | **str** | The password. | [optional] 
**token** | **str** | The authentication token. | [optional] 
**customer_title** | **str** | The customer title. | [optional] 
**provider_key** | **str** | The provider key. | [optional] 

## Example

```python
from docspace-api-python.models.third_party_backup_request_dto import ThirdPartyBackupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyBackupRequestDto from a JSON string
third_party_backup_request_dto_instance = ThirdPartyBackupRequestDto.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyBackupRequestDto.to_json())

# convert the object into a dict
third_party_backup_request_dto_dict = third_party_backup_request_dto_instance.to_dict()
# create an instance of ThirdPartyBackupRequestDto from a dict
third_party_backup_request_dto_from_dict = ThirdPartyBackupRequestDto.from_dict(third_party_backup_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


