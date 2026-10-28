# FormGalleryDto
Where the ready-made form templates are served from, for browsing them and for submitting new ones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path under `domain` that the gallery's own listing API is reached at. It is joined to `domain` by the  client; the portal only relays the values from its configuration. | 
**domain** | **str** | The address of the gallery service, which is a service of the vendor rather than part of the portal. Every  field of this object is empty on an installation that configures no gallery, and a client should then not  offer the gallery at all. | 
**ext** | **str** | The file extension to ask the gallery for, which decides which rendition of a template is downloaded when  several are published. | 
**upload_path** | **str** | The path used for submitting a form of one's own to the gallery, the counterpart of `path` for the upload  side. The four `upload` fields are empty when the installation allows browsing but not submitting. | 
**upload_domain** | **str** | The address the submission is sent to, which may differ from `domain`. | 
**upload_ext** | **str** | The file extension a submitted form has to carry. | 
**upload_dashboard** | **str** | The page a person is sent to in order to follow up on a submission, joined to `uploadDomain` the same way  as `uploadPath`. | 

## Example

```python
from docspace_api_sdk.models.form_gallery_dto import FormGalleryDto

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


