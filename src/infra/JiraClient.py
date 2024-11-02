from jira import JIRA, Issue
from os import getenv


class JiraClient:
    token = getenv("JIRA_TOKEN")
    server = getenv("JIRA_HOST")

    @classmethod
    def get_issue_by_key(cls, issue_key: str, expand: str) -> Issue:
        session = JIRA(server=cls.server, token_auth=cls.token)
        issue = session.issue(id=issue_key, expand=expand)
        session.close()
        return issue

    @classmethod
    def get_issues_by_filter(cls, issue_filter: str, expand) -> list:
        session = JIRA(server=cls.server, token_auth=cls.token)
        issues = session.search_issues(jql_str=issue_filter,
                                       expand=expand,
                                       maxResults=False)
        session.close()
        return issues
