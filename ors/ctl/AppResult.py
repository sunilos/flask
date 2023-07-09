class AppResult:

    error = False
    success = False
    message = ""
    data = {
        id: 0
    }

    def __init__(self, err,msg ):
        self.success = err
        self.message = msg

    def to_dict(self):
        return {
            'error': self.error,
            'message': self.message,
            'success' : self.success,
            'data': self.data
        }
