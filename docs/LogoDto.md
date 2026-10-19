# LogoDto
The room logo information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** | The original logo. | 
**large** | **str** | The large logo. | 
**medium** | **str** | The medium logo. | 
**small** | **str** | The small logo. | 
**color** | **str** | The logo color. | [optional] 
**cover** | [**LogoCoverDto**](LogoCoverDto.md) | The logo cover. | [optional] 

## Example

```python
from docspace_api_sdk.models.logo_dto import LogoDto

# TODO update the JSON string below
json = "{}"
# create an instance of LogoDto from a JSON string
logo_dto_instance = LogoDto.from_json(json)
# print the JSON string representation of the object
print(LogoDto.to_json())

# convert the object into a dict
logo_dto_dict = logo_dto_instance.to_dict()
# create an instance of LogoDto from a dict
logo_dto_from_dict = LogoDto.from_dict(logo_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


