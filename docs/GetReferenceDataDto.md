# GetReferenceDataDto
The body of a spreadsheet reference request: the source spreadsheet, and the three ways of naming the document it  refers to, which are tried in the order they are described.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_key** | **str** | The id of the referenced file as the document service recorded it in the formula. It is tried first, and only  when `instanceId` names this portal. | 
**instance_id** | **str** | The portal the reference was made on, as the document service recorded it. Only the id of this portal makes  the file key resolvable; any other value falls through to the path and the link. | 
**source_file_id** | **int** | The spreadsheet the formula sits in. The path is resolved against it - the referenced file is looked for among  the files lying next to it - and it is the file whose read access is checked. | [optional] 
**path** | **str** | The title of the referenced file exactly as the formula spells it, matched against the files lying next to the  source file. It is tried after the file key, and only when no link is given. | [optional] 
**link** | **str** | The web address the formula points at, an editor link of this portal or one of its short links. It is tried  last, and an address belonging to another site is not resolved at all but handed back for the client to follow  as it is. | [optional] 

## Example

```python
from docspace_api_sdk.models.get_reference_data_dto import GetReferenceDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetReferenceDataDto from a JSON string
get_reference_data_dto_instance = GetReferenceDataDto.from_json(json)
# print the JSON string representation of the object
print(GetReferenceDataDto.to_json())

# convert the object into a dict
get_reference_data_dto_dict = get_reference_data_dto_instance.to_dict()
# create an instance of GetReferenceDataDto from a dict
get_reference_data_dto_from_dict = GetReferenceDataDto.from_dict(get_reference_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


