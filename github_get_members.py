from github import Github
import os

g = Github(f"{os.getenv('GITHUB_TOKEN')}")
org = g.get_organization("dnxlabs")
members = org.get_members()

xs = []
for t in members:
    xs.append(t.login)

s = ', '.join(xs)

print(s)