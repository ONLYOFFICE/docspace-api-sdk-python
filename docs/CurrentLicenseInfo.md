# CurrentLicenseInfo
The two facts about the subscription in force that a payment page needs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial** | **bool** | Whether the portal is on a trial rather than a paid subscription. A trial expires at `dueDate` and is not  extended by paying - a plan has to be bought instead. | 
**due_date** | **datetime** | The day the subscription runs out, with the time of day cut off. The largest value a date can hold means  it never runs out, which is how a free or unlimited plan is expressed. | 

## Example

```python
from docspace_api_sdk.models.current_license_info import CurrentLicenseInfo

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


