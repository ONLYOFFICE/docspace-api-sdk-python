# CultureSpecificExternalResources
The external resources settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 
**common** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 
**forum** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 
**helpcenter** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 
**integrations** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 
**site** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 
**social_networks** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 
**support** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 
**videoguides** | [**CultureSpecificExternalResource**](CultureSpecificExternalResource.md) |  | [optional] 

## Example

```python
from docspace-api-python.models.culture_specific_external_resources import CultureSpecificExternalResources

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


