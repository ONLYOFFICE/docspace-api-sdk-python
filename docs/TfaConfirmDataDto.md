# TfaConfirmDataDto
The TFA confirmation data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The confirmation URL. | [optional] 
**cookie_name** | **str** | The confirmation cookie name. | [optional] 
**cookie_value** | **str** | The confirmation cookie value. | [optional] 

## Example

```python
from docspace_api_sdk.models.tfa_confirm_data_dto import TfaConfirmDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of TfaConfirmDataDto from a JSON string
tfa_confirm_data_dto_instance = TfaConfirmDataDto.from_json(json)
# print the JSON string representation of the object
print(TfaConfirmDataDto.to_json())

# convert the object into a dict
tfa_confirm_data_dto_dict = tfa_confirm_data_dto_instance.to_dict()
# create an instance of TfaConfirmDataDto from a dict
tfa_confirm_data_dto_from_dict = TfaConfirmDataDto.from_dict(tfa_confirm_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


