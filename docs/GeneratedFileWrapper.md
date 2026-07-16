# GeneratedFileWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GeneratedFileDto**](GeneratedFileDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.generated_file_wrapper import GeneratedFileWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedFileWrapper from a JSON string
generated_file_wrapper_instance = GeneratedFileWrapper.from_json(json)
# print the JSON string representation of the object
print(GeneratedFileWrapper.to_json())

# convert the object into a dict
generated_file_wrapper_dict = generated_file_wrapper_instance.to_dict()
# create an instance of GeneratedFileWrapper from a dict
generated_file_wrapper_from_dict = GeneratedFileWrapper.from_dict(generated_file_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


