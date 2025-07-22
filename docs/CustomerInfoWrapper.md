# CustomerInfoWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CustomerInfoDto**](CustomerInfoDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.customer_info_wrapper import CustomerInfoWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInfoWrapper from a JSON string
customer_info_wrapper_instance = CustomerInfoWrapper.from_json(json)
# print the JSON string representation of the object
print(CustomerInfoWrapper.to_json())

# convert the object into a dict
customer_info_wrapper_dict = customer_info_wrapper_instance.to_dict()
# create an instance of CustomerInfoWrapper from a dict
customer_info_wrapper_from_dict = CustomerInfoWrapper.from_dict(customer_info_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


