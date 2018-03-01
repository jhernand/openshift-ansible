#!/bin/bash

# This script generates a Service which exposes the Origin controller manager
# process in a way that is mostly compatible with kube-controller-manager.
# Origin's controller manager process is a systemd managed service bound to
# 0.0.0.0:8444 on master nodes.
#
# Note that the Origin controller manager also contains the scheduler.
#
# TODO: Doesn't quite work yet with an `oc cluster up` deployment which uses an
# all-in-one process.

if [[ "$(oc get nodes -o go-template='{{ len .items }}')" -eq 1 ]]; then
  master_ips=$(oc get nodes -o jsonpath='{$.items[*].status.addresses[?(@.type=="InternalIP")].address}')
else
  master_ips=$(oc get nodes -l node-role.kubernetes.io/master=true -o jsonpath='{$.items[*].status.addresses[?(@.type=="InternalIP")].address}')
fi

cat <<-EOF
kind: Service
apiVersion: v1
metadata:
  name: kube-controller-manager
  namespace: kube-system
  labels:
    k8s-app: kube-controller-manager
spec:
  ports:
  - name: http-metrics
    port: 443
    protocol: TCP
    targetPort: 8444
EOF

cat <<-EOF
---
kind: Endpoints
apiVersion: v1
metadata:
  name: kube-controller-manager
  namespace: kube-system
subsets:
  - addresses:
EOF

for ip in $master_ips; do
cat <<-EOF
    - ip: $ip
EOF
done

cat <<-EOF
    ports:
    - name: http-metrics
      port: 8444
      protocol: TCP
EOF
