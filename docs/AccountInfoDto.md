# AccountInfoDto
The account information parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The name of the identity provider, in lowercase, as every other operation of this group expects it: `google`,  `zoom`, `linkedin`, `facebook`, `twitter`, `microsoft`, `appleid`, `weixin` or `nextcloud`. | 
**url** | **str** | The URL that starts the login with this provider. Open it as it is - it already carries the provider and the  popup or redirect mode the request asked for. | 
**linked** | **bool** | Whether this provider is already linked to the calling profile. It is always false for an anonymous caller,  because there is no profile to compare against. | 

## Example

```python
from docspace_api_sdk.models.account_info_dto import AccountInfoDto

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


