# PageableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**last_client_id** | **str** |  | [optional] 
**last_created_on** | **datetime** |  | [optional] 

## Example

```python
from docspace.models.pageable_response import PageableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageableResponse from a JSON string
pageable_response_instance = PageableResponse.from_json(json)
# print the JSON string representation of the object
print(PageableResponse.to_json())

# convert the object into a dict
pageable_response_dict = pageable_response_instance.to_dict()
# create an instance of PageableResponse from a dict
pageable_response_from_dict = PageableResponse.from_dict(pageable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


