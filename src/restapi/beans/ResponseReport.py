from json import JSONEncoder


class ResponseReport:

    def __init__(self, status=None, finished=None, file_spreadsheet=None, file_html=None):
        self.status = status
        self.finished = finished
        self.file_spreadsheet = file_spreadsheet
        self.file_html = file_html

    @property
    def status_attr(self):
        return self.status

    @status_attr.setter
    def status_attr(self, status):
        self.status = status

    @property
    def finished_attr(self):
        return self.finished

    @finished_attr.setter
    def finished_attr(self, finished):
        self.finished = finished

    @property
    def file_spreadsheet_attr(self):
        return self.file_spreadsheet

    @file_spreadsheet_attr.setter
    def file_spreadsheet_attr(self, file_spreadsheet):
        self.file_spreadsheet = file_spreadsheet

    @property
    def file_html_attr(self):
        return self.file_html

    @file_html_attr.setter
    def file_html_attr(self, file_html):
        self.file_html = file_html
