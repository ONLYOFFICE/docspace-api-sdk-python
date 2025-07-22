# ExternalShareWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ExternalShareDto**](ExternalShareDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.external_share_wrapper import ExternalShareWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalShareWrapper from a JSON string
external_share_wrapper_instance = ExternalShareWrapper.from_json(json)
# print the JSON string representation of the object
print(ExternalShareWrapper.to_json())

# convert the object into a dict
external_share_wrapper_dict = external_share_wrapper_instance.to_dict()
# create an instance of ExternalShareWrapper from a dict
external_share_wrapper_from_dict = ExternalShareWrapper.from_dict(external_share_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


