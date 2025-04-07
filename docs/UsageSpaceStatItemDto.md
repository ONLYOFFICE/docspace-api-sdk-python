# UsageSpaceStatItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**icon** | **str** | Icon | [optional] 
**disabled** | **bool** | Specifies if the module space is disabled or not | [optional] 
**size** | **str** | Size | [optional] 
**url** | **str** | URL | [optional] 

## Example

```python
from docspace.models.usage_space_stat_item_dto import UsageSpaceStatItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of UsageSpaceStatItemDto from a JSON string
usage_space_stat_item_dto_instance = UsageSpaceStatItemDto.from_json(json)
# print the JSON string representation of the object
print(UsageSpaceStatItemDto.to_json())

# convert the object into a dict
usage_space_stat_item_dto_dict = usage_space_stat_item_dto_instance.to_dict()
# create an instance of UsageSpaceStatItemDto from a dict
usage_space_stat_item_dto_from_dict = UsageSpaceStatItemDto.from_dict(usage_space_stat_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


