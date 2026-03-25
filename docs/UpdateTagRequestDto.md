# UpdateTagRequestDto
The request parameters for creating a tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The old tag name. | 
**new_name** | **str** | The new tag name. | 

## Example

```python
from docspace_api_sdk.models.update_tag_request_dto import UpdateTagRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTagRequestDto from a JSON string
update_tag_request_dto_instance = UpdateTagRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateTagRequestDto.to_json())

# convert the object into a dict
update_tag_request_dto_dict = update_tag_request_dto_instance.to_dict()
# create an instance of UpdateTagRequestDto from a dict
update_tag_request_dto_from_dict = UpdateTagRequestDto.from_dict(update_tag_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


