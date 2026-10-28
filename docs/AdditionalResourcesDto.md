# AdditionalResourcesDto
Which of the ONLYOFFICE help and community entries the interface may offer, installation-wide, in the shape the  reset of these flags returns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_docs_enabled** | **bool** | Whether the sample documents that ONLYOFFICE ships may be placed in a new user's Documents. Unlike the link  flags below it depends on nothing that has to be configured, so its built-in value is always `true`. | [optional] 
**help_center_enabled** | **bool** | Whether the interface may offer the Help Center entry. It is `false` both when the entry was switched off  for the installation and when the installation configures no Help Center address at all; the addresses  themselves are not part of this answer and arrive in `externalResources` of `GET api/2.0/settings`. | [optional] 
**feedback_and_support_enabled** | **bool** | Whether the interface may offer the Feedback and Support entry, `false` for the same two reasons as  `helpCenterEnabled`. | [optional] 
**user_forum_enabled** | **bool** | Whether the interface may offer the user forum entry, `false` for the same two reasons as  `helpCenterEnabled`. | [optional] 
**video_guides_enabled** | **bool** | Whether the interface may offer the Video Guides entry, `false` for the same two reasons as  `helpCenterEnabled`. | [optional] 
**license_agreements_enabled** | **bool** | Whether the interface may offer the License Agreements entry, `false` for the same two reasons as  `helpCenterEnabled`. | [optional] 
**last_modified** | **datetime** | When these flags were last stored. Flags that were never stored report the moment they were read, and the  answer of the reset operation reports `0001-01-01T00:00:00`. | [optional] 

## Example

```python
from docspace_api_sdk.models.additional_resources_dto import AdditionalResourcesDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalResourcesDto from a JSON string
additional_resources_dto_instance = AdditionalResourcesDto.from_json(json)
# print the JSON string representation of the object
print(AdditionalResourcesDto.to_json())

# convert the object into a dict
additional_resources_dto_dict = additional_resources_dto_instance.to_dict()
# create an instance of AdditionalResourcesDto from a dict
additional_resources_dto_from_dict = AdditionalResourcesDto.from_dict(additional_resources_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


