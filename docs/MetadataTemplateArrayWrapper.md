# MetadataTemplateArrayWrapper
The successful API response containing the list of MetadataTemplateDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[MetadataTemplateDto]**](MetadataTemplateDto.md) | The list of MetadataTemplateDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_template_array_wrapper import MetadataTemplateArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataTemplateArrayWrapper from a JSON string
metadata_template_array_wrapper_instance = MetadataTemplateArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(MetadataTemplateArrayWrapper.to_json())

# convert the object into a dict
metadata_template_array_wrapper_dict = metadata_template_array_wrapper_instance.to_dict()
# create an instance of MetadataTemplateArrayWrapper from a dict
metadata_template_array_wrapper_from_dict = MetadataTemplateArrayWrapper.from_dict(metadata_template_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


