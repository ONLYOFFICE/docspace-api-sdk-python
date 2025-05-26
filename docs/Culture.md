# Culture

The culture code parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**culture_name** | **str** | The user language. | [optional] 

## Example

```python
from docspace.models.culture import Culture

# TODO update the JSON string below
json = "{}"
# create an instance of Culture from a JSON string
culture_instance = Culture.from_json(json)
# print the JSON string representation of the object
print(Culture.to_json())

# convert the object into a dict
culture_dict = culture_instance.to_dict()
# create an instance of Culture from a dict
culture_from_dict = Culture.from_dict(culture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


