Self-hosted Sentry: [official website](https://sentry.io/welcome/)

Chart for Helm: [github project link](https://github.com/sentry-kubernetes/charts)

## Секреты
Секреты нужно класть до деплоя по пути /mnt/sentry/secrets:
- `/mnt/sentry/secrets/sentry-secret.yaml` - секреты приложения.
- `/mnt/sentry/secrets/sentry-sentry-postgresql.yaml` - постгреса.

## Ошибка CSRF
Если возникает ошибка **Не удалось выполнить проверку CSRF**, то в values.yaml в HelmChartRepo нужно поменять значение **url:** на то, с которого происходит подключение.

## PV/PVC

Проще всего воспользоваться [local-path-provisioner](https://github.com/rancher/local-path-provisioner).
