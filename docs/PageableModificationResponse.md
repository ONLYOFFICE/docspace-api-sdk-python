# PageableModificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**last_modified_on** | **datetime** |  | [optional] 

## Example

```python
from docspace.models.pageable_modification_response import PageableModificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageableModificationResponse from a JSON string
pageable_modification_response_instance = PageableModificationResponse.from_json(json)
# print the JSON string representation of the object
print(PageableModificationResponse.to_json())

# convert the object into a dict
pageable_modification_response_dict = pageable_modification_response_instance.to_dict()
# create an instance of PageableModificationResponse from a dict
pageable_modification_response_from_dict = PageableModificationResponse.from_dict(pageable_modification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


