# DocsCloudLicenseInfo
Represents the license information of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **datetime** | The date and time until which the license is valid. | [optional] 
**trial** | **bool** | Whether the license is a trial. | [optional] 
**build_date** | **datetime** | The license build date. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_license_info import DocsCloudLicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudLicenseInfo from a JSON string
docs_cloud_license_info_instance = DocsCloudLicenseInfo.from_json(json)
# print the JSON string representation of the object
print(DocsCloudLicenseInfo.to_json())

# convert the object into a dict
docs_cloud_license_info_dict = docs_cloud_license_info_instance.to_dict()
# create an instance of DocsCloudLicenseInfo from a dict
docs_cloud_license_info_from_dict = DocsCloudLicenseInfo.from_dict(docs_cloud_license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


