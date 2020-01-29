# Orgrimmar

## The problem

It is challenging for developers to identify gaps in testing after code changes. Often developers do not know what existing tests are relevant to their changes.

## The broader application

Learn about how to provide automated feedback to developer based on code commits

## Objective

Given that there are always a list of tests available for execution, we would like to experiment ways to tell developers which tests to run after code change through some level of AI.

## The input

* A simple class which serves as the system under test
* A list of tests (with just function headers) associated with the class

## Use case

* Developer make a change to existing code
* git add .
* git commit
* Run a command to trigger the tool
* Developer sees the list of tests generated to run against the code change

## Implementatiom details

### The test analyser
* Analyse code based on git commit locally
* Utilize AI/ML tooling to format each commit into a string
  * Each commit
* Some data training is applied to
  * Recognize relevance between commit and the list of tests

### The training data

### Limitations
* It currently assumes that each commit is already pre-formatted into a string that be used as training data.
