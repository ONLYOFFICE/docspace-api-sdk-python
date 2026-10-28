# UpdateCommentRequest
The comment to store on one version of a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The version the comment belongs to, as reported by `GET api/2.0/files/file/{fileId}/edit/history`. A version  that does not exist is rejected as an invalid request. | 
**comment** | **str** | The note that explains what changed in that version, as the version history shows it. An empty text clears the  note, and a longer one is cut rather than refused, so read the stored text from the answer. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_comment_request import UpdateCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommentRequest from a JSON string
update_comment_request_instance = UpdateCommentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCommentRequest.to_json())

# convert the object into a dict
update_comment_request_dict = update_comment_request_instance.to_dict()
# create an instance of UpdateCommentRequest from a dict
update_comment_request_from_dict = UpdateCommentRequest.from_dict(update_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


