# AutoTestPostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | Specifies the ID of your autotest in the external system.&lt;br /&gt;  To test the method, you can use any ID. | 
**project_id** | **str** | Specifies the project GUID.&lt;br /&gt;  You can get it using the &#x60;GET /api/v2/projects&#x60; method. | 
**name** | **str** | Specifies autotest name in the test management system. | 
**work_item_ids_for_link_with_auto_test** | **[str], none_type** | Specifies the IDs of work items to link your autotest to. You can specify several IDs. | [optional] 
**should_create_work_item** | **bool** | Creates a test case linked to the autotest. | [optional] 
**links** | [**[LinkPostModel], none_type**](LinkPostModel.md) | Specifies the links in the autotest. | [optional] 
**namespace** | **str, none_type** | Specifies the name of the namespace in the test management system. | [optional] 
**classname** | **str, none_type** | Specifies the class name in the test management system. | [optional] 
**steps** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Specifies the steps in the autotest. | [optional] 
**setup** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Specifies the setup steps and relates them to the autotest. Supported values are the same as in the &#x60;steps&#x60; parameter. | [optional] 
**teardown** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) | Specifies the teardown steps and relates them to the autotest. Supported values are the same as in the &#x60;steps&#x60; parameter. | [optional] 
**title** | **str, none_type** | Specifies the name of the autotest in the autotest card.   The &#x60;Name&#x60; parameter is responsible for the name in the table. | [optional] 
**description** | **str, none_type** | Specifies the autotest description in the test management system. | [optional] 
**labels** | [**[LabelPostModel], none_type**](LabelPostModel.md) | Specifies autotest labels. | [optional] 
**is_flaky** | **bool** | Marks the autotest as flaky. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


