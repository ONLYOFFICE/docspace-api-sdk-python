# InvitationLinkWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**InvitationLinkDto**](InvitationLinkDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.invitation_link_wrapper import InvitationLinkWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationLinkWrapper from a JSON string
invitation_link_wrapper_instance = InvitationLinkWrapper.from_json(json)
# print the JSON string representation of the object
print(InvitationLinkWrapper.to_json())

# convert the object into a dict
invitation_link_wrapper_dict = invitation_link_wrapper_instance.to_dict()
# create an instance of InvitationLinkWrapper from a dict
invitation_link_wrapper_from_dict = InvitationLinkWrapper.from_dict(invitation_link_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


