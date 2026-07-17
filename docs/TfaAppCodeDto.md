# TfaAppCodeDto
The TFA app code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_used** | **bool** | The TFA app code usage status. | [optional] 
**code** | **str** | The TFA app code. | [optional] 

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


