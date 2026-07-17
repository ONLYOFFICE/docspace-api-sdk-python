# StringWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.string_wrapper import StringWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of StringWrapper from a JSON string
string_wrapper_instance = StringWrapper.from_json(json)
# print the JSON string representation of the object
print(StringWrapper.to_json())

# convert the object into a dict
string_wrapper_dict = string_wrapper_instance.to_dict()
# create an instance of StringWrapper from a dict
string_wrapper_from_dict = StringWrapper.from_dict(string_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


