# AiAgentsUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | Profile id to rebind (optional). | [optional] 
**chat_settings** | **object** | Chat settings (`ChatSettings`); requires a valid provider/model. | [optional] 
**send_form_to_external_db** | **bool** | Whether form results are sent to an external DB. | [optional] 
**save_form_as_xlsx** | **bool** | Whether forms are saved as XLSX. | [optional] 
**title** | **str** | Agent (room) title. | [optional] 
**quota** | **float** | Room quota in bytes. | [optional] 
**indexing** | **bool** | Whether room content is indexed for search. | [optional] 
**deny_download** | **bool** | Whether downloading room content is denied. | [optional] 
**lifetime** | **object** | Room data lifetime policy (`RoomDataLifetimeDto`). | [optional] 
**watermark** | **object** | Watermark settings (`WatermarkRequestDto`). | [optional] 
**logo** | **object** | Room logo (`LogoRequest`). | [optional] 
**tags** | **List[str]** | Room tags. | [optional] 
**color** | **str** | Room accent color. | [optional] 
**cover** | **str** | Room cover image id. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_agents_update_request import AiAgentsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAgentsUpdateRequest from a JSON string
ai_agents_update_request_instance = AiAgentsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AiAgentsUpdateRequest.to_json())

# convert the object into a dict
ai_agents_update_request_dict = ai_agents_update_request_instance.to_dict()
# create an instance of AiAgentsUpdateRequest from a dict
ai_agents_update_request_from_dict = AiAgentsUpdateRequest.from_dict(ai_agents_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


