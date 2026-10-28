# GroupMemberSecurityArrayWrapper
The successful API response containing the list of GroupMemberSecurityDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[GroupMemberSecurityDto]**](GroupMemberSecurityDto.md) | The list of GroupMemberSecurityDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.group_member_security_array_wrapper import GroupMemberSecurityArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberSecurityArrayWrapper from a JSON string
group_member_security_array_wrapper_instance = GroupMemberSecurityArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(GroupMemberSecurityArrayWrapper.to_json())

# convert the object into a dict
group_member_security_array_wrapper_dict = group_member_security_array_wrapper_instance.to_dict()
# create an instance of GroupMemberSecurityArrayWrapper from a dict
group_member_security_array_wrapper_from_dict = GroupMemberSecurityArrayWrapper.from_dict(group_member_security_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


