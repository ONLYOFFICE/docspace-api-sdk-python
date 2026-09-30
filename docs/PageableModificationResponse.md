# PageableModificationResponse
One page of results ordered by modification time, together with the cursor that asks for the next page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**limit** | **int** | The page size that was applied to this request, between 1 and 50. | [optional] 
**last_modified_on** | **datetime** | The cursor to send back as last_modified_on to ask for the next page. It is null when the page is empty. | [optional] 

## Example

```python
from docspace_api_sdk.models.pageable_modification_response import PageableModificationResponse

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


