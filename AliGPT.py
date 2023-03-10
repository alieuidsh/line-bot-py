import openai
openai.api_key = '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'

class AliGPT:
    
    def CH_GPT(test):
        
        sam_text = test
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = sam_text ,
            max_tokens=1024,
            temperature=0.5,
            )

        completed_text = response["choices"][0]["text"]
        return completed_text

