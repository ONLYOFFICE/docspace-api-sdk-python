# Logo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** | Original | [optional] 
**large** | **str** | Large | [optional] 
**medium** | **str** | Medium | [optional] 
**small** | **str** | Small | [optional] 
**color** | **str** | Color | [optional] 
**cover** | [**LogoCover**](LogoCover.md) |  | [optional] 

## Example

```python
from docspace.models.logo import Logo

# TODO update the JSON string below
json = "{}"
# create an instance of Logo from a JSON string
logo_instance = Logo.from_json(json)
# print the JSON string representation of the object
print(Logo.to_json())

# convert the object into a dict
logo_dict = logo_instance.to_dict()
# create an instance of Logo from a dict
logo_from_dict = Logo.from_dict(logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


