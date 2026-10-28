# GroupArrayWrapper
The successful API response containing the list of GroupDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[GroupDto]**](GroupDto.md) | The list of GroupDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of GroupArrayWrapper from a JSON string
group_array_wrapper_instance = GroupArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(GroupArrayWrapper.to_json())

# convert the object into a dict
group_array_wrapper_dict = group_array_wrapper_instance.to_dict()
# create an instance of GroupArrayWrapper from a dict
group_array_wrapper_from_dict = GroupArrayWrapper.from_dict(group_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


