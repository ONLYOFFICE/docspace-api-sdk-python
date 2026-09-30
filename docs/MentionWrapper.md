# MentionWrapper
A user the editor may offer: to be mentioned in a comment, or to be picked when protecting a document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserInfo**](UserInfo.md) | The account itself, in the shape the people listings use. | [optional] 
**email** | **str** | Where a mention notification for this user is delivered. | [optional] [readonly] 
**id** | **str** | The account id as text, the same value the account object carries; it is what identifies the user in a sharing  request built from this list. | [optional] [readonly] 
**image** | **str** | An absolute address of the medium-sized avatar. A generated default avatar is reported when the user never  uploaded one, so the field is never empty. | [optional] [readonly] 
**has_access** | **bool** | Not filled in by the operations that return this list: it always comes back false. Whether a user can already  open the document has to be read from the sharing settings of the file. | [optional] [readonly] 
**name** | **str** | The name to display, assembled the way the portal is configured to show names. | [optional] [readonly] 

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


