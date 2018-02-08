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
    - force_reset: True
    - target: /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/


/home/mysite/venv:
    virtualenv.managed:
        - requirements: /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/requirements.txt
        - require:
            - pkg: python-pip_pkg

{% if '/home/mysite/venv' %}
testing_if:
  cmd.run:
    - name: 'echo "testing!"'
{% endif %}


create_env_file:
  cmd.run:
    - names:
      - '> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'touch /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "MAIL_SERVER=smtp.googlemail.com" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "SECRET_KEY=" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "MAIL_SERVER=smtp.googlemail.com" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "MAIL_PORT=465" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "MAIL_USE_TLS=False" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "MAIL_USE_SSL=True" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "MAIL_USERNAME=" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "MAIL_PASSWORD=" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "LINKEDIN:https=//www.linkedin.com/in/eduardoverde/" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "GITHUB=https://github.com/eiab30p/" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "TEST_WEB_URL=http://127.0.0.1:5000" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'echo "CHROME_WEB_DRIVER=D:/chromedriver.exe" >> /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'
      - 'cat /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/test.env'

#test_run:
# cmd.run:
#   - name: 'python /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/app/test.py'



#testJob:
#  schedule.present:
#    - function: state.apply
#    - job_args:
#      - random
#    - when:
#        - Monday 4:40pm
#        - Tuesday 6:10pm
#        - Wednesday 4:00pm
#        - Thursday 4:00pm
#        - Friday 5:00pm
