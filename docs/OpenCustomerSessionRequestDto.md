# OpenCustomerSessionRequestDto
Client session opening parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account** | **int** | Service account | [optional] 
**external_ref** | **str** | External reference | [optional] 
**quantity** | **int** | Quantity | [optional] 

## Example

```python
from docspace-api-python.models.open_customer_session_request_dto import OpenCustomerSessionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenCustomerSessionRequestDto from a JSON string
open_customer_session_request_dto_instance = OpenCustomerSessionRequestDto.from_json(json)
# print the JSON string representation of the object
print(OpenCustomerSessionRequestDto.to_json())

# convert the object into a dict
open_customer_session_request_dto_dict = open_customer_session_request_dto_instance.to_dict()
# create an instance of OpenCustomerSessionRequestDto from a dict
open_customer_session_request_dto_from_dict = OpenCustomerSessionRequestDto.from_dict(open_customer_session_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


