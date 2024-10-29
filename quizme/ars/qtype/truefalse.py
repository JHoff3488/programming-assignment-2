from ars.qtype.question import Question

"""Module for the TrueFalse quiz item class in the Adaptive Review System."""

class TrueFalse(Question):
    """Class for a True/False quiz item."""

    def __init__(self, question, answer, explanation = ""):
        """Initialize a true/false quiz item.
      
        Args:
            question (str): The question to be displayed.
            answer (bool): The correct answer, either True or False.
            explanation (str, optional): Additional information to explain the correct answer.

        Raises:
            ValueError: If the answer is not a boolean.
        """ 
        super().__init__(question, answer)
        self._explanation = explanation
        if isinstance(answer, bool):
            pass
        else:
            raise ValueError("The answer must be a boolean (True or False).")
        
    def ask(self) -> str:
        """Return the true/false question text."""
        super().ask()
        return f"{self._question} (True/False)"
    
    def check_answer(self, answer: str) -> bool:
        """Check if the provided answer is correct.
      
        Args:
            answer (str): The user's answer to the question.
            
        Returns:
            bool: True if the answer is correct, False otherwise.
            
        Raises:
            ValueError: If the answer is not 'True' or 'False'.
        """
        n_answer = answer.strip()
        n_answer = n_answer.lower()
        if n_answer == "true" or n_answer == "t":
            user_answer = True
        elif n_answer == "false" or n_answer == "f":
            user_answer = False
        else:
            raise ValueError("Answer must be 'True' or 'False'.")
        return user_answer == self._answer
    
    def incorrect_feedback(self) -> str:
        """Return feedback for an incorrect answer.

        Returns:
            str: Feedback message for an incorrect answer, including the explanation if provided.
        """
        
        if self._explanation:
            return f"Incorrect. {self._explanation}"
        else: 
            return "Incorrect. "
        
