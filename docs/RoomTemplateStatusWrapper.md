# RoomTemplateStatusWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**RoomTemplateStatusDto**](RoomTemplateStatusDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.room_template_status_wrapper import RoomTemplateStatusWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTemplateStatusWrapper from a JSON string
room_template_status_wrapper_instance = RoomTemplateStatusWrapper.from_json(json)
# print the JSON string representation of the object
print(RoomTemplateStatusWrapper.to_json())

# convert the object into a dict
room_template_status_wrapper_dict = room_template_status_wrapper_instance.to_dict()
# create an instance of RoomTemplateStatusWrapper from a dict
room_template_status_wrapper_from_dict = RoomTemplateStatusWrapper.from_dict(room_template_status_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


