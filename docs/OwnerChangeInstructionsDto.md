# OwnerChangeInstructionsDto
The outcome of asking for the portal-ownership transfer letter to be sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Whether the letter was sent: `1` that it was, `0` that the request was turned down. A refusal comes back  with HTTP 200, so this field and not the status code is what says whether anything happened - the request  is turned down when the caller is not the portal owner and when the named member is unknown or inactive. | [optional] 
**message** | **str** | The outcome spelled out in the portal language. On success it names the address the letter went to, and it  carries an HTML `mailto:` anchor rather than plain text, so it has to be rendered as markup or stripped;  on a refusal it is the localised reason. | [optional] 

## Example

```python
from docspace_api_sdk.models.owner_change_instructions_dto import OwnerChangeInstructionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerChangeInstructionsDto from a JSON string
owner_change_instructions_dto_instance = OwnerChangeInstructionsDto.from_json(json)
# print the JSON string representation of the object
print(OwnerChangeInstructionsDto.to_json())

# convert the object into a dict
owner_change_instructions_dto_dict = owner_change_instructions_dto_instance.to_dict()
# create an instance of OwnerChangeInstructionsDto from a dict
owner_change_instructions_dto_from_dict = OwnerChangeInstructionsDto.from_dict(owner_change_instructions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


