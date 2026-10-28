# LogoRequest
The part of an uploaded picture to use as the logo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tmp_file** | **str** | The picture to cut the logo out of, named by the path that `POST api/2.0/files/logos` returned for it. The  path may be used once and only by the account that uploaded it. | 
**x** | **int** | The left edge of the rectangle cut out of the uploaded picture, counted in pixels from its left side. The  picture itself was already scaled down to fit 1280 by 1280 pixels when it was uploaded. | [optional] 
**y** | **int** | The top edge of the rectangle cut out of the uploaded picture, counted in pixels from its top. | [optional] 
**width** | **int** | How wide a piece of the uploaded picture to cut out, in pixels. It has to be sent together with the height,  and the portal builds the four logo sizes out of the piece. | [optional] 
**height** | **int** | How tall a piece of the uploaded picture to cut out, in pixels. It has to be sent together with the width. | [optional] 

## Example

```python
from docspace_api_sdk.models.logo_request import LogoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogoRequest from a JSON string
logo_request_instance = LogoRequest.from_json(json)
# print the JSON string representation of the object
print(LogoRequest.to_json())

# convert the object into a dict
logo_request_dict = logo_request_instance.to_dict()
# create an instance of LogoRequest from a dict
logo_request_from_dict = LogoRequest.from_dict(logo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


