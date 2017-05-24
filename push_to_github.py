import github3
import os

def update_file(repo_file_path, contents):
	contents_object = repository.contents(repo_file_path)
	contents_object.update("Updated file ".format(repo_file_path), contents)

def create_new_file(repo_file_path, contents):
	repository.create_file(
        path=repo_file_path,
        message='Start tracking {!r}'.format(repo_file_path),
        content=contents
    )

file_paths = ['overall.html']
repo = 'drollscience.github.io'
remote_path = 'docs/'

user = os.environ['GITHUB']
pwd = os.environ['GITHUB_OTHER']

gh = github3.login(username=user, password=pwd)
repository = gh.repository(user, repo)


for file_path in file_paths:
	with open(file_path, 'rb') as fd:
		contents = fd.read()

	repo_file_path = remote_path + file_path #docs/overall.html

	remote_file_exists = repository.contents(repo_file_path)

	update_file(repo_file_path, contents) if remote_file_exists else create_new_file(repo_file_path, contents)



