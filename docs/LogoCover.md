# LogoCover
The logo cover information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The logo cover ID. | [optional] 
**data** | **str** | The logo cover data. | [optional] 

## Example

```python
from docspace-api-python.models.logo_cover import LogoCover

# TODO update the JSON string below
json = "{}"
# create an instance of LogoCover from a JSON string
logo_cover_instance = LogoCover.from_json(json)
# print the JSON string representation of the object
print(LogoCover.to_json())

# convert the object into a dict
logo_cover_dict = logo_cover_instance.to_dict()
# create an instance of LogoCover from a dict
logo_cover_from_dict = LogoCover.from_dict(logo_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


