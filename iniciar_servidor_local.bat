@echo off
echo ===================================================
echo Iniciando el portal web de Vinculo Tecnico
echo ===================================================
echo Abre tu navegador y visita: http://localhost:8000
echo.
echo Para detener el servidor, cierra esta ventana o presiona Ctrl+C.
echo.
python -m http.server 8000
pause
