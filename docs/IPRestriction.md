# IPRestriction
The IP restiction parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IP address. | 
**for_admin** | **bool** | Specifies if the IP address is for administrator users only or not. | [optional] 
**id** | **int** | The IP restiction ID. | [optional] 
**tenant_id** | **int** | The tenant ID. | [optional] 

## Example

```python
from docspace_api_sdk.models.ip_restriction import IPRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of IPRestriction from a JSON string
ip_restriction_instance = IPRestriction.from_json(json)
# print the JSON string representation of the object
print(IPRestriction.to_json())

# convert the object into a dict
ip_restriction_dict = ip_restriction_instance.to_dict()
# create an instance of IPRestriction from a dict
ip_restriction_from_dict = IPRestriction.from_dict(ip_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


