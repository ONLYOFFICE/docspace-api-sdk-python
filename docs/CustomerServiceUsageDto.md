# CustomerServiceUsageDto
What one wallet service was consumed and cost over the requested period, added up rather than listed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | The stable key of the service, which is what the `serviceName` filter of this operation matches on and  what `GET api/2.0/portal/payment/walletservice` looks a service up by. | [optional] 
**title** | **str** | The service name in the portal language, for printing rather than matching. | [optional] 
**service_unit** | **str** | What `totalQuantity` counts, in the portal language. AI consumption is reported in tokens here rather  than in the AI credits the service is sold in, so it does not line up with the price list. | [optional] 
**currency** | **str** | The currency `totalAmount` and `price` are expressed in, as a three-letter ISO 4217 code. | [optional] 
**total_quantity** | **int** | How many units of the service were consumed over the period, in the unit named by `serviceUnit`. | [optional] 
**total_amount** | **float** | What that consumption cost over the period. It is what was actually charged, so it can differ from  `price` times `totalQuantity` when the price changed inside the period. | [optional] 
**operation_count** | **int** | How many separate charges the total was added up from. The charges themselves are in  `GET api/2.0/portal/payment/customer/operations`. | [optional] 
**price** | **float** | What one unit of the service costs today, not what it cost during the period. It is `0` when the service  is no longer on the installation's price list. | [optional] 
**subscription** | **bool** | Whether the service is billed as a standing subscription rather than per unit consumed. It is derived  from today's price list, so it describes the service as it is sold now. | [optional] 

## Example

```python
from docspace_api_sdk.models.customer_service_usage_dto import CustomerServiceUsageDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerServiceUsageDto from a JSON string
customer_service_usage_dto_instance = CustomerServiceUsageDto.from_json(json)
# print the JSON string representation of the object
print(CustomerServiceUsageDto.to_json())

# convert the object into a dict
customer_service_usage_dto_dict = customer_service_usage_dto_instance.to_dict()
# create an instance of CustomerServiceUsageDto from a dict
customer_service_usage_dto_from_dict = CustomerServiceUsageDto.from_dict(customer_service_usage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


