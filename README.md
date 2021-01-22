
ansible-galaxy collection install -r ansible-requirements.yaml
sudo apt update
sudo apt install ansible

sudo apt install python3-dev python3-pip python3-venv
python3 -m venv --system-site-packages --prompt local-k8s .venv

K3S_TOKEN=cxLyKPNuZShbzWHXaCUI \
K3S_VERSION=v1.19.4-k3s1 \
    docker-compose up