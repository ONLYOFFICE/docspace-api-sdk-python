# ConfirmDto
The confirmation parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ValidationResult**](ValidationResult.md) |  | [optional] 
**room_id** | **str** | The confirmation room ID. | [optional] 
**title** | **str** | The confirmation title. | [optional] 

## Example

```python
from docspace-api-sdk.models.confirm_dto import ConfirmDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmDto from a JSON string
confirm_dto_instance = ConfirmDto.from_json(json)
# print the JSON string representation of the object
print(ConfirmDto.to_json())

# convert the object into a dict
confirm_dto_dict = confirm_dto_instance.to_dict()
# create an instance of ConfirmDto from a dict
confirm_dto_from_dict = ConfirmDto.from_dict(confirm_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


