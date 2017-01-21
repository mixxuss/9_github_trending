import requests
import datetime


API_RESOURCE = 'https://api.github.com/search/repositories'


def get_trending_repositories(results_count):
    PERIOD = str(datetime.date.today() - datetime.timedelta(days=7))
    request_params = {'q': 'created:>{}'.format(PERIOD),
                      'sort': 'stars',
                      'order': 'desc',
                      'per_page': str(results_count)}
    repos = requests.get(API_RESOURCE, request_params)
    return repos.json()['items']


def get_open_issues_amount(all_repos):
    repos_issue = {}
    for repo in all_repos:
        repos_issue[repo['html_url']] = repo['open_issues']
    return repos_issue


if __name__ == '__main__':
    all_repos = get_trending_repositories(20)
    issues_amount = get_open_issues_amount(all_repos)
    for repo, issue in issues_amount.items():
        print('Repository %s had %d issues' % (repo, issue))