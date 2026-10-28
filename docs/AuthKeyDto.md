# AuthKeyDto
One key of an authorization provider or a storage, with how the settings form shows it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The authorization key name. | 
**value** | **str** | The authorization key value. | 
**title** | **str** | The authorization key title. | [optional] 
**type** | **str** | The field type: text, password, select, toggle. | [optional] 
**options** | **List[str]** | The list of options for select type fields. | [optional] 
**depends_on** | **str** | The name of another key this field depends on for visibility. | [optional] 
**depends_on_value** | **str** | The value of the `dependsOn` key that makes this field visible. | [optional] 

## Example

```python
from docspace_api_sdk.models.auth_key_dto import AuthKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuthKeyDto from a JSON string
auth_key_dto_instance = AuthKeyDto.from_json(json)
# print the JSON string representation of the object
print(AuthKeyDto.to_json())

# convert the object into a dict
auth_key_dto_dict = auth_key_dto_instance.to_dict()
# create an instance of AuthKeyDto from a dict
auth_key_dto_from_dict = AuthKeyDto.from_dict(auth_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


