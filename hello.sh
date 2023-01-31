#!/bin/bash
              
              a=2
              b=2
              c=$((a + b))
              
              echo "Bash says: Hello, World!"
              echo "$a + $b = $c"
              declare -a List = ("User1" "User2" "User3" )

		for val in ${List[@]}; do
 		echo $val
		done
