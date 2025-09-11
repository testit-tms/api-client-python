# AutoTestPostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | External ID of the autotest | 
**project_id** | **str** | Unique ID of the autotest project | 
**name** | **str** | Name of the autotest | 
**work_item_ids_for_link_with_auto_test** | **[str], none_type** | Specifies the IDs of work items to link your autotest to. You can specify several IDs. | [optional] 
**work_item_ids** | **[str], none_type** | Specifies the IDs of work items to link your autotest to. You can specify several IDs. | [optional] 
**should_create_work_item** | **bool, none_type** | Creates a test case linked to the autotest. | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Key value pair of custom work item attributes | [optional] 
**links** | [**[LinkPostModel], none_type**](LinkPostModel.md) | Collection of the autotest links | [optional] 
**namespace** | **str, none_type** | Name of the autotest namespace | [optional] 
**classname** | **str, none_type** | Name of the autotest class | [optional] 
**steps** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Collection of the autotest steps | [optional] 
**setup** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Collection of the autotest setup steps | [optional] 
**teardown** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Collection of the autotest teardown steps | [optional] 
**title** | **str, none_type** | Name of the autotest in autotest&#39;s card | [optional] 
**description** | **str, none_type** | Description of the autotest in autotest&#39;s card | [optional] 
**labels** | [**[LabelPostModel], none_type**](LabelPostModel.md) | Collection of the autotest labels | [optional] 
**is_flaky** | **bool, none_type** | Indicates if the autotest is marked as flaky | [optional] 
**external_key** | **str, none_type** | External key of the autotest | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


