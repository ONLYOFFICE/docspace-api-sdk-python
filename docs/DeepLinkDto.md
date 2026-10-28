# DeepLinkDto
What a mobile client needs to hand a portal link to the installed application instead of the browser.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android_package_name** | **str** | The package name to look for on Android, and to build a store link from when the application is missing.  All three fields are empty strings on an installation that ships no mobile application, which is the  signal to keep opening links in the browser. | 
**url** | **str** | The address the client redirects a portal link through so that the application can claim it. It is the  installation's own deep-link host, not a link to any particular document. | 
**ios_package_id** | **str** | The bundle identifier to look for on iOS, used the same way as `androidPackageName`. | 

## Example

```python
from docspace_api_sdk.models.deep_link_dto import DeepLinkDto

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


