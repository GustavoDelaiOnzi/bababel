.. _usage:


Getting started
===============

Installation
------------

To use Bababel, first install it using pip:

.. code-block:: console

   $ pip install bababel

Starting the Application
------------------------

Bababel is an asynchronous task processor. Before using it, you need to define the application and establish a
connection with the broker. Currently, only RabbitMQ is supported, but future updates aim to include additional brokers.

To start the Bababel application, follow these steps:

.. code-block:: python

   from bababel.app import BababelApp

   app = BababelApp(
       host='localhost',
       port=5672,
       username='guest',
       password='guest'
   )

Creating Tasks
--------------

Now, we need to define a task that will be processed asynchronously. Use the ``Task`` class to create tasks that BababelApp can process. Every task must implement a ``run`` method, which will be executed asynchronously by the worker.

Here is an example of a task definition:

.. code-block:: python

   from bababel.tasks.task import Task

   class SampleXpto(Task):
       def run(self, a: int, b: int):
           return a + b

Sending Tasks
-------------

To send a task to the processing queue, use the following approach:

.. code-block:: python

   task = SampleXpto(app=app)
   task.send(a=2, b=3)

Notice that when instantiating the task, you must pass the app instance as an argument. Once sent, the run
method will be executed (with the parameters given in the send method) asynchronously by the worker when it
reaches its turn in the queue.

This setup ensures efficient asynchronous processing of tasks using Bababel.

