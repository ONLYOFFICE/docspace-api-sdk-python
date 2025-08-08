# FormRoleArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FormRole]**](FormRole.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.form_role_array_wrapper import FormRoleArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FormRoleArrayWrapper from a JSON string
form_role_array_wrapper_instance = FormRoleArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FormRoleArrayWrapper.to_json())

# convert the object into a dict
form_role_array_wrapper_dict = form_role_array_wrapper_instance.to_dict()
# create an instance of FormRoleArrayWrapper from a dict
form_role_array_wrapper_from_dict = FormRoleArrayWrapper.from_dict(form_role_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


