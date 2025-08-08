# GroupWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GroupDto**](GroupDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.group_wrapper import GroupWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of GroupWrapper from a JSON string
group_wrapper_instance = GroupWrapper.from_json(json)
# print the JSON string representation of the object
print(GroupWrapper.to_json())

# convert the object into a dict
group_wrapper_dict = group_wrapper_instance.to_dict()
# create an instance of GroupWrapper from a dict
group_wrapper_from_dict = GroupWrapper.from_dict(group_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


