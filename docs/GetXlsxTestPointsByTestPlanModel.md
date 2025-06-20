# GetXlsxTestPointsByTestPlanModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_name** | **bool** |  | 
**include_section** | **bool** |  | 
**include_priority** | **bool** |  | 
**include_source_type** | **bool** |  | 
**include_automated** | **bool** |  | 
**include_status** | **bool** |  | 
**include_duration** | **bool** |  | 
**include_creation_date** | **bool** |  | 
**include_author** | **bool** |  | 
**include_modification_date** | **bool** |  | 
**include_modified_by** | **bool** |  | 
**include_tags** | **bool** |  | 
**include_iterations** | **bool** |  | 
**custom_attributes_ids** | **List[str]** |  | [optional] 
**configuration_ids** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.get_xlsx_test_points_by_test_plan_model import GetXlsxTestPointsByTestPlanModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetXlsxTestPointsByTestPlanModel from a JSON string
get_xlsx_test_points_by_test_plan_model_instance = GetXlsxTestPointsByTestPlanModel.from_json(json)
# print the JSON string representation of the object
print(GetXlsxTestPointsByTestPlanModel.to_json())

# convert the object into a dict
get_xlsx_test_points_by_test_plan_model_dict = get_xlsx_test_points_by_test_plan_model_instance.to_dict()
# create an instance of GetXlsxTestPointsByTestPlanModel from a dict
get_xlsx_test_points_by_test_plan_model_from_dict = GetXlsxTestPointsByTestPlanModel.from_dict(get_xlsx_test_points_by_test_plan_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


