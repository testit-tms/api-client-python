# UpdateLinkShortModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActionUpdate**](ActionUpdate.md) |  | 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.update_link_short_model import UpdateLinkShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLinkShortModel from a JSON string
update_link_short_model_instance = UpdateLinkShortModel.from_json(json)
# print the JSON string representation of the object
print(UpdateLinkShortModel.to_json())

# convert the object into a dict
update_link_short_model_dict = update_link_short_model_instance.to_dict()
# create an instance of UpdateLinkShortModel from a dict
update_link_short_model_from_dict = UpdateLinkShortModel.from_dict(update_link_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


