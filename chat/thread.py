from threading import Thread


class ChatThread(Thread):
    def run(self):
        result = None
        try:
            if self._target:
                result = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
        
        return result
