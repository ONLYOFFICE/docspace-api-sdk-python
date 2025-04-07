# TipsRequestDto

Settings request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show** | **bool** | Specifies whether to show tips for the user or not | [optional] 

## Example

```python
from docspace.models.tips_request_dto import TipsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TipsRequestDto from a JSON string
tips_request_dto_instance = TipsRequestDto.from_json(json)
# print the JSON string representation of the object
print(TipsRequestDto.to_json())

# convert the object into a dict
tips_request_dto_dict = tips_request_dto_instance.to_dict()
# create an instance of TipsRequestDto from a dict
tips_request_dto_from_dict = TipsRequestDto.from_dict(tips_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


