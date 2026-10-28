# CspRequestDto
The external sources the portal Content Security Policy is to trust.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | The domains the policy trusts, as the complete list that is to hold afterwards rather than a list of  additions: send the domains already trusted together with the new one to add one, leave one out to withdraw  it, and send an empty list to fall back to the portal built-in policy. An entry may be a bare host, a host  with a scheme, or a wildcard host such as `*.example.com`; it has to form a valid absolute address and may  contain ASCII characters only. Every entry becomes an allowed source for scripts, styles, images, fonts,  frames, media and connections at once - the directives cannot be set apart here. | [optional] 

## Example

```python
from docspace_api_sdk.models.csp_request_dto import CspRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CspRequestDto from a JSON string
csp_request_dto_instance = CspRequestDto.from_json(json)
# print the JSON string representation of the object
print(CspRequestDto.to_json())

# convert the object into a dict
csp_request_dto_dict = csp_request_dto_instance.to_dict()
# create an instance of CspRequestDto from a dict
csp_request_dto_from_dict = CspRequestDto.from_dict(csp_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


