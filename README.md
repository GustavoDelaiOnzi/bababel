### Bababel

Bababel is a robust and flexible messaging consumer library designed to efficiently handle and
process messages in distributed systems. It simplifies message consumption and task execution, making it ideal for scalable applications that require asynchronous processing.

Example usage:

    from bababel.app import BababelApp

    app = BababelApp(
        host='localhost',
        port=5672,
        username='guest',
        password='guest'
    )
    from bababel.tasks.task import Task

    class SampleXpto(Task):
        def run(self, a: int, b: int):
            return a + b

    task = SampleXpto(app=app)
    task.send(a=2, b=3)

This project uses conventional commits 1.0.0
