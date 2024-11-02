from src.infra.JiraClient import JiraClient
from src.handlers.StatusHistoryHandler import StatusHistoryHandler


class StatusHistoryController:

    @classmethod
    def get_issue_status_history(cls, issue_key, time_format):
        issue = JiraClient.get_issue_by_key(issue_key=issue_key, expand='changelog')
        issue_changes_history = issue.raw['changelog']['histories']
        return StatusHistoryHandler.get_issue_status_history(issue_changes_history, time_format=time_format)
