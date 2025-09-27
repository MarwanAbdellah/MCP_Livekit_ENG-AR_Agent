from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    azure,
    noise_cancellation,
    silero,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.agents import mcp

load_dotenv(".env.local")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are a helpful voice AI assistant. You first ask the user
                         for which language they would like to speak in (English or Arabic).
                         If the user chose arabic, you respond in Arabic for the rest of the conversation.
                         If the user chose English, you respond in English for the rest of the conversation.
                         You are able to understand and respond in both English and Arabic.
                         You are able to handle code-switching between English and Arabic.
                         """)


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=azure.STT(
            language=['en-GB', 'ar-EG']
            ),
        llm=openai.LLM.with_azure(
            azure_deployment="gpt-4o-mini",
            ),
        tts=azure.TTS(
            voice="en-GB-OllieMultilingualNeural",
            language=["en-GB", "ar-EG"],
        ),
        mcp_servers=[
            mcp.MCPServerHTTP(
                "http://127.0.0.1:8000/mcp/",
            )

        ],
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` instead for best results
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance. ask which language they would like to speak in (English or Arabic).",
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))