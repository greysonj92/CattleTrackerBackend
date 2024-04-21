import yaml
import sys

def convert_env_to_requirements(env_file, req_file):
    print("Opening env yaml")
    with open(env_file, 'r') as file:
        env_yml = yaml.safe_load(file)
    
    requirements = []
    for dep in env_yml['dependencies']:
        if isinstance(dep, str):
            # Add directly to requirements if it's just a string
            requirements.append(dep)
        elif isinstance(dep, dict) and 'pip' in dep:
            # Add pip dependencies if present
            requirements.extend(dep['pip'])

    print("got all requirements")
    with open(req_file, 'w') as file:
        for req in requirements:
            file.write(req + '\n')
    print("wrote requirements.txt")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python convert.py environment.yml requirements.txt")
    else:
        convert_env_to_requirements(sys.argv[1], sys.argv[2])
