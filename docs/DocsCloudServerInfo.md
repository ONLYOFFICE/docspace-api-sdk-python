# DocsCloudServerInfo
Represents the DocsCloud server information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The server version. | [optional] 
**package_type** | **str** | The server package type (Open Source, Enterprise Edition or Developer Edition). | [optional] 
**var_date** | **datetime** | The server build date. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_server_info import DocsCloudServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudServerInfo from a JSON string
docs_cloud_server_info_instance = DocsCloudServerInfo.from_json(json)
# print the JSON string representation of the object
print(DocsCloudServerInfo.to_json())

# convert the object into a dict
docs_cloud_server_info_dict = docs_cloud_server_info_instance.to_dict()
# create an instance of DocsCloudServerInfo from a dict
docs_cloud_server_info_from_dict = DocsCloudServerInfo.from_dict(docs_cloud_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


