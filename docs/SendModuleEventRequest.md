# SendModuleEventRequest
A socket event from an integration module: who receives it in the portal, its name and its payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room** | **str** | A room of the module in this portal: everyone subscribed to `plugin-{module}-{room}` receives the event. Latin  letters, digits and the characters `_ . : -`. | [optional] 
**user** | **str** | The e-mail of the portal user who receives the event; with single sign-on it is the same e-mail the module's own  application knows the person by. Only that user's open sessions receive it. | [optional] 
**event** | **str** | The event name. Browsers receive it as `plugin:{module}:{event}`. Latin letters, digits and the characters  `_ . : -`. | [optional] 
**message** | **str** | Passed to the browser as it is, as `{ message }`. Meant as a signal to re-read, such as an unread count; use  JSON text for structured data and keep personal content out of it. | [optional] 

## Example

```python
from docspace_api_sdk.models.send_module_event_request import SendModuleEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendModuleEventRequest from a JSON string
send_module_event_request_instance = SendModuleEventRequest.from_json(json)
# print the JSON string representation of the object
print(SendModuleEventRequest.to_json())

# convert the object into a dict
send_module_event_request_dict = send_module_event_request_instance.to_dict()
# create an instance of SendModuleEventRequest from a dict
send_module_event_request_from_dict = SendModuleEventRequest.from_dict(send_module_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


