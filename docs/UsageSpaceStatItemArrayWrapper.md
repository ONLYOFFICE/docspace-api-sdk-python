# UsageSpaceStatItemArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[UsageSpaceStatItemDto]**](UsageSpaceStatItemDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.usage_space_stat_item_array_wrapper import UsageSpaceStatItemArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of UsageSpaceStatItemArrayWrapper from a JSON string
usage_space_stat_item_array_wrapper_instance = UsageSpaceStatItemArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(UsageSpaceStatItemArrayWrapper.to_json())

# convert the object into a dict
usage_space_stat_item_array_wrapper_dict = usage_space_stat_item_array_wrapper_instance.to_dict()
# create an instance of UsageSpaceStatItemArrayWrapper from a dict
usage_space_stat_item_array_wrapper_from_dict = UsageSpaceStatItemArrayWrapper.from_dict(usage_space_stat_item_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


