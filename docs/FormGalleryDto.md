# FormGalleryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path | [optional] 
**domain** | **str** | Domain | [optional] 
**ext** | **str** | Ext | [optional] 
**upload_path** | **str** | Upload path | [optional] 
**upload_domain** | **str** | Upload domain | [optional] 
**upload_ext** | **str** | Upload ext | [optional] 
**upload_dashboard** | **str** | Upload dashboard | [optional] 

## Example

```python
from docspace.models.form_gallery_dto import FormGalleryDto

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


