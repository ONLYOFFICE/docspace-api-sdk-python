# UpdateComment

Parameters for updating a comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | File version | [optional] 
**comment** | **str** | Comment text | [optional] 

## Example

```python
from docspace.models.update_comment import UpdateComment

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateComment from a JSON string
update_comment_instance = UpdateComment.from_json(json)
# print the JSON string representation of the object
print(UpdateComment.to_json())

# convert the object into a dict
update_comment_dict = update_comment_instance.to_dict()
# create an instance of UpdateComment from a dict
update_comment_from_dict = UpdateComment.from_dict(update_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


