# BatchTagsRequestDto
The tag names a request attaches to a room or detaches from it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | The tags, by name: a tag has no identifier of its own, and the name is what links a room to it.  `GET api/2.0/files/tags` lists the names already in the portal catalogue. An empty list is accepted and does  nothing, while a blank or overlong entry makes the whole request invalid. | 

## Example

```python
from docspace_api_sdk.models.batch_tags_request_dto import BatchTagsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTagsRequestDto from a JSON string
batch_tags_request_dto_instance = BatchTagsRequestDto.from_json(json)
# print the JSON string representation of the object
print(BatchTagsRequestDto.to_json())

# convert the object into a dict
batch_tags_request_dto_dict = batch_tags_request_dto_instance.to_dict()
# create an instance of BatchTagsRequestDto from a dict
batch_tags_request_dto_from_dict = BatchTagsRequestDto.from_dict(batch_tags_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


