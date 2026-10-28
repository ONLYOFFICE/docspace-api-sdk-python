# TfaAppCodeDto
One backup code of the caller's authenticator credential.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_used** | **bool** | Whether the code has already been spent. A spent code is kept in the list but is no longer accepted, so  count the entries where this is `false` to know how many fallbacks remain. | [optional] 
**code** | **str** | The code itself, in the form it is typed at sign-in - six characters with the default configuration. It is  stored encrypted and decrypted for this answer, so this is the one place a caller can read it. | [optional] 

## Example

```python
from docspace_api_sdk.models.tfa_app_code_dto import TfaAppCodeDto

# TODO update the JSON string below
json = "{}"
# create an instance of TfaAppCodeDto from a JSON string
tfa_app_code_dto_instance = TfaAppCodeDto.from_json(json)
# print the JSON string representation of the object
print(TfaAppCodeDto.to_json())

# convert the object into a dict
tfa_app_code_dto_dict = tfa_app_code_dto_instance.to_dict()
# create an instance of TfaAppCodeDto from a dict
tfa_app_code_dto_from_dict = TfaAppCodeDto.from_dict(tfa_app_code_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


