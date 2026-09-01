# BackupsCountResultWrapper
The successful API response containing the BackupsCountResultDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BackupsCountResultDto**](BackupsCountResultDto.md) | The BackupsCountResultDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.backups_count_result_wrapper import BackupsCountResultWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of BackupsCountResultWrapper from a JSON string
backups_count_result_wrapper_instance = BackupsCountResultWrapper.from_json(json)
# print the JSON string representation of the object
print(BackupsCountResultWrapper.to_json())

# convert the object into a dict
backups_count_result_wrapper_dict = backups_count_result_wrapper_instance.to_dict()
# create an instance of BackupsCountResultWrapper from a dict
backups_count_result_wrapper_from_dict = BackupsCountResultWrapper.from_dict(backups_count_result_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


