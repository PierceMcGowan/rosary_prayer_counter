# Docker Commands

## Docker Build
docker build -t my-jenkins-agent:custom -f docker/jenkins-agent/Dockerfile .

## Docker Push
docker login
docker tag my-jenkins-agent:custom piercemcgowan/my-jenkins-agent:custom
docker push piercemcgowan/my-jenkins-agent:custom