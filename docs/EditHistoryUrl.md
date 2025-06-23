# EditHistoryUrl

The file editing history URL parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The document identifier of the previous version of the document. | [optional] 
**url** | **str** | The url address of the previous version of the document. | [optional] 
**file_type** | **str** | The document extension. | [optional] 

## Example

```python
from docspace.models.edit_history_url import EditHistoryUrl

# TODO update the JSON string below
json = "{}"
# create an instance of EditHistoryUrl from a JSON string
edit_history_url_instance = EditHistoryUrl.from_json(json)
# print the JSON string representation of the object
print(EditHistoryUrl.to_json())

# convert the object into a dict
edit_history_url_dict = edit_history_url_instance.to_dict()
# create an instance of EditHistoryUrl from a dict
edit_history_url_from_dict = EditHistoryUrl.from_dict(edit_history_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


