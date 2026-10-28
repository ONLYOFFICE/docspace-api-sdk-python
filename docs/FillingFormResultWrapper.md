# FillingFormResultWrapper
The successful API response containing the FillingFormResultDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FillingFormResultDto**](FillingFormResultDto.md) | The FillingFormResultDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.filling_form_result_wrapper import FillingFormResultWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FillingFormResultWrapper from a JSON string
filling_form_result_wrapper_instance = FillingFormResultWrapper.from_json(json)
# print the JSON string representation of the object
print(FillingFormResultWrapper.to_json())

# convert the object into a dict
filling_form_result_wrapper_dict = filling_form_result_wrapper_instance.to_dict()
# create an instance of FillingFormResultWrapper from a dict
filling_form_result_wrapper_from_dict = FillingFormResultWrapper.from_dict(filling_form_result_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


