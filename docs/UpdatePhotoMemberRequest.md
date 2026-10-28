# UpdatePhotoMemberRequest
The request parameters for updating a photo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **str** | The address the portal downloads the new avatar from. It has to be absolute or relative to the portal, and it  has to use HTTPS unless the request itself came over HTTP; an address the portal refuses to fetch is rejected.  It is required - an empty value is answered with 400 rather than clearing the avatar. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_photo_member_request import UpdatePhotoMemberRequest

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


