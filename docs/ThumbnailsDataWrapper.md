# ThumbnailsDataWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ThumbnailsDataDto**](ThumbnailsDataDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.thumbnails_data_wrapper import ThumbnailsDataWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ThumbnailsDataWrapper from a JSON string
thumbnails_data_wrapper_instance = ThumbnailsDataWrapper.from_json(json)
# print the JSON string representation of the object
print(ThumbnailsDataWrapper.to_json())

# convert the object into a dict
thumbnails_data_wrapper_dict = thumbnails_data_wrapper_instance.to_dict()
# create an instance of ThumbnailsDataWrapper from a dict
thumbnails_data_wrapper_from_dict = ThumbnailsDataWrapper.from_dict(thumbnails_data_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


