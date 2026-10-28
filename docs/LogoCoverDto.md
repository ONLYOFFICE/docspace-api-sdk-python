# LogoCoverDto
The logo cover information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The logo cover ID. | 
**data** | **str** | The logo cover data. | 

## Example

```python
from docspace_api_sdk.models.logo_cover_dto import LogoCoverDto

# TODO update the JSON string below
json = "{}"
# create an instance of LogoCoverDto from a JSON string
logo_cover_dto_instance = LogoCoverDto.from_json(json)
# print the JSON string representation of the object
print(LogoCoverDto.to_json())

# convert the object into a dict
logo_cover_dto_dict = logo_cover_dto_instance.to_dict()
# create an instance of LogoCoverDto from a dict
logo_cover_dto_from_dict = LogoCoverDto.from_dict(logo_cover_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


