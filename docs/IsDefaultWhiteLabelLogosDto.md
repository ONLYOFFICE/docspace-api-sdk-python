# IsDefaultWhiteLabelLogosDto

The default white label logos parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The white label logo name. | [optional] 
**default** | **bool** | Specifies if the white label logo is default or not. | [optional] 

## Example

```python
from docspace.models.is_default_white_label_logos_dto import IsDefaultWhiteLabelLogosDto

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


