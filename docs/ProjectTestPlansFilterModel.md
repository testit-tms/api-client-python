# ProjectTestPlansFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**build** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**List[TestPlanStatusModel]**](TestPlanStatusModel.md) |  | [optional] 
**global_ids** | **List[int]** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**locked_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**automatic_duration_timer** | **List[bool]** |  | [optional] 
**created_by_ids** | **List[str]** |  | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**start_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**end_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**tag_names** | **List[str]** |  | [optional] 
**attributes** | **Dict[str, Optional[List[str]]]** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from testit_api_client.models.project_test_plans_filter_model import ProjectTestPlansFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTestPlansFilterModel from a JSON string
project_test_plans_filter_model_instance = ProjectTestPlansFilterModel.from_json(json)
# print the JSON string representation of the object
print(ProjectTestPlansFilterModel.to_json())

# convert the object into a dict
project_test_plans_filter_model_dict = project_test_plans_filter_model_instance.to_dict()
# create an instance of ProjectTestPlansFilterModel from a dict
project_test_plans_filter_model_from_dict = ProjectTestPlansFilterModel.from_dict(project_test_plans_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


