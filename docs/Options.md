# Options

The document options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watermark_on_draw** | [**WatermarkOnDraw**](WatermarkOnDraw.md) |  | [optional] 

## Example

```python
from docspace.models.options import Options

# TODO update the JSON string below
json = "{}"
# create an instance of Options from a JSON string
options_instance = Options.from_json(json)
# print the JSON string representation of the object
print(Options.to_json())

# convert the object into a dict
options_dict = options_instance.to_dict()
# create an instance of Options from a dict
options_from_dict = Options.from_dict(options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


