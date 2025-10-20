# TimezonesRequestsArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[TimezonesRequestsDto]**](TimezonesRequestsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.timezones_requests_array_wrapper import TimezonesRequestsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TimezonesRequestsArrayWrapper from a JSON string
timezones_requests_array_wrapper_instance = TimezonesRequestsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(TimezonesRequestsArrayWrapper.to_json())

# convert the object into a dict
timezones_requests_array_wrapper_dict = timezones_requests_array_wrapper_instance.to_dict()
# create an instance of TimezonesRequestsArrayWrapper from a dict
timezones_requests_array_wrapper_from_dict = TimezonesRequestsArrayWrapper.from_dict(timezones_requests_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


