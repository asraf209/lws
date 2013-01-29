apt-get install libusb-1.0-0-dev
wget http://www.phidgets.com/downloads/libraries/libphidget.tar.gz
tar -xzvf libphidget.tar.gz 
cd libphidget-2.1.8.20121218/
./configure
make
make install
cd ..
sudo wget http://www.phidgets.com/downloads/libraries/PhidgetsPython.zip
unzip PhidgetsPython.zip
cd PhidgetsPython
python setup.py install

