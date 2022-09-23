param (
    $AppPath = '.\glue\app.py',

    [switch]
    $FlaskDebug
)

if ($FlaskDebug) {
    $env:FLASK_DEBUG = 1
}

$env:FLASK_APP = $AppPath

Start-Process -FilePath 'flask.exe' -ArgumentList @('run') -WorkingDirectory $PSScriptRoot
