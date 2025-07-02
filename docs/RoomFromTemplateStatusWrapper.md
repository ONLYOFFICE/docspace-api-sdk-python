# RoomFromTemplateStatusWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**RoomFromTemplateStatusDto**](RoomFromTemplateStatusDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.room_from_template_status_wrapper import RoomFromTemplateStatusWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of RoomFromTemplateStatusWrapper from a JSON string
room_from_template_status_wrapper_instance = RoomFromTemplateStatusWrapper.from_json(json)
# print the JSON string representation of the object
print(RoomFromTemplateStatusWrapper.to_json())

# convert the object into a dict
room_from_template_status_wrapper_dict = room_from_template_status_wrapper_instance.to_dict()
# create an instance of RoomFromTemplateStatusWrapper from a dict
room_from_template_status_wrapper_from_dict = RoomFromTemplateStatusWrapper.from_dict(room_from_template_status_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


