# WhiteLabelItemPathDto
The white label item path parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light** | **str** | The path to the light theme logo. | [optional] 
**dark** | **str** | The path to the dark theme logo. | [optional] 

## Example

```python
from docspace_api_sdk.models.white_label_item_path_dto import WhiteLabelItemPathDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteLabelItemPathDto from a JSON string
white_label_item_path_dto_instance = WhiteLabelItemPathDto.from_json(json)
# print the JSON string representation of the object
print(WhiteLabelItemPathDto.to_json())

# convert the object into a dict
white_label_item_path_dto_dict = white_label_item_path_dto_instance.to_dict()
# create an instance of WhiteLabelItemPathDto from a dict
white_label_item_path_dto_from_dict = WhiteLabelItemPathDto.from_dict(white_label_item_path_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


