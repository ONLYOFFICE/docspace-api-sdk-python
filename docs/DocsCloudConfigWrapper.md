# DocsCloudConfigWrapper
The successful API response containing the DocsCloudConfig object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DocsCloudConfig**](DocsCloudConfig.md) | The DocsCloudConfig object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_config_wrapper import DocsCloudConfigWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudConfigWrapper from a JSON string
docs_cloud_config_wrapper_instance = DocsCloudConfigWrapper.from_json(json)
# print the JSON string representation of the object
print(DocsCloudConfigWrapper.to_json())

# convert the object into a dict
docs_cloud_config_wrapper_dict = docs_cloud_config_wrapper_instance.to_dict()
# create an instance of DocsCloudConfigWrapper from a dict
docs_cloud_config_wrapper_from_dict = DocsCloudConfigWrapper.from_dict(docs_cloud_config_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


