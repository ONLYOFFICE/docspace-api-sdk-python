# UpdateServiceLimitRequestDto
The new thresholds and state of an existing service limit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the service limit, as returned in `id` by the operation that created it or by the reads of limits. | 
**amount_value** | **float** | The most money the AI services may cost per period, in their currency. Zero blocks the AI services completely. | [optional] 
**quantity_value** | **int** | The largest quantity the AI services may consume per period, in their common unit. Zero blocks the AI services  completely. | [optional] 
**enabled** | **bool** | Whether the limit is in force: false switches it off at once, true switches it back on. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_service_limit_request_dto import UpdateServiceLimitRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceLimitRequestDto from a JSON string
update_service_limit_request_dto_instance = UpdateServiceLimitRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateServiceLimitRequestDto.to_json())

# convert the object into a dict
update_service_limit_request_dto_dict = update_service_limit_request_dto_instance.to_dict()
# create an instance of UpdateServiceLimitRequestDto from a dict
update_service_limit_request_dto_from_dict = UpdateServiceLimitRequestDto.from_dict(update_service_limit_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


