# FeatureUsedDto
The used space parameters of the tenant quota feature.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | The used space value. | 
**title** | **str** | The used space title. | [optional] 

## Example

```python
from docspace_api_sdk.models.feature_used_dto import FeatureUsedDto

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureUsedDto from a JSON string
feature_used_dto_instance = FeatureUsedDto.from_json(json)
# print the JSON string representation of the object
print(FeatureUsedDto.to_json())

# convert the object into a dict
feature_used_dto_dict = feature_used_dto_instance.to_dict()
# create an instance of FeatureUsedDto from a dict
feature_used_dto_from_dict = FeatureUsedDto.from_dict(feature_used_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


