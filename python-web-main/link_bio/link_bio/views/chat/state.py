# state.py
import os

from openai import AsyncOpenAI

import reflex as rx

class TutorialState(rx.State):
    question: str = ""

    chat_history: list[tuple[str, str]] = []

    async def answer(self):
        client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
        
        context = "Eres un asistente médico. Responde solo preguntas relacionadas con la salud y medicina o datos que has respondido o historial del chat. Si la pregunta no está relacionada con estos temas, pide amablemente que se haga una pregunta médica. Además, si solamente menciona sintomas da recomendaciones de medicamentos comunes o remedios que pueda hacer ademas de recomendarle asistir al medico si es grave."
        
        messages = [
            {"role": "system", "content": context},
        ]
        
        for q, a in self.chat_history:
            messages.append({"role": "user", "content": q})
            messages.append({"role": "assistant", "content": a})
        
        messages.append({"role": "user", "content": self.question})
        
        session = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stop=None,
            temperature=0.7,
            stream=True,
        )

        answer = ""
        self.chat_history.append((self.question, answer))

        self.question = ""
        yield

        async for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield