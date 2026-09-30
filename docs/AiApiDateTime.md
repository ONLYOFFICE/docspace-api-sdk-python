# AiApiDateTime
The API date and time parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utc_time** | **datetime** | The time in UTC format. | [optional] [readonly] 
**time_zone_offset** | **str** | The time zone offset. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.ai_api_date_time import AiApiDateTime

# TODO update the JSON string below
json = "{}"
# create an instance of AiApiDateTime from a JSON string
ai_api_date_time_instance = AiApiDateTime.from_json(json)
# print the JSON string representation of the object
print(AiApiDateTime.to_json())

# convert the object into a dict
ai_api_date_time_dict = ai_api_date_time_instance.to_dict()
# create an instance of AiApiDateTime from a dict
ai_api_date_time_from_dict = AiApiDateTime.from_dict(ai_api_date_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


