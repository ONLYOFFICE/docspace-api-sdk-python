# CheckDocServiceUrlRequestDto

Request parameters for checking the document service location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_service_url** | **str** | The Document Server address | [optional] 
**doc_service_url_internal** | **str** | The Document Server address in the local private network | [optional] 
**doc_service_url_portal** | **str** | The Community Server address | [optional] 
**doc_service_signature_secret** | **str** | Signature secret | [optional] 
**doc_service_signature_header** | **str** | Signature header | [optional] 
**doc_service_ssl_verification** | **bool** | Enable SSL verification | [optional] 

## Example

```python
from docspace.models.check_doc_service_url_request_dto import CheckDocServiceUrlRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDocServiceUrlRequestDto from a JSON string
check_doc_service_url_request_dto_instance = CheckDocServiceUrlRequestDto.from_json(json)
# print the JSON string representation of the object
print(CheckDocServiceUrlRequestDto.to_json())

# convert the object into a dict
check_doc_service_url_request_dto_dict = check_doc_service_url_request_dto_instance.to_dict()
# create an instance of CheckDocServiceUrlRequestDto from a dict
check_doc_service_url_request_dto_from_dict = CheckDocServiceUrlRequestDto.from_dict(check_doc_service_url_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


