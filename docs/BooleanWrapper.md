# BooleanWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **bool** |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanWrapper from a JSON string
boolean_wrapper_instance = BooleanWrapper.from_json(json)
# print the JSON string representation of the object
print(BooleanWrapper.to_json())

# convert the object into a dict
boolean_wrapper_dict = boolean_wrapper_instance.to_dict()
# create an instance of BooleanWrapper from a dict
boolean_wrapper_from_dict = BooleanWrapper.from_dict(boolean_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


