from distributed_logger.facade import LoggerFacade

class StormSession:
    def __init__(self, service_name, session_id, verbose=False):
        self.session_id = session_id
        self.logger = LoggerFacade.get_logger(
            name=service_name,
            verbose=verbose
        ).with_context(session_id=session_id)

    def get_logger(self):
        return self.logger
