# CreateFolder
The title a folder is created with or renamed to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title the folder is given. It is trimmed before it is stored and may not be blank or consist of spaces  alone; it need not differ from the titles of the neighbouring folders, so the same title may appear twice in  one parent. | 

## Example

```python
from docspace_api_sdk.models.create_folder import CreateFolder

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


