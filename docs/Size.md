# Size
Represents dimensions with width and height values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | Gets or sets the height dimension of an object, typically measured in pixels or other unit.  It defines the vertical size of the object. | [optional] 
**width** | **int** | Gets or sets the width dimension of an object, typically measured in pixels or other unit. | [optional] 

## Example

```python
from docspace_api_sdk.models.size import Size

# TODO update the JSON string below
json = "{}"
# create an instance of Size from a JSON string
size_instance = Size.from_json(json)
# print the JSON string representation of the object
print(Size.to_json())

# convert the object into a dict
size_dict = size_instance.to_dict()
# create an instance of Size from a dict
size_from_dict = Size.from_dict(size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


