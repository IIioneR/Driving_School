cd .
isort . -w 120
autopep8 --in-place --recursive .
echo success