# ServiceLimitWrapper
The successful API response containing the ServiceLimitDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ServiceLimitDto**](ServiceLimitDto.md) | The ServiceLimitDto object returned by the operation. | [optional] 
**count** | **int** | How many items this response carries: the length of the page for a list, 1 for a single object | [optional] 
**total** | **int** | How many items the whole list holds across all pages, for working out how many pages to request. Sent only by the operations that page their results, and left out of every other response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.service_limit_wrapper import ServiceLimitWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLimitWrapper from a JSON string
service_limit_wrapper_instance = ServiceLimitWrapper.from_json(json)
# print the JSON string representation of the object
print(ServiceLimitWrapper.to_json())

# convert the object into a dict
service_limit_wrapper_dict = service_limit_wrapper_instance.to_dict()
# create an instance of ServiceLimitWrapper from a dict
service_limit_wrapper_from_dict = ServiceLimitWrapper.from_dict(service_limit_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


