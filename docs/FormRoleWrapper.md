# FormRoleWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FormRole**](FormRole.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.form_role_wrapper import FormRoleWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FormRoleWrapper from a JSON string
form_role_wrapper_instance = FormRoleWrapper.from_json(json)
# print the JSON string representation of the object
print(FormRoleWrapper.to_json())

# convert the object into a dict
form_role_wrapper_dict = form_role_wrapper_instance.to_dict()
# create an instance of FormRoleWrapper from a dict
form_role_wrapper_from_dict = FormRoleWrapper.from_dict(form_role_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


