# CreateFolder

The parameters for creating a folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The folder title to create. | 

## Example

```python
from docspace.models.create_folder import CreateFolder

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolder from a JSON string
create_folder_instance = CreateFolder.from_json(json)
# print the JSON string representation of the object
print(CreateFolder.to_json())

# convert the object into a dict
create_folder_dict = create_folder_instance.to_dict()
# create an instance of CreateFolder from a dict
create_folder_from_dict = CreateFolder.from_dict(create_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


