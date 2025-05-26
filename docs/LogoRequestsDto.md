# LogoRequestsDto

The request parameters for the theme-specific logo configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light** | **str** | The URL or base64-encoded image data for the light theme logo. | [optional] 
**dark** | **str** | The URL or base64-encoded image data for the dark theme logo. | [optional] 

## Example

```python
from docspace.models.logo_requests_dto import LogoRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of LogoRequestsDto from a JSON string
logo_requests_dto_instance = LogoRequestsDto.from_json(json)
# print the JSON string representation of the object
print(LogoRequestsDto.to_json())

# convert the object into a dict
logo_requests_dto_dict = logo_requests_dto_instance.to_dict()
# create an instance of LogoRequestsDto from a dict
logo_requests_dto_from_dict = LogoRequestsDto.from_dict(logo_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


