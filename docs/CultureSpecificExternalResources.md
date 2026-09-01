# CultureSpecificExternalResources
The external resources settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the product API. | [optional] 
**common** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the common product information. | [optional] 
**forum** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the forum. | [optional] 
**helpcenter** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the Help Center. | [optional] 
**integrations** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the product integrations. | [optional] 
**site** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the product website. | [optional] 
**social_networks** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the product social nerworks. | [optional] 
**support** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the product support. | [optional] 
**videoguides** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) | The link to the video guides. | [optional] 

## Example

```python
from docspace_api_sdk.models.culture_specific_external_resources import CultureSpecificExternalResources

# TODO update the JSON string below
json = "{}"
# create an instance of CultureSpecificExternalResources from a JSON string
culture_specific_external_resources_instance = CultureSpecificExternalResources.from_json(json)
# print the JSON string representation of the object
print(CultureSpecificExternalResources.to_json())

# convert the object into a dict
culture_specific_external_resources_dict = culture_specific_external_resources_instance.to_dict()
# create an instance of CultureSpecificExternalResources from a dict
culture_specific_external_resources_from_dict = CultureSpecificExternalResources.from_dict(culture_specific_external_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


