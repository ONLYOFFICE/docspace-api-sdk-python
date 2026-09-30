# IsDefaultWhiteLabelLogosDto
Whether one branding slot still holds the built-in image or wordmark.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The stable name of the slot, matching the `name` of the same slot in  `GET api/2.0/settings/whitelabel/logos` - `LightSmall`, `LoginPage`, `Favicon`, `DocsEditor` and the rest,  plus `Notification`, which that list leaves out. The wordmark check reports the fixed name `logotext`  instead of a slot. | 
**default** | **bool** | Whether the slot has never been written for this portal, in which case the built-in image is what gets  rendered. It turns `false` once an image has been stored, for either the light or the dark theme, and back  to `true` after the matching restore operation. For `logotext` it stays `true` when the built-in wordmark  itself is saved, because saving that value counts as clearing the setting. | 

## Example

```python
from docspace_api_sdk.models.is_default_white_label_logos_dto import IsDefaultWhiteLabelLogosDto

# TODO update the JSON string below
json = "{}"
# create an instance of IsDefaultWhiteLabelLogosDto from a JSON string
is_default_white_label_logos_dto_instance = IsDefaultWhiteLabelLogosDto.from_json(json)
# print the JSON string representation of the object
print(IsDefaultWhiteLabelLogosDto.to_json())

# convert the object into a dict
is_default_white_label_logos_dto_dict = is_default_white_label_logos_dto_instance.to_dict()
# create an instance of IsDefaultWhiteLabelLogosDto from a dict
is_default_white_label_logos_dto_from_dict = IsDefaultWhiteLabelLogosDto.from_dict(is_default_white_label_logos_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


