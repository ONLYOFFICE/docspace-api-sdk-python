# SchemaRequestsArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[SchemaRequestsDto]**](SchemaRequestsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.schema_requests_array_wrapper import SchemaRequestsArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaRequestsArrayWrapper from a JSON string
schema_requests_array_wrapper_instance = SchemaRequestsArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(SchemaRequestsArrayWrapper.to_json())

# convert the object into a dict
schema_requests_array_wrapper_dict = schema_requests_array_wrapper_instance.to_dict()
# create an instance of SchemaRequestsArrayWrapper from a dict
schema_requests_array_wrapper_from_dict = SchemaRequestsArrayWrapper.from_dict(schema_requests_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


