# MentionMessageWrapper
The mention message parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_link** | [**ActionLinkConfig**](ActionLinkConfig.md) |  | [optional] 
**emails** | **List[str]** | A list of emails which will receive the mention message. | [optional] 
**message** | **str** | The comment message. | [optional] 

## Example

```python
from docspace_api_sdk.models.mention_message_wrapper import MentionMessageWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MentionMessageWrapper from a JSON string
mention_message_wrapper_instance = MentionMessageWrapper.from_json(json)
# print the JSON string representation of the object
print(MentionMessageWrapper.to_json())

# convert the object into a dict
mention_message_wrapper_dict = mention_message_wrapper_instance.to_dict()
# create an instance of MentionMessageWrapper from a dict
mention_message_wrapper_from_dict = MentionMessageWrapper.from_dict(mention_message_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


