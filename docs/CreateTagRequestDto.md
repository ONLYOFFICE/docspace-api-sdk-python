# CreateTagRequestDto

The request parameters for creating a tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The tag name. | 

## Example

```python
from docspace.models.create_tag_request_dto import CreateTagRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTagRequestDto from a JSON string
create_tag_request_dto_instance = CreateTagRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateTagRequestDto.to_json())

# convert the object into a dict
create_tag_request_dto_dict = create_tag_request_dto_instance.to_dict()
# create an instance of CreateTagRequestDto from a dict
create_tag_request_dto_from_dict = CreateTagRequestDto.from_dict(create_tag_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


