# DocsCloudLicenseInfoDto
Represents the license information of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **datetime** | The date and time until which the license is valid. | [optional] 
**trial** | **bool** | Whether the license is a trial. | [optional] 
**build_date** | **datetime** | The license build date. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_license_info_dto import DocsCloudLicenseInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudLicenseInfoDto from a JSON string
docs_cloud_license_info_dto_instance = DocsCloudLicenseInfoDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudLicenseInfoDto.to_json())

# convert the object into a dict
docs_cloud_license_info_dto_dict = docs_cloud_license_info_dto_instance.to_dict()
# create an instance of DocsCloudLicenseInfoDto from a dict
docs_cloud_license_info_dto_from_dict = DocsCloudLicenseInfoDto.from_dict(docs_cloud_license_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


