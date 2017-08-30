"""
Integration contains everything that's required to run integration
tests for a Wallaro application (Python, Pony, or otherwise) via a Python
script.

It has:
    - TCPReceiver: a multi-client TCP sink receiver
    - Metrics: an alias for TCPReceiver
    - Sink: an alias for TCPReceiver
    - Sender: a TCP sender
    - Reader: a buffered reader interface wrapper for bytestream generators
    - files_generator: a file source supporting both newlines and framed modes
    - sequence_generator: a framed source encoded U64 sequence generator
        (binary)
    - iter_generator: a generic framed source encoded generator that operates on
        iterators. It takes an optional `to_string` lambda for converting
        iterator items to strings.
    - files_generator: a generic
    - Runner: Runs a single Wallaroo worker with command line parameters.
    - ex_validation: a function to execute external validation commands and
      capture their outputs

You will need to include /testing/tools in your PYTHONPATH, and the
application binary in your PATH before running your integration test.

Below is an example for running the integration test on reverse, a
python-wallaroo application, using the machida binary, the wallaroo python
api, and the the integration tester utility. The integration test script
can be found at
https://github.com/Sendence/wallaroo/examples/python/reverse/_test.py.

```bash
# Add integration utility to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:~/wallaroo-tutorial/wallaroo/testing/tools"
# Add wallaroo to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:~/wallaroo-tutorial/wallaroo/machida:."
# Add machida to PATH
export PATH="%PATH:~/wallaroo-tutorial/wallaroo/machida/build"

# Run integration test
python2 -m pytest _test.py --verbose
```


Alternatively, for a CLI style integration tester, you may use the
`integration_test` CLI. Add
`~/wallaroo-tutorial/wallaroo/testing/tools/integration` to your PATH, then
`integration_test -h` for instructions.
"""


from integration import (clean_up_resilience_path,
                         ex_validate,
                         files_generator,
                         get_port_values,
                         is_address_available,
                         iter_generator,
                         Metrics,
                         MetricsStopper,
                         Reader,
                         Runner,
                         RunnerChecker,
                         RunnerReadyChecker,
                         Sender,
                         sequence_generator,
                         setup_resilience_path,
                         start_runners,
                         pipeline_test,
                         Sink,
                         SinkAwaitValue,
                         SinkExpect,
                         TCPReceiver,
                         TimeoutError)
