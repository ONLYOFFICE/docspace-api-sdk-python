# UpdatePhotoMemberRequest

Request parameters for updating user photo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **str** | Avatar photo URL | [optional] 

## Example

```python
from docspace.models.update_photo_member_request import UpdatePhotoMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePhotoMemberRequest from a JSON string
update_photo_member_request_instance = UpdatePhotoMemberRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePhotoMemberRequest.to_json())

# convert the object into a dict
update_photo_member_request_dict = update_photo_member_request_instance.to_dict()
# create an instance of UpdatePhotoMemberRequest from a dict
update_photo_member_request_from_dict = UpdatePhotoMemberRequest.from_dict(update_photo_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


