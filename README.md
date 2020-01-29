# Orgrimmar

## The problem

It is challenging for developers to identify gaps in testing after code changes. Often developers do not know what existing tests are relevant to their changes.

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

### Libraries in use

* gitpython
* tensorflow

### The tests analyser
* Analyse code based on git commit locally
  * The commit log (obtained via gitpython) is formatted into a strings that can be used as training data
* Utilize AI/ML tooling for data training and prediction
  * We use Keras RNN (Recurrent Neural Network) API of tensorflow in this exercise
    * RNN can be used in speech recognition, hand-writing, text classification, etc
  * Data training is applied to recognize relevance between commits and the list of tests; i.e. recognizing patterns in code change from commits

### The training data

### Limitations
* It currently assumes that each commit is already pre-formatted into a string that be used as training data.

## Additional findings
* Sample data needs to be large and diversified enough to produce more accurate predictions
* With the actual source code experimented in the exercise, more different classes and methods under tests result in better prediction.
* A broader application is to classify code commits, e.g. when there has been refactoring, where there are a lot of bug fixes, etc


