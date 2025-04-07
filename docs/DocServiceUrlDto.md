# DocServiceUrlDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Version | 
**doc_service_url_api** | **str** | Doc service url api | 
**doc_service_url** | **str** | Doc service url | 
**doc_service_url_internal** | **str** | Doc service url internal | 
**doc_service_portal_url** | **str** | Doc service portal url | 
**doc_service_signature_header** | **str** | Doc service signature header | [optional] 
**doc_service_ssl_verification** | **bool** | Enable SSL verification | [optional] 
**is_default** | **bool** | Is default | 

## Example

```python
from docspace.models.doc_service_url_dto import DocServiceUrlDto

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


