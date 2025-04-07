# LogoRequest

Logo request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tmp_file** | **str** | The path to the temporary image file | [optional] 
**x** | **int** | The X coordinate of the rectangle starting point | [optional] 
**y** | **int** | The Y coordinate of the rectangle starting point | [optional] 
**width** | **int** | The rectangle width | [optional] 
**height** | **int** | The rectangle height | [optional] 

## Example

```python
from docspace.models.logo_request import LogoRequest

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


