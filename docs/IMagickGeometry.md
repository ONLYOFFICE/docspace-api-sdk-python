# IMagickGeometry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **bool** |  | [optional] [readonly] 
**fill_area** | **bool** |  | [optional] 
**greater** | **bool** |  | [optional] 
**height** | **int** |  | [optional] 
**ignore_aspect_ratio** | **bool** |  | [optional] 
**is_percentage** | **bool** |  | [optional] 
**less** | **bool** |  | [optional] 
**limit_pixels** | **bool** |  | [optional] 
**width** | **int** |  | [optional] 
**x** | **int** |  | [optional] 
**y** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.i_magick_geometry import IMagickGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of IMagickGeometry from a JSON string
i_magick_geometry_instance = IMagickGeometry.from_json(json)
# print the JSON string representation of the object
print(IMagickGeometry.to_json())

# convert the object into a dict
i_magick_geometry_dict = i_magick_geometry_instance.to_dict()
# create an instance of IMagickGeometry from a dict
i_magick_geometry_from_dict = IMagickGeometry.from_dict(i_magick_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


