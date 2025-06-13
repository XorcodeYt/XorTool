@echo off
REM Verification de Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH.
    pause
    exit /b 1
) else (
    echo [OK] Python est present.
)

REM Verification de Pip
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Pip n'est pas installe ou n'est pas accessible via Python.
    pause
    exit /b 1
) else (
    echo [OK] Pip est present.
)

REM === Installer les requirements ===
if exist requirements.txt (
    echo Installation des requirements...
    python -m pip install -r requirements.txt
) else (
    echo Fichier requirements.txt introuvable.
)

REM === Chemin d'installation de ffmpeg ===
set FF_DIR=C:\Programmes\ffmpeg
set FF_BIN=%FF_DIR%\bin

REM === Telecharger FFmpeg si absent ===
if not exist "%FF_BIN%\ffmpeg.exe" (
    echo Telechargement et installation de FFmpeg...
    if not exist "%FF_DIR%" mkdir "%FF_DIR%"
    powershell -Command "Invoke-WebRequest https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip -OutFile '%FF_DIR%\ffmpeg.zip'"
    powershell -Command "Expand-Archive -Path '%FF_DIR%\ffmpeg.zip' -DestinationPath '%FF_DIR%'"
    REM Recherche du dossier extrait
    for /d %%G in ("%FF_DIR%\ffmpeg-*") do (
        if exist "%%G\bin\ffmpeg.exe" (
            xcopy /Y /E /I "%%G\bin\*" "%FF_BIN%\"
        )
    )
    del "%FF_DIR%\ffmpeg.zip"
    REM Nettoyage des dossiers extraits
    for /d %%G in ("%FF_DIR%\ffmpeg-*") do (
        rmdir /S /Q "%%G"
    )
) else (
    echo FFmpeg deja installe dans %FF_BIN%
)

REM === Ajout de FFmpeg au PATH utilisateur ===
setx PATH "%PATH%;%FF_BIN%" >nul
echo FFmpeg ajoute a votre PATH utilisateur (nouveaux terminaux seulement).

echo.
echo [OK] Setup termine !
pause
