# .github

## Purpose

This repository stores reusable workflows for GitHub and other configuration files for use across repositories, including Renovate and Codecov.

Wherever possible, existing multi-job workflow files have been broken down to single-job workflows here so they can be mixed-and-matched.

The central workflow files live here. The templates for the files to call these are in the `workflow-templates` directory

# Contents

## Workflows

### SFDX

#### Create Scratch Org and Apex Test

Script that creates a scratch org, deploys metadata, runs Apex tests, calls other workflow, and deletes scratch org

#### Lint LWC and LWC Test

Run LWC tests

#### Prettier Verify

Ensures npm modules are installed, runs Prettier, exits with error if code is unformatted

#### SFDX Scanner

### GitHub CI

#### Release Please

#### PMD (download)

#### PMD (action)

#### Copy ApexDox Site

### Package Updates

#### Dependabot

#### Renovate

A central configuration file, `renovate.json5` is referenced from other repositories using the `renovate.json` file at `/.github/renovate.json`.

## Templates

### Bug Report

Configured with a YAML template instead of markdown, this template allows for text fields and picklists

### Feature Request

This is a more traditional markdown template
