# DocServiceUrlWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DocServiceUrlDto**](DocServiceUrlDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.doc_service_url_wrapper import DocServiceUrlWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DocServiceUrlWrapper from a JSON string
doc_service_url_wrapper_instance = DocServiceUrlWrapper.from_json(json)
# print the JSON string representation of the object
print(DocServiceUrlWrapper.to_json())

# convert the object into a dict
doc_service_url_wrapper_dict = doc_service_url_wrapper_instance.to_dict()
# create an instance of DocServiceUrlWrapper from a dict
doc_service_url_wrapper_from_dict = DocServiceUrlWrapper.from_dict(doc_service_url_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


