# FileLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filetype** | **str** | File type | [optional] 
**token** | **str** | Token | [optional] 
**url** | **str** | Url | [optional] 

## Example

```python
from docspace.models.file_link import FileLink

# TODO update the JSON string below
json = "{}"
# create an instance of FileLink from a JSON string
file_link_instance = FileLink.from_json(json)
# print the JSON string representation of the object
print(FileLink.to_json())

# convert the object into a dict
file_link_dict = file_link_instance.to_dict()
# create an instance of FileLink from a dict
file_link_from_dict = FileLink.from_dict(file_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


