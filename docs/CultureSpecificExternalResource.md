# CultureSpecificExternalResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**entries** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from docspace.models.culture_specific_external_resource import CultureSpecificExternalResource

# TODO update the JSON string below
json = "{}"
# create an instance of CultureSpecificExternalResource from a JSON string
culture_specific_external_resource_instance = CultureSpecificExternalResource.from_json(json)
# print the JSON string representation of the object
print(CultureSpecificExternalResource.to_json())

# convert the object into a dict
culture_specific_external_resource_dict = culture_specific_external_resource_instance.to_dict()
# create an instance of CultureSpecificExternalResource from a dict
culture_specific_external_resource_from_dict = CultureSpecificExternalResource.from_dict(culture_specific_external_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


