# AiThreadMessageLikeContent
Message content: either plain text or a list of typed content parts (text, image, tool-call, …). Parts are open-ended by content type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.ai_thread_message_like_content import AiThreadMessageLikeContent

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadMessageLikeContent from a JSON string
ai_thread_message_like_content_instance = AiThreadMessageLikeContent.from_json(json)
# print the JSON string representation of the object
print(AiThreadMessageLikeContent.to_json())

# convert the object into a dict
ai_thread_message_like_content_dict = ai_thread_message_like_content_instance.to_dict()
# create an instance of AiThreadMessageLikeContent from a dict
ai_thread_message_like_content_from_dict = AiThreadMessageLikeContent.from_dict(ai_thread_message_like_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


