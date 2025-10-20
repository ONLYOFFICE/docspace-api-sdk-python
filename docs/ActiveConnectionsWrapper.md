# ActiveConnectionsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ActiveConnectionsDto**](ActiveConnectionsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.active_connections_wrapper import ActiveConnectionsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveConnectionsWrapper from a JSON string
active_connections_wrapper_instance = ActiveConnectionsWrapper.from_json(json)
# print the JSON string representation of the object
print(ActiveConnectionsWrapper.to_json())

# convert the object into a dict
active_connections_wrapper_dict = active_connections_wrapper_instance.to_dict()
# create an instance of ActiveConnectionsWrapper from a dict
active_connections_wrapper_from_dict = ActiveConnectionsWrapper.from_dict(active_connections_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


