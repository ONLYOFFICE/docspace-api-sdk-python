# TfaSetupCodeDto
The setup TFA code parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | The account for which the setup code is generated. | [optional] [readonly] 
**manual_entry_key** | **str** | The manual entry key. | [optional] [readonly] 
**qr_code_setup_image_url** | **str** | The QR-code setup image URL (base64-encoded PNG image). | [optional] [readonly] 

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


