# InfoConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite** | **bool** | Favorite | [optional] 
**folder** | **str** | Folder | [optional] 
**owner** | **str** | Owner | [optional] 
**sharing_settings** | [**List[AceShortWrapper]**](AceShortWrapper.md) | Sharing settings | [optional] 
**type** | [**EditorType**](EditorType.md) |  | [optional] 
**uploaded** | **str** | Uploaded | [optional] 

## Example

```python
from docspace.models.info_config_dto import InfoConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of InfoConfigDto from a JSON string
info_config_dto_instance = InfoConfigDto.from_json(json)
# print the JSON string representation of the object
print(InfoConfigDto.to_json())

# convert the object into a dict
info_config_dto_dict = info_config_dto_instance.to_dict()
# create an instance of InfoConfigDto from a dict
info_config_dto_from_dict = InfoConfigDto.from_dict(info_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


