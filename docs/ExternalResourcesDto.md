# ExternalResourcesDto
The external resources settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_panel** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the administration panel. It is returned only to the full administrators of a licensed (Enterprise) server (standalone) portal. | [optional] 
**api** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the product API. | [optional] 
**common** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the common product information. | [optional] 
**forum** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the forum. | [optional] 
**helpcenter** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the Help Center. | [optional] 
**integrations** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the product integrations. | [optional] 
**site** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the product website. | [optional] 
**social_networks** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the product social nerworks. | [optional] 
**support** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the product support. | [optional] 
**videoguides** | [**ExternalResourceDto**](ExternalResourceDto.md) | The link to the video guides. | [optional] 

## Example

```python
from docspace_api_sdk.models.external_resources_dto import ExternalResourcesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalResourcesDto from a JSON string
external_resources_dto_instance = ExternalResourcesDto.from_json(json)
# print the JSON string representation of the object
print(ExternalResourcesDto.to_json())

# convert the object into a dict
external_resources_dto_dict = external_resources_dto_instance.to_dict()
# create an instance of ExternalResourcesDto from a dict
external_resources_dto_from_dict = ExternalResourcesDto.from_dict(external_resources_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


