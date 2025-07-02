# UsageSpaceStatItemDto
The parameters of the usage space statistics item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The item name. | [optional] 
**icon** | **str** | The item icon path. | [optional] 
**disabled** | **bool** | Specifies if the item is disabled or not. | [optional] 
**size** | **str** | The item used space. | [optional] 
**url** | **str** | The item URL. | [optional] 

## Example

```python
from docspace-api-python.models.usage_space_stat_item_dto import UsageSpaceStatItemDto

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


