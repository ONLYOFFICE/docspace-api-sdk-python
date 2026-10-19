# LicensorDetailsArrayWrapper
The successful API response containing the list of LicensorDetailsDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[LicensorDetailsDto]**](LicensorDetailsDto.md) | The list of LicensorDetailsDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.licensor_details_array_wrapper import LicensorDetailsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of LicensorDetailsArrayWrapper from a JSON string
licensor_details_array_wrapper_instance = LicensorDetailsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(LicensorDetailsArrayWrapper.to_json())

# convert the object into a dict
licensor_details_array_wrapper_dict = licensor_details_array_wrapper_instance.to_dict()
# create an instance of LicensorDetailsArrayWrapper from a dict
licensor_details_array_wrapper_from_dict = LicensorDetailsArrayWrapper.from_dict(licensor_details_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


