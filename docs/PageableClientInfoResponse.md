# PageableClientInfoResponse
One page of consent-facing client info together with the next-page cursor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientInfoResponse]**](ClientInfoResponse.md) | The items on this page, at most as many as the requested limit. An empty array means there is nothing further to read. | [optional] 
**limit** | **int** | The page size that was applied to this request, between 1 and 50. | [optional] 
**last_client_id** | **str** | The cursor to send back as last_client_id to ask for the next page, together with last_created_on. It is null when the page is empty. | [optional] 
**last_created_on** | **datetime** | The cursor to send back as last_created_on to ask for the next page, together with last_client_id. It is null when the page is empty. | [optional] 

## Example

```python
from docspace_api_sdk.models.pageable_client_info_response import PageableClientInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageableClientInfoResponse from a JSON string
pageable_client_info_response_instance = PageableClientInfoResponse.from_json(json)
# print the JSON string representation of the object
print(PageableClientInfoResponse.to_json())

# convert the object into a dict
pageable_client_info_response_dict = pageable_client_info_response_instance.to_dict()
# create an instance of PageableClientInfoResponse from a dict
pageable_client_info_response_from_dict = PageableClientInfoResponse.from_dict(pageable_client_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


