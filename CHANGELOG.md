## Unreleased

### Feat

- **utils**: add __init__.py to the package
- **task**: raise TaskError for invalid argument types in signature binding
- **exceptions**: add TaskError exception class extending BababelError
- **exceptions**: add BababelError base exception class
- **publisher**: enhance Publisher class with publish method and refactor initialization
- **task**: implement Singleton pattern in Task class and add consumer parameter
- **consumer**: implement IConsumer interface in Consumer class
- **pre-commit**: add Commitizen changelog hook to pre-commit configuration
- **publisher**: implement IPublisher interface in Publisher class
- create BababelApp object
- add Task class
- WIP publisher
- **worker**: change consume_bind to declare_bind
- **worker**: add start method

### Fix

- **exceptions**: initialize module with __init__.py
- fix circular import of babebel app and publisher
- **pre-commit**: remove local cz-changelog hook from pre-commit configuration
- **task**: raise NotImplementedError in run method of abstract class
- **task**: add __init__.py

### Refactor

- rename test_worker.py to test_consumer.py
- **consumer**: remove interfaces
- code convention
- **publisher**: type hint client attribute as IClient in Publisher class
- **tests**: simplify RabbitMQClient test methods
- change name Wokrer -> Consumer

## 0.3.3 (2025-02-20)

### Fix

- **pyproject.toml**: fix packages

## 0.3.2 (2025-02-20)

### Fix

- fix Worker import

## 0.3.1 (2025-02-20)

### Fix

- **Worker**: attribute name

### Refactor

- **makefile**: aff missing .PHONY
- **makefile**: add code-convention
- **.pre-commit-config.yaml**: remove black from pre-commit
- add .coveragerc
- **makefile**: add clean

## 0.3.0 (2025-02-20)

### Fix

- fix Worker import from module

## 0.2.0 (2025-02-19)

### Feat

- add consume method

### Refactor

- **Worker**: change worker method name
- change connection behavior
- rename rabbitmq.client to rabbitmq.rabbitmq_client
- add Connection abstract class
- add bind to worker __init__
- **Worker**: remove _set_client method

## 0.1.2 (2025-02-15)

### Fix

- fix build

## 0.1.1 (2025-02-15)

### Fix

- **pyproject.toml**: add license-files to [project]

## 0.1.0 (2025-02-15)

### Feat

- first commit
