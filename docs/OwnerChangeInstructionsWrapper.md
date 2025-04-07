# OwnerChangeInstructionsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**OwnerChangeInstructionsDto**](OwnerChangeInstructionsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.owner_change_instructions_wrapper import OwnerChangeInstructionsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerChangeInstructionsWrapper from a JSON string
owner_change_instructions_wrapper_instance = OwnerChangeInstructionsWrapper.from_json(json)
# print the JSON string representation of the object
print(OwnerChangeInstructionsWrapper.to_json())

# convert the object into a dict
owner_change_instructions_wrapper_dict = owner_change_instructions_wrapper_instance.to_dict()
# create an instance of OwnerChangeInstructionsWrapper from a dict
owner_change_instructions_wrapper_from_dict = OwnerChangeInstructionsWrapper.from_dict(owner_change_instructions_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


