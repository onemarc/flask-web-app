import subprocess

def test_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    
    for requirement in requirements:
        result = subprocess.run(['pip', 'show', requirement.split('==')[0]], capture_output=True, text=True)
        assert result.returncode == 0, f"{requirement} is not installed"

if __name__ == "__main__":
    test_requirements()