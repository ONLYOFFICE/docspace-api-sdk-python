# QuotaArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[QuotaDto]**](QuotaDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.quota_array_wrapper import QuotaArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaArrayWrapper from a JSON string
quota_array_wrapper_instance = QuotaArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(QuotaArrayWrapper.to_json())

# convert the object into a dict
quota_array_wrapper_dict = quota_array_wrapper_instance.to_dict()
# create an instance of QuotaArrayWrapper from a dict
quota_array_wrapper_from_dict = QuotaArrayWrapper.from_dict(quota_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


