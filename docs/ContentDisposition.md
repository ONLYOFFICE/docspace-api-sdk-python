# ContentDisposition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disposition_type** | **str** |  | [optional] 
**parameters** | **List[object]** |  | [optional] [readonly] 
**file_name** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**modification_date** | **datetime** |  | [optional] 
**inline** | **bool** |  | [optional] 
**read_date** | **datetime** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.content_disposition import ContentDisposition

# TODO update the JSON string below
json = "{}"
# create an instance of ContentDisposition from a JSON string
content_disposition_instance = ContentDisposition.from_json(json)
# print the JSON string representation of the object
print(ContentDisposition.to_json())

# convert the object into a dict
content_disposition_dict = content_disposition_instance.to_dict()
# create an instance of ContentDisposition from a dict
content_disposition_from_dict = ContentDisposition.from_dict(content_disposition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


