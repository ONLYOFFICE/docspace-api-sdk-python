# FileShareParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_to** | **str** | ID of the user with whom we want to share a file | [optional] 
**email** | **str** | User email address | [optional] 
**access** | [**FileShare**](FileShare.md) |  | [optional] 

## Example

```python
from docspace.models.file_share_params import FileShareParams

# TODO update the JSON string below
json = "{}"
# create an instance of FileShareParams from a JSON string
file_share_params_instance = FileShareParams.from_json(json)
# print the JSON string representation of the object
print(FileShareParams.to_json())

# convert the object into a dict
file_share_params_dict = file_share_params_instance.to_dict()
# create an instance of FileShareParams from a dict
file_share_params_from_dict = FileShareParams.from_dict(file_share_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


