# akad12

sudo mkdir -p /opt/arp-daemon/
sudo cp s.py /opt/arp-daemon/
sudo cp d.service /etc/systemd/system/

sudo chown -R root:root /opt/arp-daemon
sudo chmod +x /opt/arp-daemon/s.py


sudo systemctl daemon-reload

sudo systemctl enable d
sudo systemctl start d

sudo journalctl -u d -f
