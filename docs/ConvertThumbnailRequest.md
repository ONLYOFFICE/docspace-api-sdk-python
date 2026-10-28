# ConvertThumbnailRequest
How a thumbnail is fitted. A field left out takes the document service default.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect** | **int** | The mode to fit the image to the height and width specified:  0 - stretch file to fit height and width;  1 - keep the aspect for the image;  2 - convert the metric size of the page into pixels at 96 dpi. | [optional] 
**first** | **bool** | Whether a thumbnail is made of the first page only; false makes one of every page. | [optional] 
**height** | **int** | The thumbnail height in pixels; not used with aspect 2. | [optional] 
**width** | **int** | The thumbnail width in pixels; not used with aspect 2. | [optional] 

## Example

```python
from docspace_api_sdk.models.convert_thumbnail_request import ConvertThumbnailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertThumbnailRequest from a JSON string
convert_thumbnail_request_instance = ConvertThumbnailRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertThumbnailRequest.to_json())

# convert the object into a dict
convert_thumbnail_request_dict = convert_thumbnail_request_instance.to_dict()
# create an instance of ConvertThumbnailRequest from a dict
convert_thumbnail_request_from_dict = ConvertThumbnailRequest.from_dict(convert_thumbnail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


