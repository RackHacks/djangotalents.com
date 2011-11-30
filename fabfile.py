from fabric.api import *

def dev():
    return
    env.enviroment = 'dev'
    env.branch = 'dev'
    env.collect_static = False
    env.sync_db = True
    env.app_name = 'djangotalents'

def production():
    env.enviroment = 'production'
    env.branch = 'master'
    env.collect_static = True
    env.sync_db = False
    env.app_name = 'djangotalents'

def deploy(branch=None):
    if branch is not None:
        env.branch = branch

    command = 'git push --force {enviroment} {branch}:master'.format(**env)
    local(command)

    if env.collect_static:
        command = 'heroku run bin/python jobsite/manage.py collectstatic --noinput'
        local(command)

    if env.sync_db:
        command = 'heroku pg:reset DATABASE --confirm {app_name}'.format(**env)
        local(command)
        command = 'heroku run bin/python jobsite/manage.py syncdb --noinput'
        local(command)

