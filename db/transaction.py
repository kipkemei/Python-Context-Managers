import contextlib


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self0):
        self.conn._rollback_transaction(self.xid)

@contextlib.contextmanager
def _start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield tx
    except:
        tx.rollback()
        raise

    tx.commit()