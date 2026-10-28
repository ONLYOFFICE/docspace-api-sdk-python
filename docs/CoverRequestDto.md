# CoverRequestDto
The picture and the colour a room is drawn with while it has no logo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The background colour the room is drawn with while it has no logo, as six hexadecimal digits with no leading  number sign. An empty value restores the default colour of the room type. | [optional] 
**cover** | **str** | The picture drawn on the room while it has no logo, named by an identifier from  `GET api/2.0/files/rooms/covers`. Any other value is rejected, and an empty value leaves the room without a  cover. | [optional] 

## Example

```python
from docspace_api_sdk.models.cover_request_dto import CoverRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CoverRequestDto from a JSON string
cover_request_dto_instance = CoverRequestDto.from_json(json)
# print the JSON string representation of the object
print(CoverRequestDto.to_json())

# convert the object into a dict
cover_request_dto_dict = cover_request_dto_instance.to_dict()
# create an instance of CoverRequestDto from a dict
cover_request_dto_from_dict = CoverRequestDto.from_dict(cover_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


