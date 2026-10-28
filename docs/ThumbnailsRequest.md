# ThumbnailsRequest
The crop rectangle to apply to an avatar image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tmp_file** | **str** | The temporary image to crop, as returned in the `data` of an upload made with `autosave` off. Only the file  name part of the value is used. Omit it to re-crop the photo the profile already has. | [optional] 
**x** | **int** | The distance in pixels from the left edge of the original image to the left edge of the crop rectangle. | [optional] 
**y** | **int** | The distance in pixels from the top edge of the original image to the top edge of the crop rectangle. | [optional] 
**width** | **int** | The width of the crop rectangle in pixels. Passing 0 together with `height` and `tmpFile` keeps the whole  uploaded image instead of cropping it. | [optional] 
**height** | **int** | The height of the crop rectangle in pixels. Passing 0 together with `width` and `tmpFile` keeps the whole  uploaded image instead of cropping it. | [optional] 

## Example

```python
from docspace_api_sdk.models.thumbnails_request import ThumbnailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailsRequest from a JSON string
thumbnails_request_instance = ThumbnailsRequest.from_json(json)
# print the JSON string representation of the object
print(ThumbnailsRequest.to_json())

# convert the object into a dict
thumbnails_request_dict = thumbnails_request_instance.to_dict()
# create an instance of ThumbnailsRequest from a dict
thumbnails_request_from_dict = ThumbnailsRequest.from_dict(thumbnails_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


