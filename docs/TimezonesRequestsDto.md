# TimezonesRequestsDto
One time zone the host offers, as its identifier and the label to show for it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The IANA identifier of the time zone. This is the value the portal time zone is set to, so pass it on  unchanged to `PUT api/2.0/settings/timeandlanguage`. | 
**display_name** | **str** | The label to show for the zone, carrying its UTC offset as it stood when the list was built. The offset is a  snapshot rather than a rule, so a zone observing daylight saving reads differently at other times of the  year; sort and match on `id` instead. | 

## Example

```python
from docspace_api_sdk.models.timezones_requests_dto import TimezonesRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TimezonesRequestsDto from a JSON string
timezones_requests_dto_instance = TimezonesRequestsDto.from_json(json)
# print the JSON string representation of the object
print(TimezonesRequestsDto.to_json())

# convert the object into a dict
timezones_requests_dto_dict = timezones_requests_dto_instance.to_dict()
# create an instance of TimezonesRequestsDto from a dict
timezones_requests_dto_from_dict = TimezonesRequestsDto.from_dict(timezones_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


