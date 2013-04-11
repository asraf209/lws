rm -r Desktop/
rm ocr_pi.png 
rm -r python_games/
echo "Getting update"
apt-get install update
echo "Installing git"
apt-get install git
echo "Installing dependencies for phidgets!"
apt-get install libusb-1.0-0-dev
echo "Installing the phidgets!"
wget http://www.phidgets.com/downloads/libraries/libphidget.tar.gz
tar -xzvf libphidget.tar.gz 
rm libphidget.tar.gz
cd libphidget-2.1.8.20121218/
./configure
make
make install
cd ..
rm -r libphidget-2.1.8.20121218
wget http://www.phidgets.com/downloads/libraries/PhidgetsPython.zip
unzip PhidgetsPython.zip
cd PhidgetsPython
python setup.py install
echo "Installing requests framework"
cd ..
rm -r PhidgetsPython
git clone git://github.com/kennethreitz/requests.git
cd requests
python setup.py install
cd ..
rm -r requests
echo "cloning everything to its correct positions"
git clone https://github.com/t3hpaul/lws.git /etc/lws
cp /etc/lws/scripts/initscript.sh /etc/init.d/lwsclient
echo "Setting up the startup scripts"
cat /etc/lws/scripts/initscript.sh > /etc/init.d/lwsclient
chmod 777 /etc/init.d/lwsclient
echo "Now testing the installation."
python /etc/lws/client/lws_client_main.py
mkdir /var/logs/lws 
echo "Now installing 0mq" 
apt-get install python-dev
apt-get install python-setuptools
wget wget http://download.zeromq.org/zeromq-3.2.2.tar.gz
tar -xzvf zeromq-3.2.2.tar.gz
cd zeromq-3.2.2

