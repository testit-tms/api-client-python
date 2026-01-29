# AutoTestUpdateApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | External ID of the autotest | 
**project_id** | **str** | Unique ID of the autotest project | 
**name** | **str** | Name of the autotest | 
**id** | **str, none_type** | Autotest unique internal identifier | [optional] 
**external_key** | **str, none_type** | External key of the autotest | [optional] 
**namespace** | **str, none_type** | Name of the autotest namespace | [optional] 
**classname** | **str, none_type** | Name of the autotest class | [optional] 
**steps** | [**[AutoTestStepApiModel], none_type**](AutoTestStepApiModel.md) | Collection of the autotest steps | [optional] 
**setup** | [**[AutoTestStepApiModel], none_type**](AutoTestStepApiModel.md) | Collection of the autotest setup steps | [optional] 
**teardown** | [**[AutoTestStepApiModel], none_type**](AutoTestStepApiModel.md) | Collection of the autotest teardown steps | [optional] 
**title** | **str, none_type** | Name of the autotest in autotest&#39;s card | [optional] 
**description** | **str, none_type** | Description of the autotest in autotest&#39;s card | [optional] 
**labels** | [**[LabelApiModel], none_type**](LabelApiModel.md) | Collection of the autotest labels | [optional] 
**links** | [**[LinkUpdateApiModel], none_type**](LinkUpdateApiModel.md) | Collection of the autotest links | [optional] 
**is_flaky** | **bool, none_type** | Indicates if the autotest is marked as flaky | [optional] 
**work_item_ids_for_link_with_auto_test** | **[str], none_type** | Specifies the IDs of work items to link your autotest to. You can specify several IDs. | [optional] 
**work_item_ids** | **[str], none_type** | Specifies the IDs of work items to link your autotest to. You can specify several IDs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


