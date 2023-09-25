#!/bin/bash
for palavra in $(cat listadns.txt)
do
resposta=$(curl -s -o /dev/null -H "User-Agent: Recontest"  -w "%{http_code}" $1/$palavra/)
if [ $resposta == "200" ]
then
echo "Diretorio encontrado: $1/$palavra/"
fi
done
