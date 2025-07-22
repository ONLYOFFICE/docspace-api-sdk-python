# PageableResponseClientInfoResponse
The response containing paginated client information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | The paginated client data. | [optional] 
**limit** | **int** | The maximum number of results returned per page. | [optional] 
**last_client_id** | **str** | The identifier of the last retrieved client. | [optional] 
**last_created_on** | **datetime** | The creation date of the last retrieved client. | [optional] 

## Example

```python
from docspace-api-sdk.models.pageable_response_client_info_response import PageableResponseClientInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageableResponseClientInfoResponse from a JSON string
pageable_response_client_info_response_instance = PageableResponseClientInfoResponse.from_json(json)
# print the JSON string representation of the object
print(PageableResponseClientInfoResponse.to_json())

# convert the object into a dict
pageable_response_client_info_response_dict = pageable_response_client_info_response_instance.to_dict()
# create an instance of PageableResponseClientInfoResponse from a dict
pageable_response_client_info_response_from_dict = PageableResponseClientInfoResponse.from_dict(pageable_response_client_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


