# LoginEventDto
The login event parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The login event ID. | [optional] 
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**user** | **str** | The user name of the login event. | [optional] 
**user_id** | **str** | The user ID of the login event. | [optional] 
**login** | **str** | The user login of the login event. | [optional] 
**action** | **str** | The login event action. | [optional] 
**action_id** | [**MessageAction**](MessageAction.md) |  | [optional] 
**ip** | **str** | The login event IP. | [optional] 
**country** | **str** | The login event country. | [optional] 
**city** | **str** | The login event city. | [optional] 
**browser** | **str** | The login event browser. | [optional] 
**platform** | **str** | The login event platform. | [optional] 
**page** | **str** | The login event page. | [optional] 

## Example

```python
from docspace-api-python.models.login_event_dto import LoginEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of LoginEventDto from a JSON string
login_event_dto_instance = LoginEventDto.from_json(json)
# print the JSON string representation of the object
print(LoginEventDto.to_json())

# convert the object into a dict
login_event_dto_dict = login_event_dto_instance.to_dict()
# create an instance of LoginEventDto from a dict
login_event_dto_from_dict = LoginEventDto.from_dict(login_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


