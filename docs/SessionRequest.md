# SessionRequest
The file a chunked upload session is opened for, and how a clash with an existing name is settled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The name to store the file under, extension included. Characters a title cannot hold are replaced and the name  is truncated, so the stored title can differ from the one sent. | 
**file_size** | **int** | The exact number of bytes that will be sent. The size is reserved when the session opens and compared with the  parts as they arrive; below the portal chunk size the session takes the whole payload in one part, and above  the portal limit for chunked uploads it is refused. | [optional] 
**relative_path** | **str** | A slash-separated chain of folder titles under the target folder to store the file in; folders in the chain  that do not exist yet are created. Leave it empty to store the file in the folder from the path itself. | [optional] 
**create_on** | [**ApiDateTime**](ApiDateTime.md) | The creation time to stamp on a newly created file instead of the moment the upload finishes. It is ignored  when the upload lands on a file that already exists. | [optional] 
**encrypted** | **bool** | Marks the stored file as client-side encrypted, which is how content uploaded into a private room is kept;  with false the bytes are stored as they arrive. | [optional] 
**create_new_if_exist** | **bool** | Settles the clash when the folder already holds a file with this name: true stores the upload beside it under  a name with a numeric suffix, false takes the existing file over and adds the content to it as a new version. | [optional] 

## Example

```python
from docspace_api_sdk.models.session_request import SessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SessionRequest from a JSON string
session_request_instance = SessionRequest.from_json(json)
# print the JSON string representation of the object
print(SessionRequest.to_json())

# convert the object into a dict
session_request_dict = session_request_instance.to_dict()
# create an instance of SessionRequest from a dict
session_request_from_dict = SessionRequest.from_dict(session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


