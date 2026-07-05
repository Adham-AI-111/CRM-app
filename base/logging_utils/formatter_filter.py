import json
import logging
import datetime

# this line here not in the method, to avoid create tens or thousands of STANDARD_LOG_RECORD_FIELDS
STANDARD_LOG_RECORD_FIELDS = set(
            logging.makeLogRecord({}).__dict__.keys()
        )


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        log = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "function": record.funcName,
            "line": record.lineno,
        }
        extra_log = {log_key : log_val for log_key, log_val in record.__dict__.items() if log_key not in STANDARD_LOG_RECORD_FIELDS}
        full_log = log | extra_log

        return json.dumps(full_log, default=str)
