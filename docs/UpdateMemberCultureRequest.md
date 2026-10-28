# UpdateMemberCultureRequest
The culture name parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**culture_name** | **str** | The user culture name (en-US, de, fr, es, ...). | 

## Example

```python
from docspace_api_sdk.models.update_member_culture_request import UpdateMemberCultureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMemberCultureRequest from a JSON string
update_member_culture_request_instance = UpdateMemberCultureRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMemberCultureRequest.to_json())

# convert the object into a dict
update_member_culture_request_dict = update_member_culture_request_instance.to_dict()
# create an instance of UpdateMemberCultureRequest from a dict
update_member_culture_request_from_dict = UpdateMemberCultureRequest.from_dict(update_member_culture_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


