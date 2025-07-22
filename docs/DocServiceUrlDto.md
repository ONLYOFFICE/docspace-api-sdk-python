# DocServiceUrlDto
The document service URL parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the document service. | 
**doc_service_url_api** | **str** | The document service URL API. | 
**doc_service_url** | **str** | The document service URL. | 
**doc_service_url_internal** | **str** | The internal document service URL. | 
**doc_service_portal_url** | **str** | The document service portal URL. | 
**doc_service_signature_header** | **str** | The document service signature header. | [optional] 
**doc_service_ssl_verification** | **bool** | Specifies if the document service SSL verification is enabled. | [optional] 
**is_default** | **bool** | Specifies if the document service is default. | 

## Example

```python
from docspace-api-sdk.models.doc_service_url_dto import DocServiceUrlDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocServiceUrlDto from a JSON string
doc_service_url_dto_instance = DocServiceUrlDto.from_json(json)
# print the JSON string representation of the object
print(DocServiceUrlDto.to_json())

# convert the object into a dict
doc_service_url_dto_dict = doc_service_url_dto_instance.to_dict()
# create an instance of DocServiceUrlDto from a dict
doc_service_url_dto_from_dict = DocServiceUrlDto.from_dict(doc_service_url_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


