# TfaSetupCodeDto
The secret to enrol in an authenticator application, in both of the forms an application can take it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The label the authenticator application will list the credential under, which is the caller's own email  address. It identifies the entry to a person, and no application checks it. | [optional] [readonly] 
**manual_entry_key** | **str** | The secret in the base32 form that is typed into an application by hand. It describes the very same  credential as `qrCodeSetupImageUrl`, and repeating the call hands back the same value for the account until  the credential is reset. | [optional] [readonly] 
**qr_code_setup_image_url** | **str** | The same secret as a scannable image, given as a `data:image/png;base64,` URL that can be rendered  directly - it is not a link to fetch. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.tfa_setup_code_dto import TfaSetupCodeDto

# TODO update the JSON string below
json = "{}"
# create an instance of TfaSetupCodeDto from a JSON string
tfa_setup_code_dto_instance = TfaSetupCodeDto.from_json(json)
# print the JSON string representation of the object
print(TfaSetupCodeDto.to_json())

# convert the object into a dict
tfa_setup_code_dto_dict = tfa_setup_code_dto_instance.to_dict()
# create an instance of TfaSetupCodeDto from a dict
tfa_setup_code_dto_from_dict = TfaSetupCodeDto.from_dict(tfa_setup_code_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


