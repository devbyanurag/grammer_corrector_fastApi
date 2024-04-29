from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

args = TTSettings(num_beams=5, min_length=1)



def grammar_corrector(text_input):
    try:
        # Add the prefix "grammar: " before each input 
        input=f'grammar: {text_input}'
        result = happy_tt.generate_text(input, args=args)

        print(result.text) # This sentence has bad grammar.
        return result.text
    except Exception as e:
        return None
        