# InfoConfigDto
The information config parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite** | **bool** | Specifies if the file is favorite or not. | [optional] 
**folder** | **str** | The folder of the file. | [optional] 
**owner** | **str** | The file owner. | [optional] 
**sharing_settings** | [**List[AceShortWrapper]**](AceShortWrapper.md) | The sharing settings of the file. | [optional] 
**type** | [**EditorType**](EditorType.md) |  | [optional] 
**uploaded** | **str** | The uploaded file. | [optional] 

## Example

```python
from docspace-api-python.models.info_config_dto import InfoConfigDto

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


