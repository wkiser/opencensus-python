# Copyright 2017, OpenCensus Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Export the spans data to python logging."""

import logging

from opencensus.trace.exporters import base


class LoggingExporter(base.Exporter):
    """A exporter to export the spans data to python logging. Also can use
    handlers like CloudLoggingHandler to log to Stackdriver Logging API.

    :type handler: :class:`logging.handler`
    :param handler: the handler to attach to the global handler

    Example:

    .. code-block:: python

        import google.cloud.logging
        from google.cloud.logging.handlers import CloudLoggingHandler
        from opencensus.trace.exporters import logging_exporter

        client = google.cloud.logging.Client()
        cloud_handler = CloudLoggingHandler(client)
        exporter = logging_exporter.LoggingExporter(handler=cloud_handler)

        exporter.export(your_spans_list)

    Or initialize a context tracer with the logging exporter, then the traces
    will be exported to logging when finished.
    """

    def __init__(self, handler=None):
        self.logger = logging.getLogger()

        if handler is None:
            handler = logging.StreamHandler()

        self.handler = handler
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def export(self, trace):
        """
        :type traces: dict
        :param traces: Trace collected.
        """
        self.logger.info(trace)