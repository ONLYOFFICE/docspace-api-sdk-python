# CreateFileJsonElementTemplateId
An existing file the new one copies its content from, as a number for a file in the portal and as a string for  one in a connected third-party storage; the caller has to be able to read it. Left out, a blank template for  the format and the language of the caller is used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.create_file_json_element_template_id import CreateFileJsonElementTemplateId

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileJsonElementTemplateId from a JSON string
create_file_json_element_template_id_instance = CreateFileJsonElementTemplateId.from_json(json)
# print the JSON string representation of the object
print(CreateFileJsonElementTemplateId.to_json())

# convert the object into a dict
create_file_json_element_template_id_dict = create_file_json_element_template_id_instance.to_dict()
# create an instance of CreateFileJsonElementTemplateId from a dict
create_file_json_element_template_id_from_dict = CreateFileJsonElementTemplateId.from_dict(create_file_json_element_template_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


