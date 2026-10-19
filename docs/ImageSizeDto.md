# ImageSizeDto
A pixel size measured on the image itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | The height of the image in pixels, read from the stored file rather than from any display setting. | [optional] 
**width** | **int** | The width of the image in pixels, read from the stored file rather than from any display setting. | [optional] 

## Example

```python
from docspace_api_sdk.models.image_size_dto import ImageSizeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImageSizeDto from a JSON string
image_size_dto_instance = ImageSizeDto.from_json(json)
# print the JSON string representation of the object
print(ImageSizeDto.to_json())

# convert the object into a dict
image_size_dto_dict = image_size_dto_instance.to_dict()
# create an instance of ImageSizeDto from a dict
image_size_dto_from_dict = ImageSizeDto.from_dict(image_size_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


