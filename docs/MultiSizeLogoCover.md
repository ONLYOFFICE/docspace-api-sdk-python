# MultiSizeLogoCover

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The logo cover ID. | 
**data** | **Dict[str, Optional[str]]** | The logo cover data. | 

## Example

```python
from docspace_api_sdk.models.multi_size_logo_cover import MultiSizeLogoCover

# TODO update the JSON string below
json = "{}"
# create an instance of MultiSizeLogoCover from a JSON string
multi_size_logo_cover_instance = MultiSizeLogoCover.from_json(json)
# print the JSON string representation of the object
print(MultiSizeLogoCover.to_json())

# convert the object into a dict
multi_size_logo_cover_dict = multi_size_logo_cover_instance.to_dict()
# create an instance of MultiSizeLogoCover from a dict
multi_size_logo_cover_from_dict = MultiSizeLogoCover.from_dict(multi_size_logo_cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


