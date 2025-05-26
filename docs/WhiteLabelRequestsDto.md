# WhiteLabelRequestsDto

The request parameters for configuring the white label branding settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_text** | **str** | The text to display alongside or in place of the logo. | [optional] 
**logo** | [**List[ItemKeyValuePairStringLogoRequestsDto]**](ItemKeyValuePairStringLogoRequestsDto.md) | The white label tenant IDs with their logos (light or dark). | [optional] 

## Example

```python
from docspace.models.white_label_requests_dto import WhiteLabelRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteLabelRequestsDto from a JSON string
white_label_requests_dto_instance = WhiteLabelRequestsDto.from_json(json)
# print the JSON string representation of the object
print(WhiteLabelRequestsDto.to_json())

# convert the object into a dict
white_label_requests_dto_dict = white_label_requests_dto_instance.to_dict()
# create an instance of WhiteLabelRequestsDto from a dict
white_label_requests_dto_from_dict = WhiteLabelRequestsDto.from_dict(white_label_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


