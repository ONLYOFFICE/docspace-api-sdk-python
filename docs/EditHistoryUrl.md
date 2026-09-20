# EditHistoryUrl
The address, document key and format of the revision a comparison is made against.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The document key of that revision. When the file has no earlier revision the portal generates a fresh key for  the template it falls back to, so the value is not always one an earlier revision ever had. | [optional] 
**url** | **str** | The address that revision's content is served from. It is meant for the editing service and carries its own  key, which is valid for a limited time. | [optional] 
**file_type** | **str** | The format of that revision, as an extension without the leading dot. | [optional] 

## Example

```python
from docspace_api_sdk.models.edit_history_url import EditHistoryUrl

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


