# ThumbnailsDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** | Original photo | [optional] 
**retina** | **str** | Retina | [optional] 
**max** | **str** | Maximum size | [optional] 
**big** | **str** | Big | [optional] 
**medium** | **str** | Medium | [optional] 
**small** | **str** | Small | [optional] 

## Example

```python
from docspace.models.thumbnails_data_dto import ThumbnailsDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailsDataDto from a JSON string
thumbnails_data_dto_instance = ThumbnailsDataDto.from_json(json)
# print the JSON string representation of the object
print(ThumbnailsDataDto.to_json())

# convert the object into a dict
thumbnails_data_dto_dict = thumbnails_data_dto_instance.to_dict()
# create an instance of ThumbnailsDataDto from a dict
thumbnails_data_dto_from_dict = ThumbnailsDataDto.from_dict(thumbnails_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


