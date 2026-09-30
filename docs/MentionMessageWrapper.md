# MentionMessageWrapper
The mention notification to send: what to say, whom to tell and where in the document the mention sits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_link** | [**ActionLinkConfig**](ActionLinkConfig.md) | The place in the document the notification link should open at, as the editor reports it when the mention is  made. Left out, the link opens the file at its beginning. | [optional] 
**emails** | **List[str]** | The addresses to notify. Only an address that belongs to a portal account receives a mail; an unknown address  is skipped, and the answer then carries the access list of the file so that the client can invite its owner. | [optional] 
**message** | **str** | The note shown next to the link in the mail. Only its first 200 characters are sent, and a value longer than  the field allows is refused. | [optional] 

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


