# SetPublicDto
The public access to set on a room template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier of the room template. Take it from `templateId` of `GET api/2.0/files/roomtemplate/status`, or  from the folder list of `GET api/2.0/files/rooms` called with `searchArea` set to 4; an identifier of an  ordinary room is not accepted. | 
**public** | **bool** | Whether the Everyone group keeps read access to the template. True shares it with every member allowed to  create rooms; false leaves it reachable only for its owner. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_public_dto import SetPublicDto

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


