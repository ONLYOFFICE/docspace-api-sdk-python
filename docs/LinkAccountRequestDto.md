# LinkAccountRequestDto
The request parameters for linking accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serialized_profile** | **str** | The profile a completed provider authorization produced, in the serialized form the login flow hands back.  Pass that value unchanged; it carries the provider, the third-party account ID and the authorization result,  and a hand-written object is not accepted. | [optional] 

## Example

```python
from docspace_api_sdk.models.link_account_request_dto import LinkAccountRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of LinkAccountRequestDto from a JSON string
link_account_request_dto_instance = LinkAccountRequestDto.from_json(json)
# print the JSON string representation of the object
print(LinkAccountRequestDto.to_json())

# convert the object into a dict
link_account_request_dto_dict = link_account_request_dto_instance.to_dict()
# create an instance of LinkAccountRequestDto from a dict
link_account_request_dto_from_dict = LinkAccountRequestDto.from_dict(link_account_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


