import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, _ = process.communicate()
    return output
    

if __name__ == "__main__":
    player_1_count = 0
    player_2_count = 0

    for _ in range(50):
        # Replace the command with the actual command you want to execute
        command = ["python3", "AI_Runner.py", "6", "6", "2", "l", "../src/checkers-python/main.py", "Tools/Sample_AIs/Random_AI/main.py"]
        
        result = run_command(command)
        
        if "player 1 wins" or "Tie" in result:
            player_1_count += 1
    

    for _ in range(50):
        # Replace the command with the actual command you want to execute
        command = ["python3", "AI_Runner.py", "6", "6", "2", "l", "Tools/Sample_AIs/Random_AI/main.py", "../src/checkers-python/main.py"]
        
        result = run_command(command)
        
        if "player 2 wins" or "Tie" in result:
            player_2_count += 1
    
    print(f"Winrate as white (moving first): {player_2_count * 2}%")
    print(f"Winrate as black (moving second): {player_1_count * 2}%")
    print(f"Overall winrate: {player_1_count + player_2_count}% ")