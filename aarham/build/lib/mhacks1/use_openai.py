import openai

def explain_error_with_gpt(error_message):
    openai.api_key = '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'
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Explain the following Python error and suggest possible solutions:\n\n{error_message}",
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error in contacting OpenAI API: {str(e)}"
