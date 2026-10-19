# LogoRequestDto
The two theme variants of one branding logo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light** | **str** | The image used on a light background, either as a `data:image/png;base64,...` payload - `png`, `jpg` and  `svg` are accepted - or as the name of a file already put in the temporary store. | [optional] 
**dark** | **str** | The image used on a dark background, in the same two forms as `light`. It is only stored for the slots that  have a dark variant and is ignored for the favicon and the editor logos. | [optional] 

## Example

```python
from docspace_api_sdk.models.logo_request_dto import LogoRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of LogoRequestDto from a JSON string
logo_request_dto_instance = LogoRequestDto.from_json(json)
# print the JSON string representation of the object
print(LogoRequestDto.to_json())

# convert the object into a dict
logo_request_dto_dict = logo_request_dto_instance.to_dict()
# create an instance of LogoRequestDto from a dict
logo_request_dto_from_dict = LogoRequestDto.from_dict(logo_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


