from ars.boxmanager import BoxManager
from ars.qtype.shortanswer import ShortAnswer
from ars.qtype.truefalse import TrueFalse
from typing import List, Dict, Any, Optional

"""Core module for running the Adaptive Review System (ARS) session."""

class ARController:
    """Main controller for running an adaptive review session."""

    def __init__(self, question_data):
        """Initialize the Adaptive Review Controller.

        Args:
            question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
        """
        self._box_manager = BoxManager()
        self._initialize_questions(question_data)

    def _initialize_questions(self, question_data):
        """Initialize questions and place them in the Unasked Questions box.

        Args:
            question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
        """
        for i in question_data:
            qtype = i.get("type")
            try:
                if qtype == "shortanswer":
                    question = ShortAnswer(i["question"], i["correct_answer"], i.get("case_sensitive", False))
                elif qtype == "truefalse":
                    question = TrueFalse(i["question"], i["correct_answer"], i.get("explanation", ""))
                else:
                    print(f"Unsupported question type: {qtype}. Skipping this question.")
                    continue
                self._box_manager.add_new_question(question)
            except KeyError as e:
                print(f"Missing required field for question: {e}. Skipping this question.") 
    def start(self) -> None:
        """Run the interactive adaptive review session."""
        
        print("Type 'q' at any time to quit the session.")
        while(True):
            next_question = self._box_manager.get_next_question()
            if next_question:
                print(next_question.ask())
                user_answer = input("Please enter answer here: ")
                if user_answer == "q":
                    break
                correct = False
                try:
                    correct = next_question.check_answer(user_answer)
                    if correct:
                        print("Correct!")
                    else:
                        print(next_question.incorrect_feedback())
                except ValueError as e:
                    print(f"Invalid input: {e}")
                self._box_manager.move_question(next_question, correct)
            else:
                print("All questions have been reviewed. Session complete!")
                break
        print("Thank you, goodbye!")
