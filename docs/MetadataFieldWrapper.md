# MetadataFieldWrapper
The successful API response containing the MetadataFieldDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**MetadataFieldDto**](MetadataFieldDto.md) | The MetadataFieldDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_field_wrapper import MetadataFieldWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataFieldWrapper from a JSON string
metadata_field_wrapper_instance = MetadataFieldWrapper.from_json(json)
# print the JSON string representation of the object
print(MetadataFieldWrapper.to_json())

# convert the object into a dict
metadata_field_wrapper_dict = metadata_field_wrapper_instance.to_dict()
# create an instance of MetadataFieldWrapper from a dict
metadata_field_wrapper_from_dict = MetadataFieldWrapper.from_dict(metadata_field_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


