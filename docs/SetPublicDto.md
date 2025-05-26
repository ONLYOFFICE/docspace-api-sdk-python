# SetPublicDto

The public settings of the room template to set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The room template ID. | 
**public** | **bool** | Specifies whether the room template is public or not. | [optional] 

## Example

```python
from docspace.models.set_public_dto import SetPublicDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetPublicDto from a JSON string
set_public_dto_instance = SetPublicDto.from_json(json)
# print the JSON string representation of the object
print(SetPublicDto.to_json())

# convert the object into a dict
set_public_dto_dict = set_public_dto_instance.to_dict()
# create an instance of SetPublicDto from a dict
set_public_dto_from_dict = SetPublicDto.from_dict(set_public_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


