#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys
import httplib
import urllib
import urlparse
import json
import fnmatch
import re
from os import getenv
from subprocess import check_output
from subprocess import CalledProcessError

__author__ = 'xux'
"""
git_https_url_prefix = 'https://github.com/'
git_ssh_url_prefix = 'git@github.com:'
git_git_url_prefix = 'git://github.com/'
git_file_suffix = '.git'
github_header_accept = 'application/vnd.github.v3+json'
github_header_user_agent = 'TravisUploader/0.1'

DEVNULL = open(os.devnull, 'w')
repo_url = None

try:
    repo_url = check_output(['git', 'config', '--get', 'remote.origin.url']).splitlines()[0]
except CalledProcessError:
    print('No remote url for this project, abort')
    exit(0)

user_repo_name = None
if repo_url.startswith(git_ssh_url_prefix):
    user_repo_name = repo_url[len(git_ssh_url_prefix):]
elif repo_url.startswith(git_https_url_prefix):
    user_repo_name = repo_url[len(git_https_url_prefix):]
elif repo_url.startswith(git_git_url_prefix):
    user_repo_name = repo_url[len(git_git_url_prefix):]

if not user_repo_name:
    print('Not a github repo (%s), abort' % repo_url, file=sys.stderr)
    exit(0)

if user_repo_name.endswith(git_file_suffix):
    user_repo_name = user_repo_name[:-len(git_file_suffix)]


print user_repo_name

#github_access_token = getenv('GITHUB_ACCESS_TOKEN')
github_access_token="5794d6f8c0f3933da1647b39e7474ee671dc70c7"

if not github_access_token:
    print('No access token given, abort', file=sys.stderr)
    exit(0)

github_authorization_header = "token %s" % github_access_token

print('Creating release for tag %s' % current_tag)

conn = httplib.HTTPSConnection('api.github.com')
conn.request('POST', '/repos/%s/releases' % user_repo_name,
             body=json.dumps({
                 'tag_name': current_tag,
                 'name': "Version %s" % current_tag,
                 'body': current_tag_body
             }),
             headers={
                 'Accept': github_header_accept,
                 'Authorization': github_authorization_header,
                 'Content-Type': 'application/json',
                 'User-Agent': github_header_user_agent
             })
response = conn.getresponse()
print response
if response.status == 422:
    conn = httplib.HTTPSConnection('api.github.com')
    conn.request('GET', '/repos/%s/releases/tags/%s' % (user_repo_name, current_tag),
                 headers={
                     'Accept': github_header_accept,
                     'Authorization': github_authorization_header,
                     'User-Agent': github_header_user_agent
                 })
    response = conn.getresponse()

if response.status not in range(200, 204):
    print('Unable to create or get release, abort', file=sys.stderr)
    exit(0)

response_values = json.loads(response.read())
"""
print('-'*10)

#from git import Repo
#join = os.path.join
#repo = Repo(self.rorepo.working_tree_dir)
#print repo

import git
repo = git.Repo(self.rorepo.working_tree_dir)
print repo.git.status()
# checkout and track a remote branch
#print repo.git.checkout( 'origin/somebranch', b='somebranch' )
# add a file
#print repo.git.add( 'somefile' )
# commit
#print repo.git.commit( m='my commit message' )
# now we are one commit ahead
print repo.git.status()


#upload_url = urlparse.urlparse(re.sub('\{\?([\w\d_\-]+)\}', '', response_values['upload_url']))
for root, dirnames, filenames in os.walk(os.getcwd()):
    for filename in fnmatch.filter(filenames, '*-release.apk'):
        print(filename)
"""
        conn = httplib.HTTPSConnection(upload_url.hostname)
        conn.request('POST', "%s?%s" % (upload_url.path, urllib.urlencode({'name': filename})),
                     body=open(os.path.join(root, filename), 'r'),
                     headers={
                         'Accept': github_header_accept,
                         'Authorization': github_authorization_header,
                         'Content-Type': 'application/json',
                         'User-Agent': github_header_user_agent
                     })
        print("Upload %s returned %d" % (filename, conn.getresponse().status))
"""