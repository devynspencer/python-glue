param (
    $AppPath = "$PSScriptRoot\glue\app.py"
)

$env:FLASK_APP = $AppPath

Start-Process -FilePath 'flask.exe' -ArgumentList @('run')
