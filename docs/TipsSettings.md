# TipsSettings



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show** | **bool** | Specifies if the tips will be shown or not | [optional] 

## Example

```python
from docspace.models.tips_settings import TipsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TipsSettings from a JSON string
tips_settings_instance = TipsSettings.from_json(json)
# print the JSON string representation of the object
print(TipsSettings.to_json())

# convert the object into a dict
tips_settings_dict = tips_settings_instance.to_dict()
# create an instance of TipsSettings from a dict
tips_settings_from_dict = TipsSettings.from_dict(tips_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


