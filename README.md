# akad12

sudo mkdir -p /opt/arp-daemon/
sudo cp s.py /opt/arp-daemon/
sudo cp systemd/arp_daemon.service /etc/systemd/system/

sudo chown -R root:root /opt/arp-daemon
sudo chmod +x /opt/arp-daemon/src/arp_daemon.py

sudo systemctl daemon-reload

sudo systemctl enable arp_daemon
sudo systemctl start arp_daemon

sudo journalctl -u arp_daemon -f