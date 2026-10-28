# CreateTagRequestDto
The parameters for adding a custom tag to the portal catalog of room tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tag to create, which is also its identity: tags are addressed by name everywhere, there is no  separate identifier. It is stored exactly as sent, spacing and case included, and a name that is already in  the catalog gives back that tag instead of a second one. | 

## Example

```python
from docspace_api_sdk.models.create_tag_request_dto import CreateTagRequestDto

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


