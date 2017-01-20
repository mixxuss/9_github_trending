import requests
import datetime


# https://api.github.com/search/repositories?q=+created:%3E2017-01-13&sort=stars&order=desc&per_page=20
API_RESOURCE = 'https://api.github.com/'
PERIOD = str(datetime.date.today() - datetime.timedelta(days=7))


def get_trending_repositories(results_count):
    repos = requests.get(API_RESOURCE + 'search/repositories?q=+created:>' + PERIOD +
                         '&sort=stars&order=desc&per_page=' + str(results_count))
    return repos.json()['items']


def make_repos_list(repos_full_data):
    repos_list = [repo['full_name'] for repo in repos_full_data]
    return repos_list


def get_open_issues_amount(repo_full_names_list):
    issues_list = []
    for repo_name in repo_full_names_list:
        issues = requests.get(API_RESOURCE + 'repos/' + repo_name + '/issues').json()
        issues_list.append(issues)
    return issues_list


if __name__ == '__main__':
    all_repos = get_trending_repositories(20)
    # print(type(get_trending_repositories(20)))
    # print(make_repos_list(all_repos))
    all_opened_issues = make_repos_list(all_repos)
    repos_issue = {}
    for repo in all_repos:
        repos_issue[repo['html_url']] = repo['open_issues']
    print(repos_issue)
    '''print(all_opened_issues)
    for issues in all_opened_issues:
        issues_amount = 0
        for issue in issues:
            issues_amount += 1
        print(issues_amount)
'''
