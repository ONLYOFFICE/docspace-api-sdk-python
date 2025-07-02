# QuotaWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**QuotaDto**](QuotaDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.quota_wrapper import QuotaWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaWrapper from a JSON string
quota_wrapper_instance = QuotaWrapper.from_json(json)
# print the JSON string representation of the object
print(QuotaWrapper.to_json())

# convert the object into a dict
quota_wrapper_dict = quota_wrapper_instance.to_dict()
# create an instance of QuotaWrapper from a dict
quota_wrapper_from_dict = QuotaWrapper.from_dict(quota_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


