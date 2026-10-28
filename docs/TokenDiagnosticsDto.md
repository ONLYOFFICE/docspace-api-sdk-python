# TokenDiagnosticsDto
What the current token carries, for diagnostics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the authenticated identity. | [optional] 
**claims** | **List[str]** | The claims of the identity, each formatted as type:value. | [optional] 

## Example

```python
from docspace_api_sdk.models.token_diagnostics_dto import TokenDiagnosticsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TokenDiagnosticsDto from a JSON string
token_diagnostics_dto_instance = TokenDiagnosticsDto.from_json(json)
# print the JSON string representation of the object
print(TokenDiagnosticsDto.to_json())

# convert the object into a dict
token_diagnostics_dto_dict = token_diagnostics_dto_instance.to_dict()
# create an instance of TokenDiagnosticsDto from a dict
token_diagnostics_dto_from_dict = TokenDiagnosticsDto.from_dict(token_diagnostics_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


