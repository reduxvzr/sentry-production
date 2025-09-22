helm repo add sentry https://sentry-kubernetes.github.io/charts
helm repo update travelata
helm --namespace sentry template sentry travelata/sentry --dry-run=server --insecure-skip-tls-verify

POD_WEB=$(kubectl --namespace sentry get pods --selector role=web --field-selector status.phase=Running -o custom-columns=NAME:.metadata.name --no-headers | head -n 1)
if [ -z "$POD_WEB" ]; then
    helm --namespace sentry template sentry travelata/sentry --insecure-skip-tls-verify > manifest.yaml
else
    helm --namespace sentry template sentry travelata/sentry --set user.create=false --set hooks.enabled=false --set asHook=false --set kafka.provisioning.enabled=false --no-hooks --insecure-skip-tls-verify > manifest.yaml
fi

kubectl --namespace sentry apply --filename ./manifest.yaml --dry-run=server
kubectl --namespace sentry apply --filename ./manifest.yaml

for kind in deployment statefulset; do 
  kubectl --namespace sentry get $kind -o name | while read obj; do 
    kubectl --namespace sentry rollout status $obj
  done
done

for i in $(seq 1 450); do
  if [ "$(curl -s workers.k8s:5250/_health/)" = "ok" ]; then
    echo "Sentry started!"
    break
  else
    echo "not ready yet, retrying... ($i/100)"
    sleep 2
  fi
done
