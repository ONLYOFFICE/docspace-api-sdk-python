# FillingFormResultIntegerWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FillingFormResultDtoInteger**](FillingFormResultDtoInteger.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.filling_form_result_integer_wrapper import FillingFormResultIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FillingFormResultIntegerWrapper from a JSON string
filling_form_result_integer_wrapper_instance = FillingFormResultIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(FillingFormResultIntegerWrapper.to_json())

# convert the object into a dict
filling_form_result_integer_wrapper_dict = filling_form_result_integer_wrapper_instance.to_dict()
# create an instance of FillingFormResultIntegerWrapper from a dict
filling_form_result_integer_wrapper_from_dict = FillingFormResultIntegerWrapper.from_dict(filling_form_result_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


