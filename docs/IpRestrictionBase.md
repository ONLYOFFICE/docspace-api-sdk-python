# IpRestrictionBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**for_admin** | **bool** |  | [optional] 

## Example

```python
from docspace-api-python.models.ip_restriction_base import IpRestrictionBase

# TODO update the JSON string below
json = "{}"
# create an instance of IpRestrictionBase from a JSON string
ip_restriction_base_instance = IpRestrictionBase.from_json(json)
# print the JSON string representation of the object
print(IpRestrictionBase.to_json())

# convert the object into a dict
ip_restriction_base_dict = ip_restriction_base_instance.to_dict()
# create an instance of IpRestrictionBase from a dict
ip_restriction_base_from_dict = IpRestrictionBase.from_dict(ip_restriction_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


