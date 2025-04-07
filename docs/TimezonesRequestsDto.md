# TimezonesRequestsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Time zone ID | [optional] 
**display_name** | **str** | Time zone display name | [optional] 

## Example

```python
from docspace.models.timezones_requests_dto import TimezonesRequestsDto

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


