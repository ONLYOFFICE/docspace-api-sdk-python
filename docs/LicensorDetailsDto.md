# LicensorDetailsDto
The vendor details of the installation in the shape the licensor listing and the reset of the company details  return, with the licensor flag spelled `IsLicensor`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | The vendor name the About page shows and the letters sign off with. Until details are saved it holds  whatever the installation ships as its built-in vendor, and it is empty on an installation that ships none. | [optional] 
**site** | **str** | The address the vendor name links to, as an absolute URL with its scheme. Empty under the same conditions  as `companyName`. | [optional] 
**email** | **str** | The mailbox the About page offers for reaching the vendor. It is not the portal's own support address, and  it is empty under the same conditions as `companyName`. | [optional] 
**address** | **str** | The postal address of the vendor as one free-form line, in the shape it was saved in - no structure is  imposed on it. | [optional] 
**phone** | **str** | The telephone number of the vendor in the shape it was saved in, with no dialling format enforced. | [optional] 
**is_licensor** | **bool** | Whether these details are those of the licensor of the product itself rather than of a reseller. Saving  through `POST api/2.0/settings/rebranding/company` always clears it, so only details that came with the  installation can report `true`. The name starts with a capital letter, unlike the other fields. | [optional] 
**hide_about** | **bool** | Whether the About page is hidden from the interface. A plan that does not include branding cannot switch it  on: the value is stored as `false` in that case, so it can come back different from what was saved. | [optional] 
**last_modified** | **datetime** | When these details were last stored. Details that were never stored report the moment they were read; the  built-in ONLYOFFICE entry and the answer of the reset operation report `0001-01-01T00:00:00`. | [optional] 

## Example

```python
from docspace_api_sdk.models.licensor_details_dto import LicensorDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of LicensorDetailsDto from a JSON string
licensor_details_dto_instance = LicensorDetailsDto.from_json(json)
# print the JSON string representation of the object
print(LicensorDetailsDto.to_json())

# convert the object into a dict
licensor_details_dto_dict = licensor_details_dto_instance.to_dict()
# create an instance of LicensorDetailsDto from a dict
licensor_details_dto_from_dict = LicensorDetailsDto.from_dict(licensor_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


