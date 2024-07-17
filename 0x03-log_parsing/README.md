# Log Parsing

## Description

This project is about parsing log files. The log files are in the following format:

```
<date> <time> <log level> <message>
```

The date is in the format `YYYY-MM-DD`, the time is in the format `HH:MM:SS`, the log level is one of `INFO`, `WARNING`, `ERROR`, and the message is a string.

The log files are stored in a directory. The directory contains multiple log files. Each log file contains multiple log entries. The log entries are separated by a newline character.

The project should provide the following functionality:

1. Parse the log files and store the log entries in a database.
2. Provide an API to query the log entries.

## Requirements

1. The project should be implemented in Python.
2. The project should use SQLite as the database.
3. The project should provide a command-line interface to parse the log files and query the log entries.
4. The project should provide a RESTful API to query the log entries.
