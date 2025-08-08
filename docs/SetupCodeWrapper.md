# SetupCodeWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SetupCode**](SetupCode.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.setup_code_wrapper import SetupCodeWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SetupCodeWrapper from a JSON string
setup_code_wrapper_instance = SetupCodeWrapper.from_json(json)
# print the JSON string representation of the object
print(SetupCodeWrapper.to_json())

# convert the object into a dict
setup_code_wrapper_dict = setup_code_wrapper_instance.to_dict()
# create an instance of SetupCodeWrapper from a dict
setup_code_wrapper_from_dict = SetupCodeWrapper.from_dict(setup_code_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


