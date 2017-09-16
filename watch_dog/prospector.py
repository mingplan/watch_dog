import time
from watch_dog.harvester import Harvester

class Prospector(object):
    def __init__(self, path_list):
	self.path_list = path_list
    def start(self, queue, cur_time=None):
	if cur_time is None:
            cur_time = time.time()
	for path_item in self.path_list:
	    queue.extend(Harvester.fetch_file(path_item, 90000, cur_time))
      
	
if __name__ == '__main__':
    path_list = ['/export/jenkins/jobs/RPT/jobs/RE/jobs/RulesEngine-FullCI-Production/jobs/*/builds/*/build.xml', 
         '/export/jenkins/jobs/RPT/jobs/Analytics/jobs/RPMA-FullCI-Production/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/Analytics/jobs/RPMA-FullCI-Master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/Analytics/jobs/RPMA-FullCI-CodeFreeze/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AdServing/jobs/ADS-CICD/jobs/Full-CI/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/MRM-BE/jobs/BE-FullCI-Master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/RE/jobs/RulesEngine-FullCI-Master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/RE/jobs/RulesEngine-FullCI-CodeFreezing/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/RE/jobs/RulesEngine-FullCI-Production/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/DF/jobs/DF-CICD/jobs/Full-CI/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/ci-pipeline-uitest-Prod/jobs/uiSolrIndex/jobs/solrindex-dep-assemble_mrm/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/ci-pipeline-uitest-Prod/jobs/uiSolrIndex/jobs/solrindex-dep-assemble_rpm/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/ci-pipeline-uitest-STG/jobs/uiSolrIndex/jobs/solrindex-dep-assemble_mrm/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/ci-pipeline-uitest-STG/jobs/uiSolrIndex/jobs/solrindex-dep-assemble_rpm/builds/*/build.xml',
    
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/code-analyze___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/multijob-rebuild-images___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/multijob-unit-test___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/rebuild-image-maui___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/rebuild-image-rpm___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/rebuild-image-uif___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/unit-test-frontend___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/unit-test-maui___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/unit-test-rpm___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/unit-test___dev/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/ut_postman/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/Pipelines/jobs/ui-ui/jobs/ut_postman_for_code_analyze/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/maui_smoke_test/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/maui_smoke_test_for_CentOS7/builds/*/build.xml',
    
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/uif-dep-assemble/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/uif-dep-assemble_centos7/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/uif-package-centos7/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/uif-package-db/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/uif-post-package/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/uif_smoke_test/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/uif_smoke_test_for_CentOS7/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-new/jobs/ui_regression_placeholder/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-package/jobs/major-release/jobs/centos7/jobs/CentOS7_deploy_package/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-package/jobs/record-package-info/builds/*/build.xml',

    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/Audience-CodeFreezing/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/Audience-Master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/Audience/jobs/Audience-trunk/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/Audience-Production/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/RBP/jobs/RBP-ComScore-CodeFreezing/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/RBP/jobs/RBP-ComScore-Master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/RBP/jobs/RBP-ComScore-Production/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/RBP/jobs/RBP-Nielsen-CodeFreezing/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/RBP/jobs/RBP-Nielsen-Master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/RBP/jobs/RBP-Nielsen-Production/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/Engine-CodeFreezing/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/Engine-RHEL7/jobs/Forecast-V_6_*-RHEL7/builds/*/build.xml',

    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/Engine-Master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/Engine-RHEL7/jobs/Forecast-Trunk-RHEL7/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/Engine-Master/jobs/4.AF_Assemble_Parallel/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/Engine-Production/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/Engine-Production/jobs/AF_Assemble_Parallel/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/S2S-Codefreezing/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/S2S-Production/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/AF/jobs/AF-FullCI/jobs/S2S-Master/jobs/*/builds/*/build.xml',

    '/export/jenkins/jobs/DB/jobs/subsystem-ci-pipeline-development-db/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/DB/jobs/subsystem-ci-pipeline-development-db/jobs/MySQL/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/DB/jobs/subsystem-ci-pipeline-development-db/jobs/MySQLIB/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/DB/jobs/subsystem-ci-pipeline-development-db-release/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/DB/jobs/subsystem-ci-pipeline-development-db-release/jobs/MySQL/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/DB/jobs/subsystem-ci-pipeline-development-db-release/jobs/MySQLIB/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/DB/jobs/DB-FULL-CI/jobs/*/builds/*/build.xml',
    
    '/export/jenkins/jobs/RPT/jobs/DF/jobs/DF-CICD/jobs/CICD-Pipeline/jobs/0-DIP-CI-Pipeline/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/DF/jobs/DF-CICD/jobs/CICD-Pipeline/jobs/DIP-Build/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/MRM-BE/jobs/Build/jobs/DAL/jobs/DAL_FullCI/jobs/DAL-FullCI-master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/Analytics/jobs/MRMA-FullCI-CodeFreeze/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/Analytics/jobs/MRMA-FullCI-Master/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/RPT/jobs/Analytics/jobs/MRMA-FullCI-Production/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-dev/jobs/*/builds/*/build.xml',
    '/export/jenkins/jobs/UI/jobs/UI-CICD/jobs/UIF/jobs/FullCI-release/jobs/*/builds/*/build.xml'
]
       
    pro = Prospector(path_list)
    queue = []
    start = time.clock()
    pro.start(queue)
    elap = time.clock() - start 
    for item in queue:
        print item
    print elap
