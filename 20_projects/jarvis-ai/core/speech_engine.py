import speech_recognition as sr
import threading
import queue
from typing import Optional, Callable
import logging
from elevenlabs import play, VoiceSettings
from elevenlabs.client import ElevenLabs
import base64

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SpeechEngine:
    """
    Handles all speech recognition and text-to-speech operations.
    Optimized for macOS with threading for non-blocking operation.
    """
    
    def __init__(self, voice_rate: int = 180, voice_volume: float = 0.9):
        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000  # Adjust based on environment
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        
        self.tts_client = ElevenLabs(api_key="YOUR_ELEVENLABS_API_KEY")
        self.tts_voice = "Rachel"  # You can change this to any ElevenLabs voice
        
        # Thread-safe queue for TTS
        self.speech_queue = queue.Queue()
        self.is_speaking = False
        
        # Microphone setup
        self.microphone = sr.Microphone()
        
        logger.info("Speech engine initialized successfully")
    
    def speak(self, text: str, blocking: bool = False):
        """
        Convert text to speech.
        
        Args:
            text: Text to speak
            blocking: If True, wait for speech to complete
        """
        logger.info(f"Speaking: {text}")

        client = ElevenLabs(api_key="YOUR_ELEVENLABS_API_KEY")

        audio = client.text_to_speech.convert(
            voice_id=self.tts_voice,
            model_id="eleven_multilingual_v2",
            text=text,
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.8,
                style=0.0,
                use_speaker_boost=True
            )
        )

        play(audio)
    
    def listen(self, timeout: int = 5, phrase_time_limit: int = 10) -> Optional[str]:
        """
        Listen for voice input and convert to text.
        
        Args:
            timeout: Seconds to wait for speech to start
            phrase_time_limit: Maximum seconds for a phrase
            
        Returns:
            Recognized text or None if failed
        """
        try:
            with self.microphone as source:
                logger.info("Listening...")
                
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Listen for audio
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
                
                logger.info("Processing speech...")
                
                # Recognize speech using Google's API
                text = self.recognizer.recognize_google(audio)
                logger.info(f"Recognized: {text}")
                return text.lower()
                
        except sr.WaitTimeoutError:
            logger.warning("Listening timeout - no speech detected")
            return None
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Speech recognition service error: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in listen: {e}")
            return None
    
    def listen_continuous(self, callback: Callable[[str], None], wake_word: str = "jarvis"):
        """
        Continuous listening mode with wake word detection.
        
        Args:
            callback: Function to call when wake word detected
            wake_word: Word to activate JARVIS
        """
        logger.info(f"Starting continuous listening for wake word: '{wake_word}'")
        
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            while True:
                try:
                    logger.info("Waiting for wake word...")
                    audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=3)
                    
                    try:
                        text = self.recognizer.recognize_google(audio).lower()
                        
                        if wake_word in text:
                            logger.info("Wake word detected!")
                            self.speak("Yes, I'm listening")
                            callback()
                            
                    except sr.UnknownValueError:
                        continue
                    except sr.RequestError:
                        logger.error("Speech recognition service unavailable")
                        continue
                        
                except KeyboardInterrupt:
                    logger.info("Stopping continuous listening")
                    break
                except Exception as e:
                    logger.error(f"Error in continuous listening: {e}")
                    continue


# Test the speech engine
if __name__ == "__main__":
    engine = SpeechEngine()
    
    # Test TTS
    engine.speak("Hello! I am JARVIS, your AI assistant. Speech engine is working perfectly.")
    
    # Test STT
    engine.speak("Please say something")
    result = engine.listen()
    
    if result:
        engine.speak(f"You said: {result}")
    else:
        engine.speak("I didn't catch that")