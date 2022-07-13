apt-get -qq install -y cmake qt5-default qt5-qmake qtbase5-dev-tools libboost-all-dev

cd rivet
mkdir build
cd build
cmake ..
make
cd ..
qmake
make
