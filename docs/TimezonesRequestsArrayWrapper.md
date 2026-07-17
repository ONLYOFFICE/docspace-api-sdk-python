# TimezonesRequestsArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[TimezonesRequestsDto]**](TimezonesRequestsDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

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


