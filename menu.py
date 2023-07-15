import os
import sys
from rich.console import Console
from rich.prompt import Prompt
import importlib
from rich.progress import Progress
import time

console = Console()

def menu():
    while True:
        console.clear()
        os.system('clear')
        console.print("Options are [bold green]ACTIVE[/bold green]""\nOptions that are work in [bold medium_violet_red]PROGRESS[/bold medium_violet_red]"
            "\n1. [bold green]Help[/bold green]\n2. [bold green]AI Analysis[/bold green]\n3. [bold medium_violet_red]Live trading: [/bold medium_violet_red](In production) \n4. [bold green]About us[/bold green] \n5. [bold red]Exit[/bold red]",
            soft_wrap=False,
        )
        choice = Prompt.ask('\nChoose a task: (Enter the number)', choices=["1", "2"], default='5')


        if choice == '1':
            choice2()

        elif choice == '2':
            console.print('Exiting...')
            break

        else:
            console.print('Invalid choice. Please try again.')



# def about_us():
#     console.print('\nAndrew Carroll: Andrew Carroll is a man')
#     \
#     console.print('\nSlava Makeev: Slave Makeeve was born...')

#     console.print('\nJared Ciccarello: Woke up drunk', style='bold')
    
#     console.print('\nPress "enter" to [red]exit[/red]')
#     input()



def choice2():
    coin = Prompt.ask('\nChoose a coin: (Enter the number)')
    day_choice = Prompt.ask('\nChoose a dataset of [bold purple]30, 60, or 90 days[/bold purple]. (Enter the number)', choices=["30", "60", "90"], default='30')
    option_choice = Prompt.ask('\nChoose a strategy Conservative (C), Risky (R), Beginner (B)', choices=["Conservative", "Risky", "Beginner", "C", "R", "B"], default='4')
    
    if option_choice.lower() == "Conservative" or option_choice.lower() == "c":
        option_choice_validated = "conservative"

    elif option_choice.lower() == "Risky".lower() or option_choice.lower() == "r":
        option_choice_validated = "risky"

    elif option_choice.lower() == "Beginner".lower() or option_choice.lower() == "b":
        option_choice_validated = "beginner"
    else:
        exit    


    with Progress(console=console, transient=True) as progress:
        task = progress.add_task("[cyan]Loading...", total=10)
        for _ in range(10):
            progress.update(task, advance=1)
            time.sleep(0.2)  # Add a delay to simulate processing
        progress.stop()
    console.clear()

    user_input(coin, day_choice, option_choice_validated)
    
def user_input(coin, days, option):
    if days == "30" or days == "60" or days == "90":
        module_name = f"modules.gpt_controller"
        module = importlib.import_module(module_name)
        get_option = getattr(module, "get_option")
        get_option(coin, days, option)
        end_programm()
    else:
        exit
    
    
def end_programm():
    console.print('\nPress "enter" to [red]exit[/red]')
    input()
    exit



if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        console.print('\nCtrl+C detected. Exiting...')