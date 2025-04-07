# AceShortWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User | [optional] 
**permissions** | **str** | User access rights to the file | [optional] 
**is_link** | **bool** | Is link | [optional] 

## Example

```python
from docspace.models.ace_short_wrapper import AceShortWrapper

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


