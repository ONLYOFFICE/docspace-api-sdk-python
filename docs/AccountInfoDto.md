# AccountInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Provider | [optional] 
**url** | **str** | URL | [optional] 
**linked** | **bool** | Specifies if an account is linked or not | [optional] 

## Example

```python
from docspace.models.account_info_dto import AccountInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoDto from a JSON string
account_info_dto_instance = AccountInfoDto.from_json(json)
# print the JSON string representation of the object
print(AccountInfoDto.to_json())

# convert the object into a dict
account_info_dto_dict = account_info_dto_instance.to_dict()
# create an instance of AccountInfoDto from a dict
account_info_dto_from_dict = AccountInfoDto.from_dict(account_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


