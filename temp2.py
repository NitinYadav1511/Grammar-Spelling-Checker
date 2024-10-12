from textblob import TextBlob
import language_tool_python

class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        self.grammar_check = language_tool_python.LanguageTool('en-US')

    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected_word = str(TextBlob(word).correct())
            corrected_words.append(corrected_word)
        return " ".join(corrected_words)

    def correct_grammar(self, text):
        matches = self.grammar_check.check(text)
        found_mistakes = []
        for match in matches:
            error_word = match.context.replace(match.ruleIssueType, "").strip()
            found_mistakes.append(error_word)
        found_mistakes_count = len(found_mistakes)
        return found_mistakes, found_mistakes_count

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "my mashine is woking for teacccher. apple. banana"
    print(obj.correct_spell(message))
    print(obj.correct_grammar(message))