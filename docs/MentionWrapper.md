# MentionWrapper
The parameters of a user mentioned in a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserInfo**](UserInfo.md) |  | [optional] 
**email** | **str** | The user email address. | [optional] [readonly] 
**id** | **str** | The user unique identification. | [optional] [readonly] 
**image** | **str** | The path to the user&#39;s avatar. | [optional] [readonly] 
**has_access** | **bool** | Specifies whether the user has the access to the file where they are mentioned. | [optional] [readonly] 
**name** | **str** | The user full name. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.mention_wrapper import MentionWrapper

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


