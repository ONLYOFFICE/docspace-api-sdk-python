# SaveFormRoleMappingDto
The people who are to fill in the roles of a PDF form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_id** | **int** | The PDF form the roles belong to. This is the value the operation reads, rather than the identifier in its  route, and the two are to be sent the same. | 
**roles** | [**List[FormRole]**](FormRole.md) | The roles with the account taking each of them and the sequence number that decides the turn: the same number  means the roles may be filled in parallel, different ones make a queue. The whole set is replaced on every  call, and an empty set resets the filling. | 

## Example

```python
from docspace_api_sdk.models.save_form_role_mapping_dto import SaveFormRoleMappingDto

# TODO update the JSON string below
json = "{}"
# create an instance of SaveFormRoleMappingDto from a JSON string
save_form_role_mapping_dto_instance = SaveFormRoleMappingDto.from_json(json)
# print the JSON string representation of the object
print(SaveFormRoleMappingDto.to_json())

# convert the object into a dict
save_form_role_mapping_dto_dict = save_form_role_mapping_dto_instance.to_dict()
# create an instance of SaveFormRoleMappingDto from a dict
save_form_role_mapping_dto_from_dict = SaveFormRoleMappingDto.from_dict(save_form_role_mapping_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


