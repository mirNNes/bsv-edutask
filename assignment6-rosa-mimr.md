# Assignment 6

Team Members:  
Robin Sanssi (rosa24)  
Mirnes Mrso (mimr24)

Group Number:  
35

Repository Link:  
https://github.com/mirNNes/bsv-edutask

## Work distribution

The work was divided between us both. Robin prepared the initial draft for the workflow and code fix, and Mirnes reviewed and checked the result. All parts were discussed and checked by us both.

## 1. Continuous Integration of Backend Unit Tests

For this assignment, we created a GitHub Actions workflow that automatically runs the backend unit tests.

The workflow installs the backend dependencies and executes the unit tests with Pytest:

```text
pytest -m unit
```

The workflow file is located at:

`.github/workflows/backend-unit-tests.yml`

The workflow executions can be found here:

https://github.com/mirNNes/bsv-edutask/actions

We also opened a pull request that fixes the get_user_by_email method in backend/src/controllers/usercontroller.py.

The fix makes the method:

- return None when no user is found
- reject email addresses that do not follow the expected format

The pull request can be found here:

https://github.com/mirNNes/bsv-edutask/pull/1

The pull request shows that the backend unit tests pass successfully. The pull request has been left open for grading.
