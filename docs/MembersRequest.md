# MembersRequest

Group request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | List of group member IDs | [optional] 

## Example

```python
from docspace.models.members_request import MembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MembersRequest from a JSON string
members_request_instance = MembersRequest.from_json(json)
# print the JSON string representation of the object
print(MembersRequest.to_json())

# convert the object into a dict
members_request_dict = members_request_instance.to_dict()
# create an instance of MembersRequest from a dict
members_request_from_dict = MembersRequest.from_dict(members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


