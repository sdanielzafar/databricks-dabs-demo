.github/workflows/ 
│ └─ CI.yml                   # GitHub action when pull request is created to main branch
│ └─ CD.yml                   # GitHub action when pull request is merged to main branch
cicd_demo/ 
│ └─ resources/
│       └─ int-test.yml       # job configuration for integration test
│       └─ actual-job.yml     # prod job configuration 
│ └─ tests/                   # some unit tests
│ └─ databricks.yml           # bundle definition where resources, parameters, environments are defined
│ └─ StreamingAggNotebook.py  # databricks notebook called in the jobs above
