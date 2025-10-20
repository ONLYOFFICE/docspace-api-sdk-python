# CspDto
The CSP (Content Security Policy) parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | The list of CSP domains. | 
**header** | **str** | The CSP header. | 

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


