# ConfirmWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ConfirmDto**](ConfirmDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.confirm_wrapper import ConfirmWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmWrapper from a JSON string
confirm_wrapper_instance = ConfirmWrapper.from_json(json)
# print the JSON string representation of the object
print(ConfirmWrapper.to_json())

# convert the object into a dict
confirm_wrapper_dict = confirm_wrapper_instance.to_dict()
# create an instance of ConfirmWrapper from a dict
confirm_wrapper_from_dict = ConfirmWrapper.from_dict(confirm_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


