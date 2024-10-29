from pathlib import Path
import json
from typing import List, Dict, Any
from ars.arcontroller import ARController
import argparse

"""
QuizMe: An adaptive quiz Command Line Interface (CLI) application.

This script allows users to take an adaptive quiz based on questions loaded from a JSON file.
It uses the Adaptive Review System (ARS) to manage the quiz session.
"""

def load_questions(file_path: Path) -> List[Dict[str, Any]]:
    """
    Load questions from a JSON file.

    Args:
        file_path (Path): Path to the JSON file containing quiz questions.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each representing a quiz question.

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with file_path.open('r') as f:
            #questions = json.load(file)
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Question file not found at {file_path}")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in question file {file_path}")
        raise
    
def run_quiz(name: str, questions: List[Dict[str, Any]]) -> None:
    """
    Run the adaptive quiz session.

    Args:
        name (str): The name of the quiz taker.
        questions (List[Dict[str, Any]]): A list of dictionaries containing question data.
    """
    print(f"Welcome, {name}! Let's start your adaptive quiz session.")
    controller = ARController(questions)
    controller.start()

def main() -> None:
    """
    Main function to set up and run the QuizMe CLI application.
    """
    parser = argparse.ArgumentParser(description="Online quiz app")
    parser.add_argument("name", type=str, help="This is your name")
    parser.add_argument("--questions", type=Path, required=True, help="Path to the question data file.")

    args = parser.parse_args()

    path = Path(args.questions)

    try:
        load = load_questions(path)

#        run_quiz(args.name, load)

    except Exception as e:
        print("Exiting due to error in loading questions.")
        return
    run_quiz(args.name, load)

if __name__ == "__main__":
    main()
