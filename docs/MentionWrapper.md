# MentionWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserInfo**](UserInfo.md) |  | [optional] 
**email** | **str** | User email | [optional] [readonly] 
**id** | **str** | User ID | [optional] [readonly] 
**image** | **str** | User image | [optional] [readonly] 
**has_access** | **bool** | Specifies if the user has the access to the file or not | [optional] [readonly] 
**name** | **str** | User display name | [optional] [readonly] 

## Example

```python
from docspace.models.mention_wrapper import MentionWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MentionWrapper from a JSON string
mention_wrapper_instance = MentionWrapper.from_json(json)
# print the JSON string representation of the object
print(MentionWrapper.to_json())

# convert the object into a dict
mention_wrapper_dict = mention_wrapper_instance.to_dict()
# create an instance of MentionWrapper from a dict
mention_wrapper_from_dict = MentionWrapper.from_dict(mention_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


