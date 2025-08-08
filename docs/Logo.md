# Logo
The room logo information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** | The original logo. | [optional] 
**large** | **str** | The large logo. | [optional] 
**medium** | **str** | The medium logo. | [optional] 
**small** | **str** | The small logo. | [optional] 
**color** | **str** | The logo color. | [optional] 
**cover** | [**LogoCover**](LogoCover.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.logo import Logo

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


