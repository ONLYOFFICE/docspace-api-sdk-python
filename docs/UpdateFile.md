# UpdateFile
The changes to make to a file: a new title, an earlier version to restore, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The new title of the file, without an extension - the stored extension is kept whatever the title says, so a  rename cannot change the format. Left empty, the file keeps its name. | [optional] 
**last_version** | **int** | The version to restore on top of the history, as reported by `GET api/2.0/files/file/{fileId}/history`; 0 or  less leaves the versions untouched. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_file import UpdateFile

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFile from a JSON string
update_file_instance = UpdateFile.from_json(json)
# print the JSON string representation of the object
print(UpdateFile.to_json())

# convert the object into a dict
update_file_dict = update_file_instance.to_dict()
# create an instance of UpdateFile from a dict
update_file_from_dict = UpdateFile.from_dict(update_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


