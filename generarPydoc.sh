mkdir -p doc
pydoc -w calif_practicas_app
pydoc -w calificador_practicas
cp *.html doc/
rm *.html
