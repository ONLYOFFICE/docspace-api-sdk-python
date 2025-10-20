# FileLink
The file link properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filetype** | **str** | The type of the file for the source viewed or edited document. | 
**token** | **str** | The encrypted signature added to the config in the form of a token. | [optional] 
**url** | **str** | The absolute URL where the source viewed or edited document is stored. | 

## Example

```python
from docspace_api_sdk.models.file_link import FileLink

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


