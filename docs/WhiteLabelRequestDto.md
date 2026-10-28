# WhiteLabelRequestDto
The branding a portal is given: the wordmark, the logo images, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_text** | **str** | The wordmark printed next to or instead of a logo image, on the login page, in the editors and in  notification letters. An empty or blank value, and the built-in `ONLYOFFICE` itself, clear the setting rather  than store it. The text is not rendered into the logo images, which carry their own wordmark. | [optional] 
**logo** | [**List[ItemKeyValuePairStringLogoRequestDto]**](ItemKeyValuePairStringLogoRequestDto.md) | The logo images to store, each entry naming a logo slot in its `key` - the numeric `type` published by  `GET api/2.0/settings/whitelabel/logos` - and carrying the two theme images in its value. A slot left out of  the list keeps the image it has, so this is a partial update rather than a replacement of the whole branding.  Saving the login-page slot also rebuilds the notification logo from it. | [optional] 

## Example

```python
from docspace_api_sdk.models.white_label_request_dto import WhiteLabelRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteLabelRequestDto from a JSON string
white_label_request_dto_instance = WhiteLabelRequestDto.from_json(json)
# print the JSON string representation of the object
print(WhiteLabelRequestDto.to_json())

# convert the object into a dict
white_label_request_dto_dict = white_label_request_dto_instance.to_dict()
# create an instance of WhiteLabelRequestDto from a dict
white_label_request_dto_from_dict = WhiteLabelRequestDto.from_dict(white_label_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


