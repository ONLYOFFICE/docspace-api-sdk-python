# GroupArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[GroupDto]**](GroupDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.group_array_wrapper import GroupArrayWrapper

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


