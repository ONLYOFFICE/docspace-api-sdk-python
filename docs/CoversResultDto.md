# CoversResultDto
One drawing of the built-in gallery of room covers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The name of the cover, and the value to send as `cover` when a room is created or changed. The names are the  same on every portal and do not change with the language of the request. | 
**data** | **str** | The drawing itself, as inline vector markup ready to be rendered as it is. It is the default size of the  cover, and it may change between product versions while the name stays. | 

## Example

```python
from docspace_api_sdk.models.covers_result_dto import CoversResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of CoversResultDto from a JSON string
covers_result_dto_instance = CoversResultDto.from_json(json)
# print the JSON string representation of the object
print(CoversResultDto.to_json())

# convert the object into a dict
covers_result_dto_dict = covers_result_dto_instance.to_dict()
# create an instance of CoversResultDto from a dict
covers_result_dto_from_dict = CoversResultDto.from_dict(covers_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


