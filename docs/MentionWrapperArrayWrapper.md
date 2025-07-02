# MentionWrapperArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[MentionWrapper]**](MentionWrapper.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MentionWrapperArrayWrapper from a JSON string
mention_wrapper_array_wrapper_instance = MentionWrapperArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(MentionWrapperArrayWrapper.to_json())

# convert the object into a dict
mention_wrapper_array_wrapper_dict = mention_wrapper_array_wrapper_instance.to_dict()
# create an instance of MentionWrapperArrayWrapper from a dict
mention_wrapper_array_wrapper_from_dict = MentionWrapperArrayWrapper.from_dict(mention_wrapper_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


