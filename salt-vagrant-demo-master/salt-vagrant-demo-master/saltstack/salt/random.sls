random_job:
 cmd.run:
   - name: 'python /{{ pillar['dir_root']}}/{{ pillar['project_name'] }}/app/test.py'