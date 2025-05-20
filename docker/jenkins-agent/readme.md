# Docker Commands

## Docker Build
sudo docker build -t my-jenkins-agent:custom -f docker/jenkins-agent/Dockerfile .

## Docker Push
sudo docker login
sudo docker tag my-jenkins-agent:custom piercemcgowan/my-jenkins-agent:custom
sudo docker push piercemcgowan/my-jenkins-agent:custom