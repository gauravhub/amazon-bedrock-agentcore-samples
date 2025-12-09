"""Filter out noisy a2a.server traces."""

from opentelemetry.sdk.trace import SpanProcessor, ReadableSpan


class A2AServerSpanFilter(SpanProcessor):
    """Filters out a2a.server spans from traces."""

    def __init__(self, next_processor: SpanProcessor):
        self._next = next_processor

    def on_start(self, span, parent_context=None):
        self._next.on_start(span, parent_context)

    def on_end(self, span: ReadableSpan):
        # Skip a2a.server spans
        if "a2a.server" in span.name:
            return
        self._next.on_end(span)

    def shutdown(self):
        self._next.shutdown()

    def force_flush(self, timeout_millis=30000):
        return self._next.force_flush(timeout_millis)

