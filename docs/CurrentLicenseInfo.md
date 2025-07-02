# CurrentLicenseInfo
The current license information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial** | **bool** | Specifies whether the license is trial or not. | [optional] 
**due_date** | **datetime** | The date when the license expires. | [optional] 

## Example

```python
from docspace-api-python.models.current_license_info import CurrentLicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentLicenseInfo from a JSON string
current_license_info_instance = CurrentLicenseInfo.from_json(json)
# print the JSON string representation of the object
print(CurrentLicenseInfo.to_json())

# convert the object into a dict
current_license_info_dict = current_license_info_instance.to_dict()
# create an instance of CurrentLicenseInfo from a dict
current_license_info_from_dict = CurrentLicenseInfo.from_dict(current_license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


