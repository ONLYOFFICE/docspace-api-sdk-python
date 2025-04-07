# ThumbnailsRequest

Thumbnail request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tmp_file** | **str** | Path to the temporary file | [optional] 
**x** | **int** | Horizontal coordinate | [optional] 
**y** | **int** | Vertical coordinate | [optional] 
**width** | **int** | Thumbnail width | [optional] 
**height** | **int** | Thumbnail height | [optional] 

## Example

```python
from docspace.models.thumbnails_request import ThumbnailsRequest

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


