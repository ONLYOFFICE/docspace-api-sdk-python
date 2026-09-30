# LogoConfigDto
The logo the editor shows, resolved for the file type and the layout of this opening.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | The logo for the current layout and file type, as the portal branding defines it. | [optional] 
**image_dark** | **str** | The variant for a dark interface theme. | [optional] 
**image_light** | **str** | The variant for a light interface theme. | [optional] 
**image_embedded** | **str** | The variant for the framed viewer. It is empty in every layout but the embedded one. | [optional] 
**url** | **str** | Where clicking the logo takes the user. | [optional] 
**visible** | **bool** | Whether the logo is shown at all; the mobile layout hides it. | [optional] 

## Example

```python
from docspace_api_sdk.models.logo_config_dto import LogoConfigDto

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


