# OwnerChangeInstructionsWrapper
The successful API response containing the OwnerChangeInstructionsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**OwnerChangeInstructionsDto**](OwnerChangeInstructionsDto.md) | The OwnerChangeInstructionsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.owner_change_instructions_wrapper import OwnerChangeInstructionsWrapper

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


