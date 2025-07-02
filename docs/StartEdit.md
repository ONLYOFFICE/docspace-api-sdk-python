# StartEdit
The parameters for starting file editing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editing_alone** | **bool** | Specifies whether to share the file with other users for editing or not. | [optional] 

## Example

```python
from docspace-api-python.models.start_edit import StartEdit

# TODO update the JSON string below
json = "{}"
# create an instance of StartEdit from a JSON string
start_edit_instance = StartEdit.from_json(json)
# print the JSON string representation of the object
print(StartEdit.to_json())

# convert the object into a dict
start_edit_dict = start_edit_instance.to_dict()
# create an instance of StartEdit from a dict
start_edit_from_dict = StartEdit.from_dict(start_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


