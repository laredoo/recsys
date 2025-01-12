import yaml

with open('configmap.yaml', 'r') as f:
    configmap = yaml.safe_load(f)

playlist_path = configmap['data']['PLAYLIST_PATH']
dataset_name = playlist_path.split('/')[-1].split('.')[0]

with open('./deployment.yaml', 'r') as f:
    deployment = yaml.safe_load(f)

deployment['metadata']['name'] = dataset_name

with open('./deployment.yaml', 'w') as f:
    yaml.safe_dump(deployment, f)

print(f"Updated deployment.yaml with metadata.name: {dataset_name}")