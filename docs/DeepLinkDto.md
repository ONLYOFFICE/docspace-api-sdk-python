# DeepLinkDto

The deep link parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android_package_name** | **str** | The Android package name. | [optional] 
**url** | **str** | The deep link URL. | [optional] 
**ios_package_id** | **str** | The deep link IOS package ID. | [optional] 

## Example

```python
from docspace.models.deep_link_dto import DeepLinkDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeepLinkDto from a JSON string
deep_link_dto_instance = DeepLinkDto.from_json(json)
# print the JSON string representation of the object
print(DeepLinkDto.to_json())

# convert the object into a dict
deep_link_dto_dict = deep_link_dto_instance.to_dict()
# create an instance of DeepLinkDto from a dict
deep_link_dto_from_dict = DeepLinkDto.from_dict(deep_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


