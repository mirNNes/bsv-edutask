# Assignment 3 - Integration Testing

## Work distribution

The work was divided between us both. Robin prepared the initial draft for the written explanation, and Mirnes reviewed and refined the text. The content was discussed and checked by us both.

---

## 1. Test Levels

### Difference in scope

Unit tests and integration tests differ mainly in scope.

A unit test focuses on one small part of the system in isolation, it could be something like a single method, function, or class. The purpose is to check whether that specific unit behaves correctly on its own.

An integration test focuses on how different parts of the system work together. Instead of testing one isolated unit, it tests the communication or cooperation between different components.

---

### Purpose of mocking in unit and integration tests

In unit testing, mocking is mainly used to isolate the unit under test.

This means that dependencies such as databases, APIs, or other classes are replaced by fake objects so that the test only checks the logic of the specific unit. Mocking also makes unit tests faster, more controlled, and easier to repeat, because the result does not depend on external systems.

For example, in Assignment 2 the DAO was mocked when testing `get_user_by_email()`. This allowed the test to focus only on the controller logic, without depending on whether the database was running or not.

But in integration testing, mocking has a different role.

The main goal of an integration test is to verify that multiple components actually work well together. Because of that, the integration should usually not be mocked away. If the communication between two components is replaced by mocks, then the real integration is actually no longer being tested in reality.

Mocking can still be useful in integration tests, but only for parts that are outside the scope of the test or that would make the test unnecessarily difficult to control. But the key difference here is that the actual central interaction being tested must actually be real.

---

## 2. Integration Testing

For this part, we focused on the communication between `DAO.create()` and MongoDB. The goal was to check that object creation works correctly together with the validator of the `user` collection.

### Test design

We took the test cases from the validator for `user` and from the expected behavior of `DAO.create()`.

To use the test design technique, we first identified the main conditions that affect the result. After that, we created test cases and wrote what we expected to happen in each case.

The main conditions we used were these parts:

- valid user data
- missing required field
- wrong data type
- duplicate email

From these conditions, we defined the following test cases:

1. Create a user with valid data.
   Expected outcome: the user should be created and returned with an `_id`.

2. Create a user with a missing required field.
   Expected outcome: creation should fail with a database write error.

3. Create a user with a wrong field type.
   Expected outcome: creation should fail with a database write error.

4. Create two users with the same email.
   Expected outcome: the second creation should fail with a database write error.

---

### Pytest fixture

We implemented a pytest fixture that connects to a separate test collection called `user_test` in MongoDB. The fixture uses `yield`, which means that it first sets up the test environment and then makes sure to clean it up after the test has finished.

---

### Test implementation

The integration tests were implemented in:

`backend/test/integration/test_dao_create.py`

---

### Test execution result

We ran the integration tests with pytest. The console output looked like this:

```text
...F                                                                                                                     [100%]
FAILED test/integration/test_dao_create.py::test_create_user_fails_for_duplicated_email - Failed: DID NOT RAISE <class 'pymongo.errors.WriteError'>
1 failed, 3 passed in 1.18s
```

Brief evaluation:

The test execution shows that three integration tests passed. This means that `DAO.create()` works as expected for valid input, missing required data, and wrong data types. One test failed: creating two users with the same email did not raise a write error. This indicates that duplicate emails are currently not rejected by the system, even though the validator suggests that this should happen.
