# RecentConfigDto
One entry of the recent-documents list the editor offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | The folder shown next to the entry, as a readable name rather than an id. | [optional] 
**title** | **str** | The name shown for the entry. | [optional] 
**url** | **str** | Where the entry opens. | [optional] 

## Example

```python
from docspace_api_sdk.models.recent_config_dto import RecentConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of RecentConfigDto from a JSON string
recent_config_dto_instance = RecentConfigDto.from_json(json)
# print the JSON string representation of the object
print(RecentConfigDto.to_json())

# convert the object into a dict
recent_config_dto_dict = recent_config_dto_instance.to_dict()
# create an instance of RecentConfigDto from a dict
recent_config_dto_from_dict = RecentConfigDto.from_dict(recent_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


