#!/bin/bash

if [$1 == ""]
 then
	echo "Uso incorreto colocar o ip do alvo"

else
for ip in {1..254};
do
	hping3  -c 1  -p 1337 $1.$ip -S | grep "flags=RA";
done
fi

