# OwnerChangeInstructionsDto

The owner change instructions parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The owner change instructions status. | [optional] 
**message** | **str** | The owner change instructions message. | [optional] 

## Example

```python
from docspace.models.owner_change_instructions_dto import OwnerChangeInstructionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerChangeInstructionsDto from a JSON string
owner_change_instructions_dto_instance = OwnerChangeInstructionsDto.from_json(json)
# print the JSON string representation of the object
print(OwnerChangeInstructionsDto.to_json())

# convert the object into a dict
owner_change_instructions_dto_dict = owner_change_instructions_dto_instance.to_dict()
# create an instance of OwnerChangeInstructionsDto from a dict
owner_change_instructions_dto_from_dict = OwnerChangeInstructionsDto.from_dict(owner_change_instructions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


