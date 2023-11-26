# Contexto
Nesse repositório se encontra o código necessário para a execução da parte relacionada ao gerador de modelo no trabalho prático 2 da disciplina de Computação em Nuvem

# Comandos
A seguir segue uma lista de comandos a serem utilizados para configuração do Docker, Kubernetes e ArgoCD. É necessário que eles sejam executados na pasta onde o repositório foi clonado para garantir seu funcionamento.

Também e necesário executar os comandos listados no repositório da API, https://github.com/pdrgbr/flask_api, para garantir o funcionamento do projeto como um todo.

## Montar imagem no Docker
docker image build -t model_generator_pedro .

## Executar imagem no Docker
docker run -d model_generator_pedro

## Buildar imagem a ser publicada no DockerHub
docker build -t pdrgbr/playlists-recommender:0.X .

## Publicar imagem no DockerHub
docker push pdrgbr/playlists-recommender:0.X

## Aplicar configurações do Kubernetes
kubectl -n pedroribeiro apply -f model_generator.yaml

kubectl -n pedroribeiro apply -f pvc.yaml

## Obter detalhes do Pod
kubectl describe pod gerador-pod-pedroribeiro-2 -n pedroribeiro   

## Deletar Pod
kubectl -n pedroribeiro delete pod gerador-pod-pedroribeiro-2

## Obter status do Kubernetes
kubectl -n pedroribeiro get pod 

## Criar aplicação no ArgoCD
argocd app create pedroribeiro-model-generator \
  --repo https://github.com/pdrgbr/model_generator \
  --path . \
  --project pedroribeiro-project \
  --dest-namespace pedroribeiro \
  --dest-server https://kubernetes.default.svc \
  --sync-policy automated \
  --self-heal \
  --auto-prune

## Obter status da aplicação no ArgoCD
argocd app get pedroribeiro-model-generator 

# Adendos

É extremamente importante garantir que o Persistent Volume esteja corretamente configurado para o funcionamento correto da aplicação.
