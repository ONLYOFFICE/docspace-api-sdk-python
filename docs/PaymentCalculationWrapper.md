# PaymentCalculationWrapper
The successful API response containing the PaymentCalculationDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**PaymentCalculationDto**](PaymentCalculationDto.md) | The PaymentCalculationDto object returned by the operation. | [optional] 
**count** | **int** | How many items this response carries: the length of the page for a list, 1 for a single object | [optional] 
**total** | **int** | How many items the whole list holds across all pages, for working out how many pages to request. Sent only by the operations that page their results, and left out of every other response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.payment_calculation_wrapper import PaymentCalculationWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCalculationWrapper from a JSON string
payment_calculation_wrapper_instance = PaymentCalculationWrapper.from_json(json)
# print the JSON string representation of the object
print(PaymentCalculationWrapper.to_json())

# convert the object into a dict
payment_calculation_wrapper_dict = payment_calculation_wrapper_instance.to_dict()
# create an instance of PaymentCalculationWrapper from a dict
payment_calculation_wrapper_from_dict = PaymentCalculationWrapper.from_dict(payment_calculation_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


