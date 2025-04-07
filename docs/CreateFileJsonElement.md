# CreateFileJsonElement

Parameters for creating a file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | File title | [optional] 
**template_id** | [**CreateFileJsonElementTemplateId**](CreateFileJsonElementTemplateId.md) |  | [optional] 
**enable_external_ext** | **bool** | Specifies whether to allow the creation of external extension files or not | [optional] 
**form_id** | **int** | Form ID | [optional] 

## Example

```python
from docspace.models.create_file_json_element import CreateFileJsonElement

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileJsonElement from a JSON string
create_file_json_element_instance = CreateFileJsonElement.from_json(json)
# print the JSON string representation of the object
print(CreateFileJsonElement.to_json())

# convert the object into a dict
create_file_json_element_dict = create_file_json_element_instance.to_dict()
# create an instance of CreateFileJsonElement from a dict
create_file_json_element_from_dict = CreateFileJsonElement.from_dict(create_file_json_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


