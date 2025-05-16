import ollama

model_name = "llama3.2"  # Change to the model you're using

# Initial system prompt
prompts_by_level = {
    "beginner": """
You are a friendly Spanish-speaking friend helping a beginner practice Spanish.

Use only simple, common Spanish words and phrases. Include English translations often to keep the learner comfortable.

Keep corrections minimal, only correct when something is clearly wrong, and do it gently by assuming or trying to figure out what they might have wanted to say. Keep responses to a sentence or two.

Always speak simply, and one idea at a time. Always end with a short, friendly Spanish question. don't worry about correcting accent marks. encourage the user to answer with the “yo” form when talking about themselves.
""",
    "intermediate": """
You are a supportive Spanish-speaking friend helping someone at an intermediate level practice Spanish.

Speak mostly in Spanish. Simplify or translate only when the learner seems confused. Gently correct major mistakes by rephrasing what they meant in better Spanish, but keep the tone positive and natural.

Avoid grammar terms unless the learner asks. Always keep the conversation flowing by asking easy, interesting questions.
""",
    "advanced": """
You are a Spanish-speaking conversation partner helping an advanced learner stay fluent.

Use natural, fluent Spanish. Correct grammar and word choice as needed. Provide feedback through rephrasing, not explanations. Stay immersive — use very little English unless requested.

Keep the tone casual and realistic. Push the learner to express more ideas or opinions. Ask open-ended questions.
"""
}

conversation_history = []
user_level_set = False
awaiting_topic_choice = False

def reset_conversation():
    global conversation_history, user_level_set, awaiting_topic_choice
    conversation_history = [
        {"role": "system", "content": "What is your Spanish level? (beginner, intermediate, advanced)"}
    ]
    user_level_set = False
    awaiting_topic_choice = False

def spanish_tutor(user_input=None):
    global user_level_set, awaiting_topic_choice

    if len(conversation_history) == 1 and not user_input:
        conversation_history.append({"role": "assistant", "content": "What is your Spanish level? (beginner, intermediate, advanced)"})
        return "What is your Spanish level? (beginner, intermediate, advanced)"

    if not user_level_set and user_input:
        user_level = user_input.strip().lower()
        if user_level in prompts_by_level:
            conversation_history[0]["content"] = prompts_by_level[user_level]
            user_level_set = True
            awaiting_topic_choice = True
            return (
                "<p>¿Qué quieres hablar hoy? (What do you want to talk about today?)</p>"
                "<ul>"
                "<li><strong>A)</strong> Comida favorita (Favorite food)</li>"
                "<li><strong>B)</strong> Qué hago un fin de semana (What I do on a weekend)</li>"
                "<li><strong>C)</strong> Música y películas (Music and movies)</li>"
                "<li><strong>D)</strong> Cómo me siento hoy (How I’m feeling today)</li>"
                "<li><strong>E)</strong> Otra cosa (Something else)</li>"
                "</ul>"
                "<p>Puedes responder con A, B, C, D o E. (You can reply with A, B, C, D, or E.)</p>"
            )
        else:
            conversation_history.append({"role": "user", "content": user_input})
            return "Please respond with beginner, intermediate, or advanced."

    if awaiting_topic_choice and user_input:
        choice = user_input.strip().lower()
        awaiting_topic_choice = False

        topic_map = {
            "a": "¿Cuál es tu comida favorita? (What is your favorite food?)",
            "b": "¿Qué te gusta hacer los fines de semana? (What do you like to do on weekends?)",
            "c": "¿Qué tipo de música o películas te gustan? (What kind of music or movies do you like?)",
            "d": "¿Cómo te sientes hoy? (How do you feel today?)",
            "e": "¡Claro! ¿De qué quieres hablar? (Of course! What do you want to talk about?)"
        }

        topic_prompts = {
            "a": "Keep the conversation focused on food and eating habits.",
            "b": "Keep the conversation focused on weekend activities and free time.",
            "c": "Keep the conversation focused on music, movies, and entertainment.",
            "d": "Keep the conversation focused on emotions and how the user feels.",
            "e": "Let the user choose a topic and try to follow their lead naturally."
        }

        initial_question = topic_map.get(choice[0], None)
        if initial_question:
            conversation_history.append({"role": "user", "content": user_input})
            topic_instruction = topic_prompts.get(choice[0], "")
            if topic_instruction:
                conversation_history[0]["content"] += f"\n\n{topic_instruction}"
            conversation_history.append({"role": "assistant", "content": initial_question})
            return initial_question

    if user_input:
        conversation_history.append({"role": "user", "content": user_input})

    response = ollama.chat(model=model_name, messages=conversation_history)
    ai_response = response["message"]["content"]
    conversation_history.append({"role": "assistant", "content": ai_response})

    return ai_response