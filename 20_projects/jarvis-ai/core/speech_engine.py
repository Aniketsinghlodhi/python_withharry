import os
import logging
from typing import Optional, Callable
from dotenv import load_dotenv

import speech_recognition as sr
from elevenlabs import play, VoiceSettings
from elevenlabs.client import ElevenLabs

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SpeechEngine:
    """
    Handles all speech recognition and text-to-speech operations.
    Optimized for macOS with robust error handling.
    TTS uses ElevenLabs; STT uses Google's speech recognition via SpeechRecognition.
    """

    def __init__(
        self,
        voice_id: Optional[str] = None,
        voice_rate: int = 180,
        voice_volume: float = 0.9,
    ):
        # ---- Speech Recognition Setup ----
        self.recognizer = sr.Recognizer()
        # Let the recognizer tune itself; keep a reasonable base threshold
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.energy_threshold = 300
        self.recognizer.pause_threshold = 0.8

        # ---- Microphone Setup ----
        try:
            # Default device; if this fails, user may need to set device_index explicitly
            self.microphone = sr.Microphone()
        except OSError as e:
            logger.error(
                "Could not initialize microphone. Check macOS microphone permissions "
                "for Terminal / VS Code and ensure an input device is connected. "
                f"Underlying error: {e}"
            )
            self.microphone = None

        # ---- ElevenLabs TTS Client Setup ----
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if not api_key:
            logger.error(
                "ELEVENLABS_API_KEY environment variable is not set. "
                "Text-to-speech will not work until you export this variable."
            )
            self.tts_client = None
        else:
            self.tts_client = ElevenLabs(api_key=api_key)

        # Voice ID: can be passed directly, taken from env, or set manually
        # IMPORTANT: This must be a valid ElevenLabs voice_id (UUID-style), not just a name.
        env_voice_id = voice_id or os.getenv("ELEVENLABS_VOICE_ID")
        self.voice_id = env_voice_id or "REPLACE_WITH_YOUR_VOICE_ID"

        # Store rate/volume for future extensions (not directly used by ElevenLabs)
        self.voice_rate = voice_rate
        self.voice_volume = voice_volume

        # Default voice settings
        self.voice_settings = VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.0,
            use_speaker_boost=True,
        )

        logger.info("Speech engine initialized successfully")

    # -------------------------------------------------------------------------
    # Text-to-Speech (TTS)
    # -------------------------------------------------------------------------
    def speak(self, text: str, blocking: bool = True) -> None:
        """
        Convert text to speech using ElevenLabs.

        Args:
            text: Text to speak.
            blocking: Reserved for future async handling. Currently always blocking.
        """
        if not text:
            logger.debug("speak() called with empty text; ignoring.")
            return

        if self.tts_client is None:
            logger.error(
                "speak() called but ElevenLabs client is not initialized. "
                "Ensure ELEVENLABS_API_KEY is set."
            )
            return

        if self.voice_id == "REPLACE_WITH_YOUR_VOICE_ID":
            logger.warning(
                "Using placeholder voice_id. Set ELEVENLABS_VOICE_ID or pass voice_id "
                "to SpeechEngine(...) for proper TTS."
            )

        logger.info(f"Speaking: {text}")

        try:
            # ElevenLabs Python SDK streaming TTS
            audio_stream = self.tts_client.text_to_speech.convert(
                voice_id=self.voice_id,
                model_id="eleven_multilingual_v2",
                text=text,
                voice_settings=self.voice_settings,
            )

            # audio_stream is an iterator over audio chunks
            for chunk in audio_stream:
                play(chunk)

        except Exception as e:
            logger.error(f"Error during TTS speak(): {e}")

    # -------------------------------------------------------------------------
    # Speech-to-Text (STT)
    # -------------------------------------------------------------------------
    def listen(self, timeout: int = 5, phrase_time_limit: int = 10) -> Optional[str]:
        """
        Listen for voice input and convert to text.

        Args:
            timeout: Seconds to wait for speech to start.
            phrase_time_limit: Maximum seconds for a phrase.

        Returns:
            Recognized text (lowercased) or None if failed.
        """
        if self.microphone is None:
            logger.error("listen() called but no microphone is available.")
            return None

        try:
            with self.microphone as source:
                logger.info("Listening...")

                # Adjust for ambient noise (quick calibration)
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit,
                )

            logger.info("Processing speech...")

            try:
                # Online Google Web Speech API
                text = self.recognizer.recognize_google(audio)
                logger.info(f"Recognized (Google): {text}")
                return text.lower()
            except sr.UnknownValueError:
                logger.warning("Could not understand audio (UnknownValueError).")
                return None
            except sr.RequestError as e:
                logger.error(f"Google STT service error: {e}")
                return None

        except sr.WaitTimeoutError:
            logger.warning("Listening timeout - no speech detected.")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in listen(): {e}")
            return None

    # -------------------------------------------------------------------------
    # Continuous listening with wake word
    # -------------------------------------------------------------------------
    def listen_continuous(
        self, callback: Callable[[str], None], wake_word: str = "jarvis"
    ) -> None:
        """
        Continuous listening mode with wake word detection.

        Args:
            callback: Function to call when wake word is detected. It will be called
                      with the full recognized text containing the wake word.
            wake_word: Word to activate JARVIS (case-insensitive).
        """
        if self.microphone is None:
            logger.error("listen_continuous() called but no microphone is available.")
            return

        wake_word = wake_word.lower()
        logger.info(f"Starting continuous listening for wake word: '{wake_word}'")

        try:
            with self.microphone as source:
                # Slightly longer calibration at start
                self.recognizer.adjust_for_ambient_noise(source, duration=1.0)

                while True:
                    try:
                        logger.info("Waiting for speech...")
                        audio = self.recognizer.listen(
                            source, timeout=None, phrase_time_limit=3
                        )

                        try:
                            text = self.recognizer.recognize_google(audio).lower()
                            logger.info(f"Heard: {text}")

                            if wake_word in text:
                                logger.info("Wake word detected!")
                                # Speak a short acknowledgement
                                self.speak("Yes, I'm listening")
                                # Pass the full recognized phrase to the callback
                                callback(text)

                        except sr.UnknownValueError:
                            # Just ignore unrecognized noise/speech
                            logger.debug("Unrecognized audio in continuous mode.")
                            continue
                        except sr.RequestError as e:
                            logger.error(
                                f"Speech recognition service unavailable in continuous mode: {e}"
                            )
                            continue

                    except KeyboardInterrupt:
                        logger.info("Stopping continuous listening (KeyboardInterrupt).")
                        break
                    except Exception as e:
                        logger.error(f"Error in continuous listening loop: {e}")
                        continue

        except Exception as outer_e:
            logger.error(f"Failed to start continuous listening: {outer_e}")


# -------------------------------------------------------------------------
# Standalone test
# -------------------------------------------------------------------------
if __name__ == "__main__":
    engine = SpeechEngine()

    # Test TTS
    engine.speak(
        "Hello! I am JARVIS, your AI assistant. Speech engine is working correctly."
    )

    # Test STT (only if microphone is available)
    if engine.microphone is not None:
        engine.speak("Please say something now.")
        result = engine.listen()

        if result:
            engine.speak(f"You said: {result}")
        else:
            engine.speak("I didn't catch that.")
    else:
        logger.error("Skipping STT test because no microphone is available.")