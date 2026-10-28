# DocsCloudServerInfoDto
Represents the Docs Connect server information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The server version. | [optional] 
**package_type** | **str** | The server package type (Open Source, Enterprise Edition or Developer Edition). | [optional] 
**var_date** | **datetime** | The server build date. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_server_info_dto import DocsCloudServerInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudServerInfoDto from a JSON string
docs_cloud_server_info_dto_instance = DocsCloudServerInfoDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudServerInfoDto.to_json())

# convert the object into a dict
docs_cloud_server_info_dto_dict = docs_cloud_server_info_dto_instance.to_dict()
# create an instance of DocsCloudServerInfoDto from a dict
docs_cloud_server_info_dto_from_dict = DocsCloudServerInfoDto.from_dict(docs_cloud_server_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


