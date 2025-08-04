"""
С помощью GitHub API через GraphQL для репозитория vscode (автор microsoft)
выгрузите последние 100 опубликованных issues. Постройте линейный график,
отображающий количества созданных issues по часам. Проанализируйте полученный
график и сделайте выводы.
"""

import requests
from token_1 import TOKEN

url = "https://api.github.com/graphql"
token = TOKEN

headers_github = {
    "Authorization": f"Bearer {token}",
    'Content-Type': 'application/json'
}

query_template = '''
query {
    repository(owner: "microsoft", name: "vscode") {
        name
        description
        issues(last:100, states:CLOSED) {
            edges {
                node {
                    id
                    title
                    url
                }
            }
        }
    }
}
'''

last_100_issues = []

response = requests.post(url, json={'query': query_template}, headers=headers_github)
if response.status_code == 200:
    data = response.json()['data']['repository']
    for issue in data['issues']['edges']:
        last_100_issues.append({issue['node']['title']: {
                                                      'id': issue['node']['id'],
                                                      'url': issue['node']['url']
                                                        }
                                })

else:
    print('ошибка', response.status_code)

for issue in last_100_issues:
    for key, value in issue.items():
        print('Title:', key, value)
