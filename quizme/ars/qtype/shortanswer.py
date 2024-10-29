import re
from ars.qtype.question import Question

"""Module for the ShortAnswer quiz item class in the Adaptive Review System."""

class ShortAnswer(Question):
    """A quiz item representing a short answer question."""

    def __init__(self, question, answer, case_sensitive = False):
        """Initialize a short answer quiz item.

        Args:
            question (str): The question prompt.
            answer (str): The correct answer.
            case_sensitive (bool, optional): Whether the answer comparison should be case-sensitive. 
                                            Defaults to False.
        """
        super().__init__(question, answer)
        self._case_sensitive = case_sensitive
    
    def _normalize(self, text):
        """Normalize the text for comparison.

        Args:
            text (str): The text to normalize.

        Returns:
            str: The normalized text.
        """
        n_text = text.strip()
        if self._case_sensitive == False:
            n_text = n_text.lower()
        n_text = re.sub(r'[^\w\s]', '', n_text)
        return n_text
    
    def check_answer(self, answer):
        """Check if the provided answer is correct.

        Args:
            answer (str): The provided answer.

        Returns:
            bool: True if the provided answer is correct, False otherwise.
        """
        cor_answer = self._normalize(self._answer)
        user_answer = self._normalize(answer)
        return cor_answer == user_answer
    
    def incorrect_feedback(self):
        """Return feedback for an incorrect answer.

        Returns:
            str: Feedback message for an incorrect answer.
        """
        return f"Incorrect. The correct answer is: {self._answer}"
