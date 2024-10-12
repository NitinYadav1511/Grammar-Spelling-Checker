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
            context = match.context
            error_word = context.replace(match.ruleIssueType, "").strip()
            start_index = context.find(error_word)
            end_index = start_index + len(error_word)
            found_mistakes.append((error_word, start_index, end_index))
        found_mistakes_count = len(found_mistakes)
        return [mistake[0] for mistake in found_mistakes], found_mistakes_count

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "my mashine is woking for teacccher. apple. banana"
    correct = obj.correct_spell(message)
    print(correct)
    print(obj.correct_grammar(correct))