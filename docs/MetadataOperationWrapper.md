# MetadataOperationWrapper
The successful API response containing the MetadataOperationDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**MetadataOperationDto**](MetadataOperationDto.md) | The MetadataOperationDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_operation_wrapper import MetadataOperationWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOperationWrapper from a JSON string
metadata_operation_wrapper_instance = MetadataOperationWrapper.from_json(json)
# print the JSON string representation of the object
print(MetadataOperationWrapper.to_json())

# convert the object into a dict
metadata_operation_wrapper_dict = metadata_operation_wrapper_instance.to_dict()
# create an instance of MetadataOperationWrapper from a dict
metadata_operation_wrapper_from_dict = MetadataOperationWrapper.from_dict(metadata_operation_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


