# AuthData
The credentials of a third-party storage account. The portal takes them when an account is connected and does not  give them back afterwards.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | The account name at the storage service. | [optional] 
**password** | **str** | The password of the account at the storage service. | [optional] 
**raw_token** | **str** | The token of the account, kept as the raw JSON document the storage service issued it in. | [optional] 
**url** | **str** | The address of the storage server the account lives on. | [optional] 
**provider** | **str** | The storage service the credentials belong to, as the provider key the account was connected with. | [optional] 
**token** | [**OAuth20Token**](OAuth20Token.md) | The same token as in `rawToken`, parsed into its OAuth 2.0 fields. | [optional] 

## Example

```python
from docspace_api_sdk.models.auth_data import AuthData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthData from a JSON string
auth_data_instance = AuthData.from_json(json)
# print the JSON string representation of the object
print(AuthData.to_json())

# convert the object into a dict
auth_data_dict = auth_data_instance.to_dict()
# create an instance of AuthData from a dict
auth_data_from_dict = AuthData.from_dict(auth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


