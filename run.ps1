$env:FLASK_APP = '.\glue\app.py'

Start-Process -FilePath 'flask.exe' -ArgumentList @('run')
