# UpdateTagRequestDto
The parameters for renaming a custom room tag in the portal catalog.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The name of the tag to rename, matched against the catalog exactly as it is stored rather than searched for.  Read the stored spelling from `GET api/2.0/files/tags`. | 
**new_name** | **str** | The name to store instead. It has to be free: names are unique across the portal, so a name another tag  already carries is refused, and merging two tags this way is not possible. | 

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


