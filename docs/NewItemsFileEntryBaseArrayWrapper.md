# NewItemsFileEntryBaseArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[NewItemsDtoFileEntryBaseDto]**](NewItemsDtoFileEntryBaseDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.new_items_file_entry_base_array_wrapper import NewItemsFileEntryBaseArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of NewItemsFileEntryBaseArrayWrapper from a JSON string
new_items_file_entry_base_array_wrapper_instance = NewItemsFileEntryBaseArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(NewItemsFileEntryBaseArrayWrapper.to_json())

# convert the object into a dict
new_items_file_entry_base_array_wrapper_dict = new_items_file_entry_base_array_wrapper_instance.to_dict()
# create an instance of NewItemsFileEntryBaseArrayWrapper from a dict
new_items_file_entry_base_array_wrapper_from_dict = NewItemsFileEntryBaseArrayWrapper.from_dict(new_items_file_entry_base_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


