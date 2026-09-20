# InfoConfigDto
The facts the editor information panel shows about the open document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite** | **bool** | Whether the caller has this document among their favorites. It is empty when favorites do not apply - for an  anonymous caller, for a guest, and for an encrypted document. | [optional] 
**folder** | **str** | The place of the document as a readable path, its folders joined from the root downwards. It is empty in the  embedded layout, which shows no such panel. | [optional] 
**owner** | **str** | The display name of the owner of the document. It is empty for an anonymous session. | [optional] 
**sharing_settings** | [**List[AceShortWrapper]**](AceShortWrapper.md) | Who the document is shared with, as the information panel lists it. An empty list means it is shared with  nobody beyond its owner. | [optional] 
**type** | [**EditorType**](EditorType.md) | The layout the information panel is rendered for. | [optional] 
**uploaded** | **str** | When the document was created on the portal, already formatted for reading in the culture of the caller rather  than as a machine timestamp. | [optional] 

## Example

```python
from docspace_api_sdk.models.info_config_dto import InfoConfigDto

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


