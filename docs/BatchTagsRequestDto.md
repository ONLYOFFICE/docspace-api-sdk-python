# BatchTagsRequestDto
The parameters for adding tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | The list of tag names. | [optional] 

## Example

```python
from docspace-api-sdk.models.batch_tags_request_dto import BatchTagsRequestDto

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


