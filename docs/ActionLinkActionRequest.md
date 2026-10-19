# ActionLinkActionRequest
An anchor inside a document, as the editor writes it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The anchor value produced by the editor, opaque to the portal: it names the comment, the mention or the  place the document is scrolled to. | [optional] 
**type** | **str** | What the anchor points at, as the editor names it - a comment thread, for instance. | [optional] 

## Example

```python
from docspace_api_sdk.models.action_link_action_request import ActionLinkActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionLinkActionRequest from a JSON string
action_link_action_request_instance = ActionLinkActionRequest.from_json(json)
# print the JSON string representation of the object
print(ActionLinkActionRequest.to_json())

# convert the object into a dict
action_link_action_request_dict = action_link_action_request_instance.to_dict()
# create an instance of ActionLinkActionRequest from a dict
action_link_action_request_from_dict = ActionLinkActionRequest.from_dict(action_link_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


