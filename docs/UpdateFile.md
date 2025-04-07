# UpdateFile

Parameters for updating a file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | File title | [optional] 
**last_version** | **int** | Number of the latest file version | [optional] 

## Example

```python
from docspace.models.update_file import UpdateFile

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


