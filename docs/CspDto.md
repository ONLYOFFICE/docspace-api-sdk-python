# CspDto
The Content Security Policy of the portal: the domains an administrator allowed, and the header built from them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | The external hosts an administrator has allowed, each in the form it was saved in - a bare host, a host  with a scheme, or a wildcard such as `*.example.com`. An empty list means nobody has added one, not that  the portal serves no policy. | 
**header** | **str** | The complete policy value the portal sends to browsers, assembled from `domains` together with the  portal's own sources and the integrations it has switched on. It is therefore wider than `domains` alone,  and is filled in even while that list is empty. | 

## Example

```python
from docspace_api_sdk.models.csp_dto import CspDto

# TODO update the JSON string below
json = "{}"
# create an instance of CspDto from a JSON string
csp_dto_instance = CspDto.from_json(json)
# print the JSON string representation of the object
print(CspDto.to_json())

# convert the object into a dict
csp_dto_dict = csp_dto_instance.to_dict()
# create an instance of CspDto from a dict
csp_dto_from_dict = CspDto.from_dict(csp_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


