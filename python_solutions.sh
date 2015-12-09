#!/bin/bash 

# Obtain file name
# Run solve function from command line
# python3 -c 'import pe*; pe*.solve()'
#find . -type f -name '*.py' -exec basename {} \; | sed 's/\(pe[0-9]\{1,2\}\).py/\1/g'

filnames=`find . -name '*.py'`;
for f in ${filnames};
do
  dir=`echo ${f} | sed 's/\/pe[0-9]\{1,2\}.py//g'`;
  cd ${dir};
  pwd;
  module=`echo ${f} | sed 's/.\/pe[0-9]\{1,2\}\/\(pe[0-9]\{1,2\}\).py/\1/g'`;
  echo ${module};
  solution=`python -c "import ${module}; ${module}.solve()"`;
  echo -e "\033[0;32m${solution}\033[0m";
  cd ..;
done
