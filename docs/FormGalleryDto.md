# FormGalleryDto
The form gallery parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The form gallery path. | [optional] 
**domain** | **str** | The form gallery domain. | [optional] 
**ext** | **str** | The form gallery extension. | [optional] 
**upload_path** | **str** | The form gallery upload path. | [optional] 
**upload_domain** | **str** | The form gallery upload domain. | [optional] 
**upload_ext** | **str** | The form gallery upload extension. | [optional] 
**upload_dashboard** | **str** | The form gallery upload dashboard. | [optional] 

## Example

```python
from docspace-api-sdk.models.form_gallery_dto import FormGalleryDto

# TODO update the JSON string below
json = "{}"
# create an instance of FormGalleryDto from a JSON string
form_gallery_dto_instance = FormGalleryDto.from_json(json)
# print the JSON string representation of the object
print(FormGalleryDto.to_json())

# convert the object into a dict
form_gallery_dto_dict = form_gallery_dto_instance.to_dict()
# create an instance of FormGalleryDto from a dict
form_gallery_dto_from_dict = FormGalleryDto.from_dict(form_gallery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


