# AceShortWrapper
The information about the settings which allow to share the document with other users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | The name of the user the document will be shared with. | [optional] 
**permissions** | **str** | The access rights for the user with the name above.  Can be Full Access, Read Only, or Deny Access. | [optional] 
**is_link** | **bool** | Specifies whether to change the user icon to the link icon. | [optional] 

## Example

```python
from docspace_api_sdk.models.ace_short_wrapper import AceShortWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AceShortWrapper from a JSON string
ace_short_wrapper_instance = AceShortWrapper.from_json(json)
# print the JSON string representation of the object
print(AceShortWrapper.to_json())

# convert the object into a dict
ace_short_wrapper_dict = ace_short_wrapper_instance.to_dict()
# create an instance of AceShortWrapper from a dict
ace_short_wrapper_from_dict = AceShortWrapper.from_dict(ace_short_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


