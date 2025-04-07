# CspRequestsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | Domains | [optional] 

## Example

```python
from docspace.models.csp_requests_dto import CspRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CspRequestsDto from a JSON string
csp_requests_dto_instance = CspRequestsDto.from_json(json)
# print the JSON string representation of the object
print(CspRequestsDto.to_json())

# convert the object into a dict
csp_requests_dto_dict = csp_requests_dto_instance.to_dict()
# create an instance of CspRequestsDto from a dict
csp_requests_dto_from_dict = CspRequestsDto.from_dict(csp_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


