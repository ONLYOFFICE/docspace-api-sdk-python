# CreateFolderRequest
The title a folder is created with or renamed to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title the folder is given. It is trimmed before it is stored and may not be blank or consist of spaces  alone; it need not differ from the titles of the neighbouring folders, so the same title may appear twice in  one parent. | 

## Example

```python
from docspace_api_sdk.models.create_folder_request import CreateFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolderRequest from a JSON string
create_folder_request_instance = CreateFolderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFolderRequest.to_json())

# convert the object into a dict
create_folder_request_dict = create_folder_request_instance.to_dict()
# create an instance of CreateFolderRequest from a dict
create_folder_request_from_dict = CreateFolderRequest.from_dict(create_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


