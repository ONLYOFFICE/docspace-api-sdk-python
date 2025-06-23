# LogoConfigDto

The logo config parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | The image of the logo. | [optional] 
**image_dark** | **str** | The dark image of the logo. | [optional] 
**image_embedded** | **str** | The embedded image of the logo. | [optional] 
**url** | **str** | The url link of the logo. | [optional] 
**visible** | **bool** | Specifies if the logo is visible. | [optional] 

## Example

```python
from docspace.models.logo_config_dto import LogoConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of LogoConfigDto from a JSON string
logo_config_dto_instance = LogoConfigDto.from_json(json)
# print the JSON string representation of the object
print(LogoConfigDto.to_json())

# convert the object into a dict
logo_config_dto_dict = logo_config_dto_instance.to_dict()
# create an instance of LogoConfigDto from a dict
logo_config_dto_from_dict = LogoConfigDto.from_dict(logo_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


