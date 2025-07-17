# CreateDefectApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_result_ids** | **List[str]** | Linked test result IDs | 
**form** | [**ExternalFormCreateModel**](ExternalFormCreateModel.md) | External form definition | 

## Example

```python
from testit_api_client.models.create_defect_api_model import CreateDefectApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDefectApiModel from a JSON string
create_defect_api_model_instance = CreateDefectApiModel.from_json(json)
# print the JSON string representation of the object
print CreateDefectApiModel.to_json()

# convert the object into a dict
create_defect_api_model_dict = create_defect_api_model_instance.to_dict()
# create an instance of CreateDefectApiModel from a dict
create_defect_api_model_from_dict = CreateDefectApiModel.from_dict(create_defect_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


