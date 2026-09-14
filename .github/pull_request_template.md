# Pull Request: Merge adf_publish to main

## Description
This pull request merges all changes from the `adf_publish` branch into the `main` branch.

## Changes Included
- **Pipelines Updated**: 
  - PL_GITHUB_TO_ADLS_RAW_DYNAMIC
  - PL_RAW_TO_BRONZE
  
- **Datasets Updated**:
  - DS_ADLS_RAW_BRONZE_FOLDER
  - DS_ADLS_RAW_EMR
  - DS_ADLS_RAW_EMR_FOLDER
  - DS_GITHUB_EMR
  
- **Linked Services Updated**:
  - LS_GITHUB_HTTP
  - LS_ADLS_EMR
  
- **New Resources Added**:
  - Pipeline: FINAL-GIT-BRONZ
  - Factory: adf-emr-healthcare

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [x] New feature (non-breaking change which adds functionality)
- [x] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## Testing
All changes have been tested in the development environment.

## Checklist
- [x] My code follows the style guidelines of this project
- [x] I have performed a self-review of my own code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] My changes generate no new warnings
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] New and existing unit tests passed locally with my changes
