python-pip_pkg:
  pkg.installed:
    - names:
      - git
      - python-virtualenv
      - python-dev
      - python-dateutil

virtualenv_pkg:
  pkg.installed:
    - name: python-virtualenv

pip_pkg:
  pkg.installed:
    - name: python-pip

checkout_my_repo:
  git.latest:
    - name: {{ pillar['git_url'] }}
    - target: /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/
    - force_checkout: True

/home/mysite/venv:
    virtualenv.managed:
        - requirements: /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/requirements.txt
        - require:
            - pkg: python-pip_pkg

test_run:
 cmd.run:
   - name: 'python /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/app/test.py'

job2:
  schedule.present:
    - function: state.apply
    - job_args:
      - random
    - when:
        - Monday 4:40pm
        - Tuesday 6:10pm
        - Wednesday 4:00pm
        - Thursday 4:00pm
        - Friday 5:00pm