# Instruction

install the python requirements

`pip install -r requirements.txt`

run the  local server

`python api.py`

run the tests

`python test.py`

alternate test using curl

`curl --user john: localhost:5000//stocks`

for the docker file

`docker build -t littlejohn .`

then

`docker run -p 5000:5000 littlejohn`

make sure to stop the local server beacuse it uses the same port
